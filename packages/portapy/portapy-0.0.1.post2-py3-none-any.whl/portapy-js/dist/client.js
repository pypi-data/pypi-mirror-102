"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
var base_1 = require("./base");
var DatasetsService = /** @class */ (function (_super) {
    __extends(DatasetsService, _super);
    function DatasetsService() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    /**
     * Search existing datasets.
     */
    DatasetsService.prototype.searchDatasets = function () {
        var body = null, contentType = '';
        return this.call('GET', '/datasets/', {}, {
            'Content-Type': contentType,
        });
    };
    /**
       * Create a new dataset.
       */
    DatasetsService.prototype.createDataset = function (_req) {
        var body = null, contentType = 'application/json';
        if (contentType == 'application/json') {
            body = JSON.stringify(_req);
        }
        return this.call('PUT', '/datasets/', { _req: { value: body, where: 'body' }, }, {
            'Content-Type': contentType,
        });
    };
    /**
       * Add or update a dataset's content.
       */
    DatasetsService.prototype.updateDatasetContents = function (uid, _req) {
        var body = null, contentType = 'application/json';
        if (contentType == 'application/json') {
            body = JSON.stringify(_req);
        }
        return this.call('PUT', '/datasets/{uid}/documents', { uid: { value: uid, where: 'path' }, _req: { value: body, where: 'body' }, }, {
            'Content-Type': contentType,
        });
    };
    /**
       * Get a dataset's documents.
       */
    DatasetsService.prototype.getDatasetContents = function (uid) {
        var body = null, contentType = '';
        return this.call('GET', '/datasets/{uid}/documents/', { uid: { value: uid, where: 'path' }, }, {
            'Content-Type': contentType,
        });
    };
    /**
       * Get a dataset.
       */
    DatasetsService.prototype.getDataset = function (uid) {
        var body = null, contentType = '';
        return this.call('GET', '/datasets/{uid}/', { uid: { value: uid, where: 'path' }, }, {
            'Content-Type': contentType,
        });
    };
    /**
       * Delete a dataset.
       */
    DatasetsService.prototype.deleteDataset = function (uid) {
        var body = null, contentType = '';
        return this.call('DELETE', '/datasets/{uid}/', { uid: { value: uid, where: 'path' }, }, {
            'Content-Type': contentType,
        });
    };
    /**
       * Update a dataset metadata.
       */
    DatasetsService.prototype.updateDataset = function (uid) {
        var body = null, contentType = '';
        return this.call('PATCH', '/datasets/{uid}/', { uid: { value: uid, where: 'path' }, }, {
            'Content-Type': contentType,
        });
    };
    return DatasetsService;
}(base_1.BaseClientService));
var BaseService = /** @class */ (function (_super) {
    __extends(BaseService, _super);
    function BaseService() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(BaseService.prototype, "datasets", {
        /**
         * TODO: group description
         */
        get: function () {
            return new DatasetsService(this.session);
        },
        enumerable: true,
        configurable: true
    });
    return BaseService;
}(base_1.BaseClientService));
var Session = /** @class */ (function (_super) {
    __extends(Session, _super);
    function Session(url) {
        var _this = this;
        var session = new base_1.BaseSession(url);
        _this = _super.call(this, session) || this;
        return _this;
    }
    return Session;
}(BaseService));
exports.Session = Session;
