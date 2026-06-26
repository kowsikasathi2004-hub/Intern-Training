from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
products = []
class Product(BaseModel):
    name: str
    model: str
    cost: float
    character: str
@app.post("/products")
def add_product(product: Product):
     product_data = {
        "id": len(products) + 1,
        "name": product.name,
        "model": product.model,
        "cost": product.cost,
        "character": product.character
    }

    products.append(product_data)
    return {
        "message": "Product added successfully",
        "product": product_data
    }
@app.get("/products")
def get_products():
    return products
@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:

        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product Not Found"
    )
@app.put("/products/{product_id}")
def put_products(product_id: int, updated_product: Product):

    for product in products:

        if product["id"] == product_id:

            product["name"] = updated_product.name
            product["model"] = updated_product.model
            product["cost"] = updated_product.cost
            product["character"] = updated_product.character

            return {
                "message": "Product Updated Successfully",
                "product": product
            }

    raise HTTPException(
        status_code=404,
        detail="Product Not Found"
    )
@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    for product in products:

        if product["id"] == product_id:

            products.remove(product)

            return {
                "message": "Product Deleted Successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Product Not Found"
    )



    
