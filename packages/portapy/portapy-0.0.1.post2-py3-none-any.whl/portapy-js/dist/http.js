"use strict";
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
Object.defineProperty(exports, "__esModule", { value: true });
var polyfills_1 = require("./polyfills");
/**
 * This class allows to perform HTTP requests like promises, but defines an interface
 * to abort pending requests if necessary. It abstracts the standard fetch API with
 * additional methods and can be used like a promise object.
 */
var HttpRequest = /** @class */ (function () {
    function HttpRequest(target, opts) {
        var _this = this;
        this.target = target;
        this.opts = opts;
        this.pipes = [];
        this.response = null;
        this.body = null;
        var options = __assign({}, opts);
        this.controller = new polyfills_1.AbortController();
        this.promise = new Promise(function (resolve, reject) {
            _this.request = polyfills_1.fetch(target, options);
            _this.request.then(function (response) {
                _this.response = response;
                _this.response.text().then(function (body) {
                    _this.body = body;
                    resolve();
                }, resolve);
            }, reject);
        });
    }
    /**
     * Get the requested URL.
     */
    HttpRequest.prototype.getTarget = function () {
        return this.target;
    };
    /**
     * Get the request options.
     */
    HttpRequest.prototype.getOptions = function () {
        return this.opts || {};
    };
    /**
     * Get the status code of the request.
     */
    HttpRequest.prototype.getStatusCode = function () {
        return this.response ? this.response.status : null;
    };
    /**
     * Get the response object.
     */
    HttpRequest.prototype.getResponse = function () {
        return this.response;
    };
    /**
     * Get the response body.
     */
    HttpRequest.prototype.getBody = function () {
        return this.body;
    };
    /**
     * Get the response body as json.
     */
    HttpRequest.prototype.getJSON = function () {
        if (this.body) {
            try {
                return JSON.parse(this.body);
            }
            catch (err) {
                // not valid json
            }
        }
        return null;
    };
    /**
     * Assign handlers for success and/or failure.
     */
    HttpRequest.prototype.then = function (onFulfilled, onRejected) {
        var _this = this;
        this.promise.then(function () {
            var response = _this.getResponse();
            if (response.status >= 400) {
                if (onRejected) {
                    onRejected(_this.getJSON(), _this);
                }
            }
            else if (onFulfilled) {
                var result = _this.getJSON();
                for (var _i = 0, _a = _this.pipes; _i < _a.length; _i++) {
                    var pipe = _a[_i];
                    result = pipe(result, _this);
                }
                onFulfilled(result, _this);
            }
        }, onRejected);
        return this;
    };
    /**
     * Assign a handler on failure.
     */
    HttpRequest.prototype.catch = function (onRejected) {
        return this.then(undefined, onRejected);
    };
    /**
     * Assign a handler that is always called, after the success and failure handlers.
     */
    HttpRequest.prototype.finally = function (onFinally) {
        this.promise.finally(onFinally);
        return this;
    };
    /**
     * Add a pipe to the request object.
     */
    HttpRequest.prototype.pipe = function (pipe) {
        this.pipes.push(pipe);
        return this;
    };
    /**
     * Abort the request if it's pending.
     */
    HttpRequest.prototype.abort = function () {
        return this.controller.abort();
    };
    return HttpRequest;
}());
exports.HttpRequest = HttpRequest;
