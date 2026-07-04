from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Server v1"}

@app.get("/api")
def api():
    return {"message": "Hello from API"}
