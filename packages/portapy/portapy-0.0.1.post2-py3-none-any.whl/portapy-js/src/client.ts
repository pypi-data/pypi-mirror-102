import { BaseSession, BaseClientService } from './base';
import { HttpRequest } from './http';

export interface Dataset {
    title: string;
    created_at: Date;
    uid: string;

}

export interface Document {
    external_id: string;
    data: any;
    dataset: Dataset;
    upsert: any;
    created_at: Date;
    uid: string;

}

export interface UpdateDocumentRequest {
    external_id: string;
    data: any;

}

export interface CreateDatasetRequest {
    title: string;

}

class DatasetsService extends BaseClientService {
    /**
     * Search existing datasets.
     */
    public searchDatasets(): HttpRequest<Dataset[]> {

        const body = null, contentType = '';

        return this.call(
            'GET',
            '/datasets/',
            {},
            {
                'Content-Type': contentType,
            },
        );
    }
    /**
       * Create a new dataset.
       */
    public createDataset(_req: CreateDatasetRequest, ): HttpRequest<Dataset> {

        let body = null, contentType = 'application/json';

        if (contentType == 'application/json') {
            body = JSON.stringify(_req);
        }

        return this.call(
            'PUT',
            '/datasets/',
            { _req: { value: body, where: 'body' }, },
            {
                'Content-Type': contentType,
            },
        );
    }
    /**
       * Add or update a dataset's content.
       */
    public updateDatasetContents(uid: string, _req: UpdateDocumentRequest[], ): HttpRequest<any> {

        let body = null, contentType = 'application/json';

        if (contentType == 'application/json') {
            body = JSON.stringify(_req);
        }

        return this.call(
            'PUT',
            '/datasets/{uid}/documents',
            { uid: { value: uid, where: 'path' }, _req: { value: body, where: 'body' }, },
            {
                'Content-Type': contentType,
            },
        );
    }
    /**
       * Get a dataset's documents.
       */
    public getDatasetContents(uid: string, ): HttpRequest<Document[]> {

        const body = null, contentType = '';

        return this.call(
            'GET',
            '/datasets/{uid}/documents/',
            { uid: { value: uid, where: 'path' }, },
            {
                'Content-Type': contentType,
            },
        );
    }
    /**
       * Get a dataset.
       */
    public getDataset(uid: string, ): HttpRequest<Dataset> {

        const body = null, contentType = '';

        return this.call(
            'GET',
            '/datasets/{uid}/',
            { uid: { value: uid, where: 'path' }, },
            {
                'Content-Type': contentType,
            },
        );
    }
    /**
       * Delete a dataset.
       */
    public deleteDataset(uid: string, ): HttpRequest<null> {

        const body = null, contentType = '';

        return this.call(
            'DELETE',
            '/datasets/{uid}/',
            { uid: { value: uid, where: 'path' }, },
            {
                'Content-Type': contentType,
            },
        );
    }
    /**
       * Update a dataset metadata.
       */
    public updateDataset(uid: string, ): HttpRequest<any> {

        const body = null, contentType = '';

        return this.call(
            'PATCH',
            '/datasets/{uid}/',
            { uid: { value: uid, where: 'path' }, },
            {
                'Content-Type': contentType,
            },
        );
    }

}

class BaseService extends BaseClientService {

    /**
     * TODO: group description
     */
    public get datasets(): DatasetsService {
        return new DatasetsService(this.session);
    }

}

export class Session extends BaseService {

    constructor(url: string) {
        const session = new BaseSession(url);
        super(session);
    }

}