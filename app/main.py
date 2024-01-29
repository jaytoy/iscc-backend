import logging
import json

from fastapi import FastAPI, APIRouter, Depends, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import Optional

from app import controllers
from app import deps
from app.schemas.product import Product
from app.services.pika_client import PikaClient

logger = logging.getLogger(__name__)


class App(FastAPI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pika_client = PikaClient()

        # Initialize CORS middleware
        origins = ["http://localhost", "http://localhost:8080"]
        self.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Include API Router
        self.include_router(api_router)


# API Router definition
api_router = APIRouter()

# Initialize FastAPI app
app = App(title="E-commerce API", openapi_url="/openapi.json")


@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}


@api_router.get("/products", status_code=200)
def get_products(
    *,
    db: Session = Depends(deps.get_db)
) -> dict:
    """
    Get all products
    """
    products = controllers.product.get_multi(db=db)
    return {"products": [Product.model_validate(product) for product in products]}


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
    request: Request
) -> dict:
    """
    Handle add-to-cart request and publish message to RabbitMQ
    """
    # Construct the message
    cart_item = {
        "product_slug": product_slug,
        "quantity": quantity if quantity is not None else "unspecified",
        "color": color if color is not None else "unspecified",
        "size": size if size is not None else "unspecified"
    }

    # Convert the object to a JSON string
    message = json.dumps(cart_item)

    request.app.pika_client.publish_message(
        {"message": message}
    )
    return {"message": "Product added to cart", "cart_item": cart_item}


app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
