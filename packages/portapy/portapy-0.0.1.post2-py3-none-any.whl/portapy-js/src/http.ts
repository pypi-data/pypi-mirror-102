import { fetch, Response, AbortController } from './polyfills';
import { RequestInit } from './polyfills';

/**
 * This type is a handler that can be used to pipe functions to a HttpRequest object.
 */
export type HttpRequestPipe<R, T> = (response: T, request?: HttpRequest<T>) => R;

/**
 * This type is a handler that can be used to pipe functions to a HttpRequest object.
 */
export type HttpRequestHandler<T> = (response: T|null, request?: HttpRequest<T>) => void;

/**
 * This type is a handler that can be used to pipe functions to a HttpRequest object.
 */
export type HttpRequestError<T> = (reason?: any, request?: HttpRequest<T>) => void;

/**
 * Generic object interface.
 */
interface GenericObject<T> {
  [key: string]: T;
}

/**
 * This interface is used to provide HTTP options to requests.
 */
export type HttpRequestOptions = RequestInit;

/**
 * This interface is used to provide HTTP request headers to requests.
 */
export type HttpRequestHeaders = GenericObject<string>;

/**
 * This interface is used to provide HTTP request headers to requests.
 */
export type HttpRequestQuery = GenericObject<string|string[]>;

/**
 * This class allows to perform HTTP requests like promises, but defines an interface
 * to abort pending requests if necessary. It abstracts the standard fetch API with
 * additional methods and can be used like a promise object.
 */
export class HttpRequest<T> {

  private request?: Promise<Response>;
  private promise: Promise<void>;
  private pipes: Array<HttpRequestPipe<any, any>> = [];
  private controller: AbortController;
  private response: Response|null = null;
  private body: string|null = null;

  constructor(
    private target: string,
    private opts?: HttpRequestOptions,
  ) {
    const options = { ...opts };
    this.controller = new AbortController();
    this.promise = new Promise((resolve, reject) => {
      this.request = fetch(target, options);
      this.request.then((response) => {
        this.response = response;
        this.response.text().then((body) => {
          this.body = body;
          resolve();
        }, resolve);
      }, reject);
    });
  }

  /**
   * Get the requested URL.
   */
  public getTarget(): string {
    return this.target;
  }

  /**
   * Get the request options.
   */
  public getOptions(): HttpRequestOptions {
    return this.opts || {};
  }

  /**
   * Get the status code of the request.
   */
  public getStatusCode(): number|null {
    return this.response ? this.response.status : null;
  }

  /**
   * Get the response object.
   */
  public getResponse(): Response|null {
    return this.response;
  }

  /**
   * Get the response body.
   */
  public getBody(): string|null {
    return this.body;
  }

  /**
   * Get the response body as json.
   */
  public getJSON<T>(): T|null {
    if (this.body) {
      try {
        return JSON.parse(this.body);
      } catch (err) {
        // not valid json
      }
    }
    return null;
  }

  /**
   * Assign handlers for success and/or failure.
   */
  public then(onFulfilled?: HttpRequestHandler<T>, onRejected?: HttpRequestError<T>): HttpRequest<T> {
    this.promise.then(() => {
      const response = this.getResponse() as Response;

      if (response.status >= 400) {
        if (onRejected) {
          onRejected(this.getJSON(), this);
        }
      } else if (onFulfilled) {
        let result = this.getJSON();
        for (const pipe of this.pipes) {
          result = pipe(result, this);
        }
        onFulfilled(result as T, this);
      }
    }, onRejected);

    return this;
  }

  /**
   * Assign a handler on failure.
   */
  public catch(onRejected?: (reason: any) => void): HttpRequest<T> {
    return this.then(undefined, onRejected);
  }

  /**
   * Assign a handler that is always called, after the success and failure handlers.
   */
  public finally(onFinally?: () => void): HttpRequest<T> {
    this.promise.finally(onFinally);
    return this;
  }

  /**
   * Add a pipe to the request object.
   */
  public pipe<R = T>(pipe: HttpRequestPipe<R, T>): HttpRequest<R> {
    this.pipes.push(pipe);
    return this as any as HttpRequest<R>;
  }

  /**
   * Abort the request if it's pending.
   */
  public abort(): void {
    return this.controller.abort();
  }

}
