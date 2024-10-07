# Step 0

Let's start with the basics. An API allows us to interact with an app using code.

API
: Application Programming Interface

An API call consists of 2 parts:

1. Request
2. Response

REST
: Representational State Transfer

There is some controversy over just what `REST` actually means.
I will spare you the nerd fights and history lesson.

Here are the important bits:

- All the information that a server needs to serve a request is contained in the
request.
- When you get the response back that's the end of the conversation.
- Each new request is a whole new self-contained conversation.
REST is `stateless` in that it doesn't remember you from the last request you made.
- Each request is either a command or a query (more on this later).
- REST uses the `http` protocol.
There are other protocols that an API can use but we will focus on REST.
- An API that conforms to the REST style is called `RESTful`

We are going to start with the `GET` request.
What are you getting?
You are getting a `resource`.

Normally this is a document of some kind that contains structured data:

- HTML
- JSON
- XML

It can also be data such as

- Image
- PDF document

---

Start up the server in one terminal by running `flask run`

On your client terminal make a `GET` request
to the address `localhost` on `port` 5000.

```bash
http localhost:5000
```

localhost
: The server is running "locally", as in on your laptop and not out on the Internet.

port
: localhost is like the address to an appartment complex
and port is like a door number.
REST applications listen to a specific port and
there may be multiple APIs hosted on the same address.

---

On the server you should see something like this:

```bash
$ flask run
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [06/Oct/2024 23:44:29] "GET / HTTP/1.1" 200 -
```

The first column shows you the IP address of the client.
Note that `127.0.0.1` is the IP address for localhost.
The next column is the timestamp.
Next we see the request `verb`, `route`, and protocol.
More on verbs and routes later.
Next you will see the `status code`.
More on that later as well.
For now, just know that `200` = `OK`.

---

On the client you should see something like this:

```bash
$ http localhost:5000
HTTP/1.1 200 OK
Connection: close
Content-Length: 20
Content-Type: text/html; charset=utf-8
Date: Mon, 07 Oct 2024 03:44:29 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

<p>Hello, World!</p>

```

We see the request succeeded with the status `200 OK`.
The `Content-Type:` response `header` let's us know
the response will be in html format.
More on the different content types later. We will also go into headers in more depth.
Finally, we see the response `body` which is an html document.

Congrats! You just made your first API call!
