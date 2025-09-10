from fastapi.routing import Mount
from flask import Flask, render_template
from starlette.applications import Starlette
import uvicorn
from starlette.middleware.wsgi import WSGIMiddleware

flask_app = Flask(__name__)
app = Starlette(
    routes=[
        Mount("/", app=WSGIMiddleware(flask_app)),
    ],
)


@flask_app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="127.0.0.1",  # noqa: S104
        port=5000,
        reload=True,
    )
