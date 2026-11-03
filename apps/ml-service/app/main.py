from fastapi import FastAPI

app = FastAPI(title="FieldShift AI ML Service")

@app.get("/health")
def health():
    return {"status": "ok"}
