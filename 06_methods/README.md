# Request Methods & HTTP Verbs

The http resource is a noun and the http method is the verb.
It lets the API know what you want to do with the resource.
Refer to the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).

Here are the following methods we will cover:

- Get
- Head
- Post
- Put
- Patch
- Delete
- Options

These methods correspond roughly to the following CRUD
operations.

| Operation   | Method    |
|--------------- | --------------- |
| Create   | POST   |
| Read   | GET; HEAD  |
| Update   | PUT; PATCH   |
| Delete   | DELETE  |

`OPTIONS` is sometimes sent as a "preflight" request
to see what the API supports.
You will see an example of this in the `CORS` lab.
`HEAD` is like `GET` but only gets headers, not the body.
`PATCH` updates part of a resource.
`PUT` completely overwrites the old resource with a new copy.

## CRUD Lab

We are going to work with the following schema:

```json
{
  "id": "integer"
  "name": "string",
  "fav_color": "string"
}
```

We are going to use the following endpoint: `/colors/favorites`

### Create

Create an object recording that Mr. White's favorite color is black.
POST the request using JSON.

```bash
http POST localhost:5000/colors/favorites name="Mr. White" fav_color="black"
```

You will get an `id` back to reference this new object.

### Read

Confirm the previous request worked using the ID returned from the POST.

```bash
http GET localhost:5000/colors/favorites/1
```

### Update

Mr. White changed his mind. He likes purple now.
Use a PUT request to overwrite the existing object.
Confirm the change took with another GET.

```bash
http PUT localhost:5000/colors/favorites/1 name="Mr. White" fav_color="purple"
```

### Delete

Delete the object & then confirm with another GET request that should return `404`.

```bash
http DELETE localhost:5000/colors/favorites/1
http GET localhost:5000/colors/favorites/1
```
