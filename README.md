# http-request-lab

Learn how to use REST APIs. Demos built with HTTPie and Flask in Python.

This lab is aimed at beginners.

- You are not a programmer but you need to use APIs.
- You are a programmer that is learning API programming and
want to see some common examples.

This lab is inspired by [pie.dev](pie.dev)
which uses [httpbin.org](httpbin.org)

This lab will show you side-by-side the client and server.

## Prereqs

I suggest using [tmux](https://github.com/tmux/tmux/wiki) or some other terminal
multiplexer so that you can view the client and server terminals side-by-side.
If you are a using a GUI environment you can also tile 2 windows.
Another great option is to use [vscode](https://code.visualstudio.com/)
since it has a built-in terminal and markdown previewer.

Install [Python3](https://www.python.org/downloads/).

Clone this repo.

```bash
git clone git@github.com:McFlip/http-request-lab.git
cd http-request-lab
```

Create a virtual environment

```bash
python3 -m venv .venv
```

> [!NOTE]
>You may have to install `venv` first `sudo apt install python3.10-venv`
>*replace `3.10` with the appropriate version*
>
>In Windows use the `py` launcher instead of `python3`

Activate the environment.

On Linux:

```bash
. .venv/bin/activate
```

On Windows:

```PowerShell
.\Scripts\Activate.ps1
```

> [!NOTE]
> We will be opening multiple terminals, so remember to activate
> the environment on every terminal.

Install dependancies such as HTTPie and Flask

```bash
pip install -r requirements.txt
```

## How to use this lab

Click into each subfolder on this github page and read the `README`.

Run the server in one terminal window `flask run`

Execute the http request in the client terminal using `http`

When you are ready to move on, terminate the server by switching
to the server terminal and hitting `ctrl + c`.
Then change the server terminal to the next directory.
You don't have to change the client directory
except for labs 8 & 13.

## Lab TOC

0. [Hello World intro](/00_hello/README.md)
1. [Response codes](/01_status/README.md)
2. [JSON](/02_json/README.md)
3. [Semantic Versioning & intro to routes](/03_versioning/README.md)
4. [Dynamic routes](/04_routes/README.md)
5. [Query strings & URL encoding](/05_query/README.md)
6. [HTTP methods/verbs and CRUD](/06_methods/README.md)
7. [Forms](/07_forms/README.md)
8. [Files & Base64 encoding](/08_files/README.md)
9. [Headers & Auth Tokens](/09_headers/README.md)
10. [Cookies](/10_cookies/README.md)
11. [CORS](/11_cors/README.md)
12. [Redirects](/12_redirect/README.md)
13. [Rate limiting](/13_rate/README.md)

## Reference

- [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/)
- [HTTPie](https://httpie.io/)
