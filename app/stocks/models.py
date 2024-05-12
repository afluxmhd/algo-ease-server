from fastapi import  Query
from pydantic import BaseModel

class StockRes(BaseModel):
    symbol: str
    name: str
    price: float
    time: str
    
    
class StockReq(BaseModel):
    scrip: str
    status : str = Query(..., choices=["executed","open","closed"])
    action : str = Query(..., choices=["buy", "sell"])
    entry : float
    exit : float

