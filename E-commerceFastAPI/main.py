from fastapi import FastAPI
from routes import products

app = FastAPI(title="E-commerce API")

app.include_router(products.router)