from flask import Flask

app = Flask(__name__)


@app.get("/welcome")
@app.get("/welcome/<page>")
def welcome(page=""):
    if page:
        html = f"<h1>Welcome {page}</h1>"
    else:
        html = "<h1>Welcome</h1>"
    return html