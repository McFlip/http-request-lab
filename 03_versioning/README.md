# Semantic Versioning and Intro to Routes

SemVar
: A  versioning scheme that encodes a version by a three-part version number
(Major.Minor.Patch), an optional pre-release tag, and an optional build meta
tag. In this scheme, risk and functionality are the measures of significance.
Breaking changes are indicated by increasing the major number (high risk); new,
non-breaking features increment the minor number (medium risk); and all other
non-breaking changes increment the patch number (lowest risk).

Software and scripts are often built on top of APIs.
That's their main purpose.
Since software depends on APIs, developers need to know when a breaking
change is made to the API.
APIs provide a stable interface within the same major version.

See the [documentation](https://semver.org/) for more details.

Often API routes will begin with a version number.

This also demonstrates the concept of how resources can be organized by
different routes just like files on a file system can be organized
into different folders. A HTTP route is just like a file path.

## Versioning Lab

Get the `info` resource from both the `v1` and `v2` APIs.

```http
http GET localhost:5000/v1/info
HTTP/1.1 200 OK
Connection: close
Content-Length: 37
Content-Type: application/json
Date: Tue, 08 Oct 2024 03:01:24 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

{
    "msg": "Old and busted",
    "version": 1
}
```

```http
http GET localhost:5000/v2/info
HTTP/1.1 200 OK
Connection: close
Content-Length: 35
Content-Type: application/json
Date: Tue, 08 Oct 2024 03:01:29 GMT
Server: Werkzeug/3.0.4 Python/3.10.12

{
    "message": "New Hotness!",
    "version": 2
}
```

Since a field name was changed any code expecting a `msg`
field would break if it switched to the `v2` API.

APIs normally post release notes detailing breaking changes.
Well documented APIs will also provide a migration guide
to help you upgrade to the new version.
