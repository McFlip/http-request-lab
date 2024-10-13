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
python3 -m venv .
```

>Note: You may have to install `venv` first `sudo apt install python3.10-venv`
>*replace `3.10` with the appropriate version*
>
> [!NOTE]
> In Windows use the `py` launcher instead of `python3`

Activate the environment.

On Linux:

```bash
. .venv/bin/activate
```

On Windows:

```PowerShell
.\venv\Scripts\Activate.ps1
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
You don't have to change the client directory.

## Lab TOC

0. Hello World intro
1. Response codes
2. JSON
3. Semantic Versioning & intro to routes
4. Dynamic routes
5. Query strings & URL encoding
6. HTTP methods/verbs and CRUD
7. Forms
8. Files & Base64 encoding
9. Headers & Auth Tokens
10. Cookies
11. CORS
12. Redirects
13. Rate limiting

## Reference

- [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/)
- [HTTPie](https://httpie.io/)
