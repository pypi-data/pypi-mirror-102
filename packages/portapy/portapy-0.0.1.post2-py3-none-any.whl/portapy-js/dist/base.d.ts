import { HttpRequest, HttpRequestHeaders } from './http';
declare class RequestParams {
    [key: string]: {
        where: 'path' | 'header' | 'query' | 'body';
        value: string | string[] | null | object;
    };
}
export declare class BaseSession {
    readonly url: string;
    constructor(url: string);
    getHeaders(): HttpRequestHeaders;
}
export declare class BaseClientService {
    protected session: BaseSession;
    constructor(session: BaseSession);
    call<R = any>(method: string, endpoint: string, params?: RequestParams, headers?: HttpRequestHeaders): HttpRequest<R>;
}
export {};
