# Forms

Forms are the most common way to submit data on the web.
When you submit a form, the fields are encoded in the body of the request.
Forms are normally submitted using the POST method.

## Form lab

Fill in the following form and POST it to the `/order` route.

```json
"pizza_order": {
  "crust": "string",
  "sauce": "string",
  "topping": ["string"]
}
```

> [!NOTE]
> To send an array, just re-use the same key.
> To break up a command on multiple lines use `\`
> and hit `Enter`.

```http
http --form localhost:5000/order \
crust="thin crust" \
sauce="marinara" \
topping="peperroni" \
topping="black olives" \
topping="green olives"
HTTP/1.1 200 OK
Connection: close
Content-Length: 97
Content-Type: application/json
Date: Fri, 11 Oct 2024 17:01:04 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

{
    "crust": "thin crust",
    "sauce": "marinara",
    "toppings": [
        "peperroni",
        "black olives",
        "green olives"
    ]
}

```
