from fastapi import FastAPI

app = FastAPI(
    title="FastShop API",
    description="An API for managing a fast shop application.",
    version="1.0.0",
)


@app.get(
    path="/",
    tags=["Root"],
    summary="Root Endpoint",
    description="Welcome message for the FastShop API.",
)
async def read_root():
    return {"message": "Welcome to the FastShop API!"}
