# http-request-lab

Learn how to use REST APIs. Demos built with HTTPie and Flask.

## Prereqs

I suggest using `tmux` or some other terminal multiplexer so that you can view
the client and server terminals side-by-side.
If you are a using a GUI environment you can also tile 2 windows.

Install [Python3](https://www.python.org/downloads/).

Clone this repo.

```bash
git clone git@github.com:McFlip/http-request-lab.git
cd http-request-lab
```

Create a virtual environment and install [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/).
>Note: You may have to install `venv` first `sudo apt install python3.10-venv`

Install Flask-CORS `pip install Flask-CORS`.

Install `HTTPie` `pip install httpie`

## How to use this lab

Click into each subfolder on this github page and read the `README`.

Run the server in one terminal window `flask run`

Execute the http request in the client terminal using `http`

When you are ready to move on, terminate the server by switching
to the server terminal and hitting `ctrl + c`.
Then change the server terminal to the next directory.
You don't have to change the client directory.
