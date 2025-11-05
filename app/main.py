from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "fast api 연결 성장"}