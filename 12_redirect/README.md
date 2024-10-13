# Redirect

Redirects normally happen when a resource is moved.
They are also commonly used in authentication/authorization
login flows.
For example, if you use a "Login with Google" feature on a website,
the website will redirect you to the Google login.
Google will then ping-pong you back to the site you came from.
You may also see self-submitting forms as a way to get the browser
to do a POST redirect.

By default `httpie` does NOT follow redirects. You must specify the `follow` flag.
Please see the [documentation](https://httpie.io/docs/cli/http-redirects).

## Redirect lab

Try the following request with and without the redirect flag:

```http
http --follow localhost:5000
HTTP/1.1 200 OK
Connection: close
Content-Length: 24
Content-Type: text/html; charset=utf-8
Date: Sun, 13 Oct 2024 19:32:33 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

Please enter credentials
```

```http
http localhost:5000
HTTP/1.1 302 FOUND
Connection: close
Content-Length: 199
Content-Type: text/html; charset=utf-8
Date: Sun, 13 Oct 2024 19:32:56 GMT
Location: /login
Server: Werkzeug/3.0.4 Python/3.10.12

<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target
URL: <a href="/login">/login</a>. If not, click the link.

```

On the server you should see something like this:

```bash
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [13/Oct/2024 15:32:33] "GET / HTTP/1.1" 302 -
127.0.0.1 - - [13/Oct/2024 15:32:33] "GET /login HTTP/1.1" 200 -
127.0.0.1 - - [13/Oct/2024 15:32:56] "GET / HTTP/1.1" 302 -

```
