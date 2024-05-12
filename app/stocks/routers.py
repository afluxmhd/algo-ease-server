from fastapi import APIRouter, HTTPException
from random import uniform
from datetime import datetime
from .models import StockReq,StockRes
from .stock_simulation import StockSimulation
from datetime import datetime

router = APIRouter()

@router.post("/stock-price",response_model=StockRes,include_in_schema=False)
async def get_current_price(stock : StockReq):

    stock_simulation = StockSimulation()
    res = stock_simulation.stock_price(stock.status, stock.entry, stock.exit, stock.action)
    print(stock.status,stock.entry,stock.exit,stock.action,2)

    stockres = StockRes(
        symbol='NOT_DEFINED',
        name= stock.scrip,
        price= res,
        time= datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    )
    return stockres
