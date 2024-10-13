# JSON

JSON
: Javascript Object Notation

I promised you more content types.
The most common way to transfer data via APIs is the JSON format.

Refer to the tutorial over at
[w3schools](https://www.w3schools.com/js/js_json_intro.asp)
to learn about JSON formatting.

We will practice sending a JSON request containing our name
and we should see a greeting in JSON returned.

```http
http POST localhost:5000/ name="My name is Jeff"
HTTP/1.1 200 OK
Connection: close
Content-Length: 33
Content-Type: application/json
Date: Tue, 08 Oct 2024 02:17:43 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

{
    "msg": "Hello, My name is Jeff"
}
```

As you can see, `httpie` makes things simple for us
by encoding and decoding JSON automatically.

We just have to provide `key`=`value` pairs after the route.
Don't forget to quote values that have spaces in them.
If you have multiple key-value pairs separate them with a space
like so `lname="Bond" fname="James"`.

There are other data formats such as XML and gRPC datagrams but JSON
is the defacto standard for APIs.

If you were paying attention, you would have noticed we also used a new method
called `POST`. We will cover all of the methods later.
