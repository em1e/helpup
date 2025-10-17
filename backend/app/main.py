from fastapi import FastAPI
from app.api import auth, users, requests

app = FastAPI(title="HelpUp API")

app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")
app.include_router(requests.router, prefix="/requests")

@app.get("/")
def read_root():
    return {"msg": "HelpUp API running"}