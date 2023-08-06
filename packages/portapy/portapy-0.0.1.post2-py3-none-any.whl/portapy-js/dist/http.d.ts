import { Response } from './polyfills';
import { RequestInit } from './polyfills';
/**
 * This type is a handler that can be used to pipe functions to a HttpRequest object.
 */
export declare type HttpRequestPipe<R, T> = (response: T, request?: HttpRequest<T>) => R;
/**
 * This type is a handler that can be used to pipe functions to a HttpRequest object.
 */
export declare type HttpRequestHandler<T> = (response: T | null, request?: HttpRequest<T>) => void;
/**
 * This type is a handler that can be used to pipe functions to a HttpRequest object.
 */
export declare type HttpRequestError<T> = (reason?: any, request?: HttpRequest<T>) => void;
/**
 * Generic object interface.
 */
interface GenericObject<T> {
    [key: string]: T;
}
/**
 * This interface is used to provide HTTP options to requests.
 */
export declare type HttpRequestOptions = RequestInit;
/**
 * This interface is used to provide HTTP request headers to requests.
 */
export declare type HttpRequestHeaders = GenericObject<string>;
/**
 * This interface is used to provide HTTP request headers to requests.
 */
export declare type HttpRequestQuery = GenericObject<string | string[]>;
/**
 * This class allows to perform HTTP requests like promises, but defines an interface
 * to abort pending requests if necessary. It abstracts the standard fetch API with
 * additional methods and can be used like a promise object.
 */
export declare class HttpRequest<T> {
    private target;
    private opts?;
    private request?;
    private promise;
    private pipes;
    private controller;
    private response;
    private body;
    constructor(target: string, opts?: RequestInit | undefined);
    /**
     * Get the requested URL.
     */
    getTarget(): string;
    /**
     * Get the request options.
     */
    getOptions(): HttpRequestOptions;
    /**
     * Get the status code of the request.
     */
    getStatusCode(): number | null;
    /**
     * Get the response object.
     */
    getResponse(): Response | null;
    /**
     * Get the response body.
     */
    getBody(): string | null;
    /**
     * Get the response body as json.
     */
    getJSON<T>(): T | null;
    /**
     * Assign handlers for success and/or failure.
     */
    then(onFulfilled?: HttpRequestHandler<T>, onRejected?: HttpRequestError<T>): HttpRequest<T>;
    /**
     * Assign a handler on failure.
     */
    catch(onRejected?: (reason: any) => void): HttpRequest<T>;
    /**
     * Assign a handler that is always called, after the success and failure handlers.
     */
    finally(onFinally?: () => void): HttpRequest<T>;
    /**
     * Add a pipe to the request object.
     */
    pipe<R = T>(pipe: HttpRequestPipe<R, T>): HttpRequest<R>;
    /**
     * Abort the request if it's pending.
     */
    abort(): void;
}
export {};
