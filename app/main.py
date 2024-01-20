from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import controllers, deps

app = FastAPI(
    title="E-commerce API", openapi_url="/openapi.json"
)

api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}


@api_router.get("/products", status_code=200)
def get_products() -> dict:
    """
    Get all products
    """
    products = controllers.product.get_all(db=Depends(deps.get_db))
    if not products:
        raise HTTPException(status_code=404, detail="Products not found")
    return {"products": products}


@api_router.get("/products/{product_slug}", status_code=200)
def get_product(
    *,
    product_slug: str,
    db: Session = Depends(deps.get_db)
) -> dict:
    """
    Get a product
    """
    product = controllers.product.get_by_slug(db, id=product_slug)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"product": product}


app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
