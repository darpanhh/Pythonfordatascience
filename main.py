from fastapi import FastAPI
from enum import Enum
app = FastAPI()

# @app.get("/hello/{name}")
# def hello(name):
#     return f"Hello {name}"
food_items = {
        'indian':["Samosa","Dosa"],
        'american':["Hot Dog","Apple Pie"],
        'italian':['Ravioli','Pizza']
    }

class AvailableCussines(str,Enum):
    indian = "indian"
    american = "american"
    italian = "italian"
    
@app.get("/get_cussine/{cussine}")
def get_food(cussine:AvailableCussines):
    return food_items.get(cussine)  

coupon_code ={
    1:'10%',
    2:'20%',
    3:'30%'
}
@app.get("/get_coupon/{code}")
async def get_items(code:int):
    return {'discount_amount':coupon_code.get(code)}
# @app.get("/get_cussine/{cussine}")
# def get_food(cussine):
#     items = food_items.get(cussine)
#     if not items:
#         return f"{cussine} cussine is not available"
#     return items

# @app.get("/")
# def hello():
#     return "Hello World"