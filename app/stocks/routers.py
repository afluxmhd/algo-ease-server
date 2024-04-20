from fastapi import APIRouter, HTTPException
from random import uniform
from datetime import datetime
from .models import Stock

router = APIRouter()

@router.get("/stock-price/{name}",response_model=Stock)
async def get_current_price(name: str):
    current_price = round(uniform(400, 500), 2)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    stock = Stock(name=name,symbol='NOT_DEFINED',price=current_price,time=current_time)

    return stock
