from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Server"}

@app.get("/api")
def api():
    return {"message": "Hello from API"}
