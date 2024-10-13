from flask import Flask

app = Flask(__name__)

@app.route("/")
def htmx_ajax():
  return """
<script src="https://unpkg.com/htmx.org@2.0.3"></script>
<meta name="htmx-config" content='{"selfRequestsOnly": false}' />
<button hx-get="http://localhost:5001/api/cors" hx-swap="outerHTML">
  Click Me
</button>
"""
