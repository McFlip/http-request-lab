# CORS

CORS
: Cross-origin resource sharing - allows a web page to access restricted
resources from a server on a domain different than the domain that served
the web page.

Same-origin policy
: A type of security policy - Under the policy, a web browser permits
scripts contained in a first web page to access data in a second web page,
but only if both web pages have the same origin.

Origin
: combination of URI scheme, host name, and port number

When you are starting out with creating APIs,
a common error you will run into is having requests
denied due to violating the Same-origin policy.

This is because it is a common practice to split a website
into a front-end service and a back-end service.
The advantage to this approach is that clients other than
web browsers can access the back-end.
Therefore, developers only have to create one back-end,
while multiple front-end applications can connect to it.

This will only work if CORS is configured correctly
to allow requests from your origin or to allow
all origins with the wildcard character `*`.

The purpose of the Same-origin policy is to prevent a malicious site from
opening your for example, banking site inside of it and then accessing your banking
info using javascript.

## CORS lab

You will need an extra terminal for this as we will run 2 servers.

Run the front-end server at the default port 5000.

```bash
flask --app front run
```

Run the back-end server at the port 5001.

```bash
flask --app back run --port 5001
```

Check that you can access the back-end route `/api/cors` from the command line.

```http
http localhost:5001/api/cors
HTTP/1.1 200 OK
Access-Control-Allow-Origin: example.com
Connection: close
Content-Length: 58
Content-Type: text/html; charset=utf-8
Date: Sun, 13 Oct 2024 18:32:07 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

You should not be able to reach me by clicking the button.

```

Now open a browser and navigate to `localhost:5000`.
Open the developer console by hitting `ctl + shift + i`
Click the button.

You should see the following error message in the console:

```text
Access to XMLHttpRequest at 'http://localhost:5001/api/cors' from origin
'http://localhost:5000' has been blocked by CORS policy: Response to preflight
request doesn't pass access control check: No 'Access-Control-Allow-Origin'
header is present on the requested resource.
```

You can also see the error on the Network tab.

Fix the error by changing the CORS policy on `back.py`.
Change this line:

```Python
CORS(app, resources={r"/api/*": {"origins": "example.com"}})
```

To this:

```Python
CORS(app, resources={r"/api/*": {"origins": "*"}})
```

Restart the back-end server by hitting `ctrl + c`
and hit the `up arrow` and hit `enter`.

Hit refresh on the browser and click the button again.
