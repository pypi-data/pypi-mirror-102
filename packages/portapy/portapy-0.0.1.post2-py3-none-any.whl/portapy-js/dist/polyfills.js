"use strict";
var AbortController;
var Response;
var fetch;
if (typeof window !== "undefined") {
    fetch = function () {
        var args = arguments;
        var lst = Object.keys(args).map(function (key) {
            return args[key];
        });
        return window.fetch.apply(window, lst);
    };
    AbortController = window.AbortController;
    Response = window.Response;
}
else {
    fetch = require("node-fetch");
    var abortController = require("abort-controller");
    AbortController = abortController.AbortController;
    Response = fetch.Response;
}
module.exports = {
    AbortController: AbortController,
    RequestInit: {},
    Response: Response,
    fetch: fetch,
};
