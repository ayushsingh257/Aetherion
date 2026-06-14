from fastapi import FastAPI

app = FastAPI(
    title="Aetherion",
    description="AI-Powered Cyber Investigation Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "project": "Aetherion",
        "status": "Backend Running"
    }