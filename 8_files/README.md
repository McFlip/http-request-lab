# Files & Base64

We just looked at submitting forms and files are sometimes attached to forms.
We will cover both uploading and downloading files.

Base64
: A format for encoding binary data such as images in text.
Useful for transmitting files over the web.

## File upload & download lab

We will submit a form for creating a site profile with the following:

- Name
- Email
- Profile picture

POST the form to the route `/profile` with the text fields `name`, `email`
and attach a file to the `avatar` field.

First, make sure you change into the lab directory on the client side.
`cd 8_files`

```http
http --form localhost:5000/profile \
name="Zoned Out" \
email="z@meow.com" \
avatar@"upload.jpg"
HTTP/1.1 200 OK
Connection: close
Content-Length: 13350
Content-Type: application/json
Date: Fri, 11 Oct 2024 20:25:37 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

{
    "avatar": "/9j/4AAQSkZJRgABAQAAAQABAAD/
...truncated for brevety..."
    "email": "z@meow.com",
    "name": "Zoned Out"
}
```

That gigantic blob wall of text is the image you just uplodaded encoded in Base64.

Now let's download the image in `jpg` form.

Make a get download request to the route `/profile/avatar`

```http
http --download --output download.jpg localhost:5000/profile/avatar
```

On a unix-based system like Linux or MacOS you can use the `file` utility
to quickly check the file type of the file you just downloaded.

```bash
file download.jpg
download.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, progressive, precision 8, 360x360, components 3
```

On Windows, just open the file and you should see the black cat zoning out meme.

You can confirm that the file you downloaded is the same
as the one you uploaded by hashing the files.

```bash
sha1sum upload.jpg
5aea1825535286e6e60114cec112bac4c0372a6b  upload.jpg
sha1sum download.jpg
5aea1825535286e6e60114cec112bac4c0372a6b  download.jpg
```

On windows use the following:

```PowerShell
Get-FileHash -Algorithm "SHA1" -Path upload.jpg
```
