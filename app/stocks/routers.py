from fastapi import APIRouter, HTTPException
from random import uniform
from datetime import datetime
from .models import StockReq,StockRes
from .stock_simulation import stock_simulation
from datetime import datetime

router = APIRouter()

@router.post("/stock-price",response_model=StockRes,include_in_schema=False)
async def get_current_price(stock : StockReq):
    # current_price = round(uniform(400, 500), 2)
    # current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # stock = Stock(name=name,symbol='NOT_DEFINED',price=current_price,time=current_time)
    # Instanse of stock simulation
    stockSimulation = stock_simulation()
    res = stockSimulation.stock_price(stock.status, stock.entry, stock.exit, stock.action)
    print(stock.status,stock.entry,stock.exit,stock.action,2)

    stockres = StockRes(
        symbol='NOT_DEFINED',
        name= stock.scrip,
        price= res,
        time= datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    )
    return stockres
