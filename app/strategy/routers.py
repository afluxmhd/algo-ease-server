from fastapi import APIRouter, HTTPException
from random import uniform
from datetime import datetime
from .models import Strategy, StrategyModel,StrategyDescription

router = APIRouter()

@router.post("/strategy/interpret", response_model=StrategyModel,include_in_schema=False)
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
   
    return StrategyModel(**processed_strategy_data)

@router.get("/strategy/description", response_model=StrategyDescription)
async def get_strategy_description():
    strategy_description = {
        "scrip": "Stock symbol representing the asset being traded.",
        "action": "Specifies whether to initiate a 'Buy' or 'Sell' action.",
        "entry": "The price at which the trade will be entered.",
        "exit": "The price at which the trade will be exited.",
        "entry_time": "The date and time at which the trade will be entered.",
        "exit_time": "The date and time at which the trade will be exited.",
        "quantity": "The number of shares or contracts involved in the trade.",
        "risk": "The amount of capital at risk for this trade.",
        "max_loss": "The maximum acceptable loss for this trade.",
        "max_profit": "The maximum desired profit for this trade.",
        "risk_reward": "The risk-reward ratio for this trade."
    }

    return StrategyDescription(**strategy_description)







