# Query Strings

Query strings provide another way to pass arguments to a request.
You will commonly see this in Google searches.
If you Google `goth gf` you will see the following URL
at the top of your browser

```url
https://www.google.com/search?q=goth+gf&awholebuchofgarbage=whatever
```

The query string is everything after the `?`.
You will see `key`=`value` pairs.
You will also notice that there are no spaces.
The space character in `goth gf` was replaced with a `+` character.
This is known as URL encoding.
Multiple key-value pairs are separated by the `&` character.
Google knows what you searched for based on the `q` parameter.

## Query String Lab

Provide your `name` and favorite `food` arguments
to the `/search` endpoint to search for a recipe.

Example:

```http
http GET localhost:5000/search name=="Michelangelo" food=="Pizza"
HTTP/1.1 200 OK
Connection: close
Content-Length: 59
Content-Type: text/html; charset=utf-8
Date: Tue, 08 Oct 2024 04:05:12 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

Hello, Michelangelo, I also like Pizza! Here is a recipe...

```

Again, `httpie` makes our life simple by adding the `==` syntax.
That way you don't have to URL encode your values.
Also the `&` character has a special meaning in most shells.
