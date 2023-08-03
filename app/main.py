import sys

from absl import app, flags, logging
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Union
from prometheus_client import make_asgi_app

# NOTE on naming conventions: variables returned by the api are marked in camelCase, variables local to the script are in snake_case


version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()
FLAGS = flags.FLAGS
metrics_app = make_asgi_app()
path = "/metrics"
app.mount(path=path, app=metrics_app)
logging.info(f"Prometheus exporter mounted on {path}")


@app.get("/healthz")
async def health():
    return {"status": "ok"}


@app.get("/")
async def read_root():
    message = f"Hello World!"
    return {"message": message}


@app.post("/generate/")
async def infer(request: str):
    return {"response": f"This will eventually generate an image of a {request}"}

if __name__ == "__main__":
    logging.info("App started successfully")
