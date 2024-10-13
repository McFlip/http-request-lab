# Dynamic Routes

One of the ways a request can provide info
to the server is by the route used.
Different elements of a route can be designated as `dynamic`,
meaning they may change with every request.

Here is an example route for fetching a user by `userId`:

```url
/users/<userId>
```

A request to the route `/users/1234` will fetch the user
with ID `1234`.

## Routing Lab

Fetch the users `Alice` and `Bob`
using the endpoint

```url
/users/<userId>
```

| ID | Name |
| -------------- | --------------- |
| 1 | Alice |
| 2 | Bob   |

You should see the following:

```http
http GET localhost:5000/users/1
HTTP/1.1 200 OK
Connection: close
Content-Length: 17
Content-Type: application/json
Date: Tue, 08 Oct 2024 03:32:23 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

{
    "name": "Alice"
}
```

```http
http GET localhost:5000/users/2
HTTP/1.1 200 OK
Connection: close
Content-Length: 15
Content-Type: application/json
Date: Tue, 08 Oct 2024 03:32:30 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

{
    "name": "Bob"
}
```
