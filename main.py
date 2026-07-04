from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello dear hasbend.I Love you."}

@app.get("/api")
def api():
    return {"message": "I am Nibedita Roy, and my husband is very rude when he teaches me."}
