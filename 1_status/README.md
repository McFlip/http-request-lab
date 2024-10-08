# Response Status Codes

Refer to the Mozilla Developer Network
[MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) documentation.

Status codes are grouped into blocks of 100.

100s
: Info
200s
: Success
300s
: Redirect
400s
: Client error
500s
: Server error

We just saw an example of the `200 OK` Response.

`100` codes are not commonly seen.

The most common redirect codes are `307 Temporary Redirect` and `308 Permanent Redirect`.

We will cover redirects later.

The most common client error codes are

- `400 Bad Request` - You goofed up and fat-fingered something
or are generally doing something wrong.
- `403 Forbidden` - We will cover authentication later.
- `404 Not Found` - You have probably seen this in your browser.

The most common server error is `500 Internal Server Error`.
For security reasons, public APIs will not give detailed error messages.

## 404 Lab

0. Spin up the server as usual `flask run`
1. Read the poem at `localhost:5000/poem`
2. Attempt to get the resource at `localhost:5000/amour404`

You should see something like this

```http
http GET localhost:5000/poem
HTTP/1.1 200 OK
Connection: close
Content-Length: 637
Content-Type: text/html; charset=utf-8
Date: Tue, 08 Oct 2024 01:43:52 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

Once upon a midnight dreary, While I websurfed, weak and weary, Over many a
strange and spurious website of hot chicks galore,

While I clicked my fav'rite bookmark, Suddenly there came a warning, And my
heart was filled with mourning, Mourning for my dear amour.

'Tis not possible!, I pleaded, But my browser, so conceited, Remained blank, I
then repeated, Just a blank and nothing more.

With a scream, I was defeated, For my cookies were deleted, So i begged, no
longer seated, "Give me back my free hardcore!"

Then, in answer to my query, Through the net I loved so dearly, Came its answer,
dark and dreary: Quoth the server, 404
```

```http
http GET localhost:5000/amour404
HTTP/1.1 404 NOT FOUND
Connection: close
Content-Length: 207
Content-Type: text/html; charset=utf-8
Date: Tue, 08 Oct 2024 01:44:39 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL
manually please check your spelling and try again.</p>
</html>
```
