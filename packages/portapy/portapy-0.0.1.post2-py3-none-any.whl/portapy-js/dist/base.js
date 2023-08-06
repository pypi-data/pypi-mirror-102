"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var http_1 = require("./http");
var RequestParams = /** @class */ (function () {
    function RequestParams() {
    }
    return RequestParams;
}());
var BaseSession = /** @class */ (function () {
    function BaseSession(url) {
        this.url = url;
    }
    BaseSession.prototype.getHeaders = function () {
        return {};
    };
    return BaseSession;
}());
exports.BaseSession = BaseSession;
var BaseClientService = /** @class */ (function () {
    function BaseClientService(session) {
        this.session = session;
    }
    BaseClientService.prototype.call = function (method, endpoint, params, headers) {
        var url = "" + this.session.url + endpoint;
        var body = null;
        params = params || {};
        headers = headers || {};
        var sessionHeaders = this.session.getHeaders();
        for (var _i = 0, _a = Object.keys(sessionHeaders); _i < _a.length; _i++) {
            var key = _a[_i];
            headers[key] = sessionHeaders[key];
        }
        var parts = [];
        for (var _b = 0, _c = Object.keys(params); _b < _c.length; _b++) {
            var key = _c[_b];
            var value = params[key].value;
            switch (params[key].where) {
                case 'query':
                    key = encodeURIComponent(key);
                    if (value instanceof Array) {
                        for (var _d = 0, value_1 = value; _d < value_1.length; _d++) {
                            var item = value_1[_d];
                            item = encodeURIComponent(item);
                            parts.push(key + "=" + item);
                        }
                    }
                    else {
                        value = encodeURIComponent(value);
                        parts.push(key + "=" + value);
                    }
                    break;
                case 'header':
                    headers[key] = value;
                    break;
                case 'path':
                    url = url.replace("{" + key + "}", value);
                    break;
                case 'body':
                    body = value;
                    break;
            }
        }
        var options = { method: method, headers: headers, body: body };
        return new http_1.HttpRequest(url, options);
    };
    return BaseClientService;
}());
exports.BaseClientService = BaseClientService;
