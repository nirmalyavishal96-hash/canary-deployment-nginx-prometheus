from fastapi import FastAPI
import time
from prometheus_fastapi_instrumentator import Instrumentator
import logging

app = FastAPI()

Instrumentator().instrument(app).expose(app)

logging.basicConfig(level=logging.INFO)

@app.get("/")
def home():
    logging.info("Request received")
    return {"message": "Hello from v2"}

@app.get("/slow")
def slow_endpoint():
    time.sleep(2)
    return {"message": "This was slow"}

@app.get("/error")
def error():
    return 1 / 0

@app.get("/version")
def version():
    return {"version": "v2"}