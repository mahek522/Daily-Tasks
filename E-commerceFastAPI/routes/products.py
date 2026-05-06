from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from models.products import products_db
from schemas.product_validation import DataModel

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=DataModel, status_code=201)
def create_product(product: DataModel):
    for p in products_db:
        if p["id"] == product.id:
            raise HTTPException(status_code=400, detail="Product with this ID already exists")

    products_db.append(product.dict())
    return product


@router.get("/", response_model=List[DataModel])
def get_products(category: Optional[str] = None, price: Optional[float] = None):
    result = products_db

    if category:
        result = [p for p in result if p["category"].lower() == category.lower()]

    if price:
        result = [p for p in result if p["price"] <= price]

    return result


@router.get("/{id}", response_model=DataModel)
def get_product(id: int):
    for p in products_db:
        if p["id"] == id:
            return p
    raise HTTPException(status_code=404, detail="Product not found")


@router.put("/{id}", response_model=DataModel)
def update_product(id: int, updated_product: DataModel):
    for index, p in enumerate(products_db):
        if p["id"] == id:
            products_db[index] = updated_product.dict()
            return updated_product

    raise HTTPException(status_code=404, detail="Product not found")


@router.delete("/{id}")
def delete_product(id: int):
    for index, p in enumerate(products_db):
        if p["id"] == id:
            products_db.pop(index)
            return {"message": "Product deleted successfully"}

    raise HTTPException(status_code=404, detail="Product not found")