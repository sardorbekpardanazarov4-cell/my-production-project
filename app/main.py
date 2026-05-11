from fastapi import FastAPI

app = FastAPI(title="Production API")

@app.get("/")
def read_root():
    return {"status": "success", "message": "CI/CD Pipeline ishlamoqda!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}
