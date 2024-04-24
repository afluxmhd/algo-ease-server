from fastapi import APIRouter, HTTPException
from random import uniform
from datetime import datetime
from .models import Strategy, StrategyModel

router = APIRouter()

@router.post("/strategy/submit", response_model=StrategyModel,include_in_schema=False)
async def submit_strategy(strategy: Strategy):

    processed_strategy_data = {
        "scrip": "AAPL",
        "action": "Buy",
        "entry": 150.0,
        "exit": 160.0,
        "entry_time": "2024-04-20 09:30:00",
        "exit_time": "2024-04-20 15:30:00",
        "quantity": 100,
        "risk": 50.0,
        "max_loss": 100.0,
        "max_profit": 200.0,
        "risk_reward": 2.0
    }
   
    return StrategyModel


