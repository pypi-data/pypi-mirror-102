import { BaseClientService } from './base';
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
declare class DatasetsService extends BaseClientService {
    /**
     * Search existing datasets.
     */
    searchDatasets(): HttpRequest<Dataset[]>;
    /**
       * Create a new dataset.
       */
    createDataset(_req: CreateDatasetRequest): HttpRequest<Dataset>;
    /**
       * Add or update a dataset's content.
       */
    updateDatasetContents(uid: string, _req: UpdateDocumentRequest[]): HttpRequest<any>;
    /**
       * Get a dataset's documents.
       */
    getDatasetContents(uid: string): HttpRequest<Document[]>;
    /**
       * Get a dataset.
       */
    getDataset(uid: string): HttpRequest<Dataset>;
    /**
       * Delete a dataset.
       */
    deleteDataset(uid: string): HttpRequest<null>;
    /**
       * Update a dataset metadata.
       */
    updateDataset(uid: string): HttpRequest<any>;
}
declare class BaseService extends BaseClientService {
    /**
     * TODO: group description
     */
    get datasets(): DatasetsService;
}
export declare class Session extends BaseService {
    constructor(url: string);
}
export {};
