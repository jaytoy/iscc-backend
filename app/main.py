from fastapi import FastAPI, APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional

from app import controllers
from app import deps
from app.schemas.product import Product

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


@api_router.get("/products/{product_slug}", status_code=200)
def get_product(
    *,
    product_slug: str,
    db: Session = Depends(deps.get_db)
) -> dict:
    """
    Get a product by slug
    """
    product = controllers.product.get_by_slug(db=db, slug=product_slug)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"product": Product.model_validate(product)}


@api_router.post("/add-to-cart/{product_slug}", status_code=200)
async def add_to_cart(
    *,
    product_slug: str,
    quantity: Optional[int] = Query(None),
    color: Optional[str] = Query(None),
    size: Optional[str] = Query(None),
    db: Session = Depends(deps.get_db)
) -> dict:
    """
    Add a product to cart
    """
    quantity_part = f"with quantity of {quantity}" if quantity is not None else ""
    size_part = f"size {size}" if size is not None else ""
    color_part = f"{color} color" if color is not None else ""

    message = f"Product '{product_slug}', {quantity_part}, {size_part}, {color_part} added to cart"

    message = ' '.join(message.split()).replace(" ,", ",")

    return {"message": message}


app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
