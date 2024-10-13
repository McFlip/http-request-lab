# Headers and Authentication

Data can be passed in a request in the header as well as the body.

A common use case for request headers is passing an auth token.
REST is stateless so there are no sessions.
A token must be passed along with every request to a protected endpoint.

## Bearer token lab

First make a request to the root which is public

```http
http localhost:5000/
HTTP/1.1 200 OK
Connection: close
Content-Length: 19
Content-Type: text/html; charset=utf-8
Date: Sat, 12 Oct 2024 17:01:36 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

Publicly accessible
```

Now make a request to `/secret`.
It should get rejected.

```http
HTTP/1.1 403 FORBIDDEN
Connection: close
Content-Length: 41
Content-Type: text/html; charset=utf-8
Date: Sat, 12 Oct 2024 23:59:34 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

Ah Ah Uh... You did't say the magic word!

```

Now add the bearer auth token `SecretSquirrel`

```http
http -A bearer -a "SecretSquirrel" localhost:5000/secret
HTTP/1.1 200 OK
Connection: close
Content-Length: 24
Content-Type: text/html; charset=utf-8
Date: Sun, 13 Oct 2024 00:02:52 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

The answer to life is 42

```

Use the `offline` flag to see how the token is attached to the request header.

```http
http --offline -A bearer -a "SecretSquirrel" localhost:5000/secret
GET /secret HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Bearer SecretSquirrel
Connection: keep-alive
Host: localhost:5000
User-Agent: HTTPie/3.2.2

```

> [!NOTE]
> In a real production app, something like a JSON Web Token [(JWT)](https://jwt.io/)
> would be used instead of a passphrase.
> [!NOTE]
> You can use the [session](https://httpie.io/docs/cli/sessions) feature
> of httpie to avoid having to re-type auth headers
> for each request

One final Note:

> Life is not a problem to be solved, but a reality to be experienced.
> \- Soren Kierkegaard
