from fastapi import APIRouter, HTTPException
from random import uniform
from datetime import datetime
from .models import Strategy, StrategyModel,StrategyDescription
from .gemini.gemini import Gemini
from .data_extraction import DataClean
from .strategy_config import history,instruction
import json



router = APIRouter()

@router.post("/strategy/interpret", response_model=StrategyModel,include_in_schema=False)
async def submit_strategy(strategy: Strategy):

    # insufficient data
    if len(strategy.strategy) < 20 :
        raise HTTPException(status_code=404, detail="Insufficient prompt. Please provide a prompt with at least 25 characters")
    
                 
    # Instance of gemini class
    gemini = Gemini()
    response = gemini.send_prompt(strategy.strategy,history=history,instruction=instruction)
    data_clean  = DataClean()
    pure_res = data_clean.remove_noise(string=response)
    res_dict = {key: value for key, value in json.loads(pure_res).items()}
    processed_strategy_data = {
        "scrip": res_dict.get("scrip", ""),
        "action": res_dict.get("action", ""),
        "entry": -1 if res_dict["entry"]=="" else float(res_dict["entry"]),
        "exit": -1 if res_dict["exit"]=="" else float(res_dict["exit"]),
        "entry_time": res_dict.get("entry_time", ""),
        "exit_time": res_dict.get("exit_time", ""),
        "quantity": 1 if res_dict["quantity"]=="" else int(res_dict["quantity"]),
        "risk": -1 if res_dict["risk"]=="" else float(res_dict["risk"]),
        "max_loss": -1 if res_dict["max_loss"]=="" else float(res_dict["max_loss"]),
        "max_profit": -1 if res_dict["max_profit"]=="" else float(res_dict["max_profit"]),
        "risk_reward": -1 if res_dict["risk_reward"]=="" else float(res_dict["risk_reward"])
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







