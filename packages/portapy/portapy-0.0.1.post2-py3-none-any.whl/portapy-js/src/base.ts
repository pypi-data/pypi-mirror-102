import { HttpRequest, HttpRequestHeaders, HttpRequestOptions, HttpRequestQuery } from './http';

class RequestParams {
  [key: string]: {
    where: 'path'|'header'|'query'|'body';
    value: string|string[]|null|object;
  }
}

export class BaseSession {

  constructor(
    public readonly url: string,
  ) { }

  public getHeaders(): HttpRequestHeaders {
    return {};
  }

}

export class BaseClientService {

  constructor(
    protected session: BaseSession,
  ) { }

  public call<R = any>(
    method: string,
    endpoint: string,
    params?: RequestParams,
    headers?: HttpRequestHeaders,
  ): HttpRequest<R> {
    let url = `${this.session.url}${endpoint}`;
    let body = null;
    params = params || {};
    headers = headers || {};

    const sessionHeaders = this.session.getHeaders();
    for (const key of Object.keys(sessionHeaders)) {
      headers[key] = sessionHeaders[key];
    }

    const parts = [];
    for (let key of Object.keys(params)) {
      let value: any = params[key].value;

      switch (params[key].where) {
        case 'query':
          key = encodeURIComponent(key)
          if (value instanceof Array) {
            for (let item of value) {
              item = encodeURIComponent(item);
              parts.push(`${key}=${item}`);
            }
          } else {
            value = encodeURIComponent(value);
            parts.push(`${key}=${value}`);
          }
          break;
        case 'header':
          headers[key] = value;
          break;
        case 'path':
          url = url.replace(`{${key}}`, value);
          break;
        case 'body':
          body = value;
          break;
      }
    }

    const options: HttpRequestOptions = { method, headers, body };
    return new HttpRequest<R>(url, options);
  }

}
