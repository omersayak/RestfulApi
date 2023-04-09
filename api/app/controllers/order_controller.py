from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()


# Temporary storage for orders
orders = []


# Route to create an order in a specific category
@app.post("/orders/{category}")
async def create_order(category: str, item: str):
    order = {
        "category": category,
        "item": item
    }
    orders.append(order)
    return order


# Route to get orders for a specific category
@app.get("/orders/{category}")
async def read_orders(category: str):
    category_orders = [order for order in orders if order["category"] == category]
    if not category_orders:
        raise HTTPException(status_code=404, detail="Orders not found")
    return category_orders


# Route to list all orders
@app.get("/orders")
async def read_all_orders():
    return orders

  
# Route to update an order
@app.put("/orders/{category}/{item}")
async def update_order(category: str, item: str, new_item: str):
    order_to_update = None
    for order in orders:
        if order["category"] == category and order["item"] == item:
            order_to_update = order
            break
    if not order_to_update:
        raise HTTPException(status_code=404, detail="Order not found")
    order_to_update["item"] = new_item
    return order_to_update


# Route to delete an order
@app.delete("/orders/{category}/{item}")
async def delete_order(category: str, item: str):
    order_to_delete = None
    for order in orders:
        if order["category"] == category and order["item"] == item:
            order_to_delete = order
            break
    if not order_to_delete:
        raise HTTPException(status_code=404, detail="Order not found")
    orders.remove(order_to_delete)
    return {"message": "Order deleted successfully"}