# Cookies

Cookies are primarily used to create the illusion of sessions
in a stateless protocol.
They are often used to record preferences.
Cookies are sent along with every request.

## Cookie lab

Send the following request with the cookies for
theme and language preferences.

```http
http localhost:5000/ 'Cookie:theme=dark;language=english'
HTTP/1.1 200 OK
Connection: close
Content-Length: 38
Content-Type: application/json
Date: Sun, 13 Oct 2024 00:34:35 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

{
    "language": "english",
    "theme": "dark"
}

```

> [!NOTE]
> You can use the [session](https://httpie.io/docs/cli/sessions) feature
> of httpie to avoid having to re-type cookie data
> for each request
