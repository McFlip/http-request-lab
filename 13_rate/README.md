# Rate limiting and scripting

If you poll an API in a script, it is best-practice
to limit the rate of your requests.
This is to prevent overwhelming the service.
Also, some services will block you if they think
you are trying to launch a DOS attack.

Polling
: Continuosly sending the same request to look for changes.

DOS
: Denial of Service

## Scripting lab

`httpie` is meant for interactive use but you can look
at the [docs](https://httpie.io/docs/cli/scripting) if you want to
use it in BASH or PowerShell scripts.

We will be using the Python `Requests` library
which is what `httpie` is built on top of.
It should automatically be installed as a
dependancy.

Run the server in lab 0.

Now execute the `limit.py` script and notice the 1 second delay
between requests. It will make 3 requests total.

```BASH
cd 13_rate/
python3 ./limit.py
```
