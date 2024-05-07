from fastapi import APIRouter, HTTPException
from random import uniform
from datetime import datetime
from .models import Strategy, StrategyModel,StrategyDescription
from .gemini.gemini import Gemini
from .data_extraction import DataClean
import json



router = APIRouter()

@router.post("/strategy/interpret", response_model=StrategyModel,include_in_schema=False)
async def submit_strategy(strategy: Strategy):

    history = [
      {
        "role": "user",
        "parts": ["I want to buy 200 shares of Tata Motors today at 10:30 AM. My entry price is $150 per share, and I plan to sell them when the price hits $180 per share. I'm willing to risk $15 per share, with a maximum loss capped at $30 per share. I aim to close the position by 3:00 PM.\nPlease generate JSON data for the provided strategy using the following keys:\n\"scrip\": \"Tata Motors\",\n\"action\": \"buy\",\n\"entry\": 150,\n\"exit\": 180,\n\"entry_time\": \"10:30 AM\",\n\"exit_time\": \"3:00 PM\",\n\"quantity\": 200,\n\"risk\": 15,\n\"max_loss\": 30,\n\"max_profit\": 30,\n\"risk_reward\": 2"]
      },
      {
        "role": "model",
        "parts": ["```json\n{\n\"scrip\": \"Tata Motors\",\n\"action\": \"buy\",\n\"entry\": 150,\n\"exit\": 180,\n\"entry_time\": \"10:30 AM\",\n\"exit_time\": \"3:00 PM\",\n\"quantity\": 200,\n\"risk\": 15,\n\"max_loss\": 30,\n\"max_profit\": 30,\n\"risk_reward\": 2\n}\n```"]
      },
    ]
    
    instruction = "\nGenerate JSON for the provided strategy using the following keys:\n"\
                 "scrip, action, entry, exit, entry_time, exit_time, quantity, risk, max_loss, max_profit, risk_reward"\
                 " If parameter values are not available, assign empty strings.,the risk parameter should be percentage float value"
                 
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
        "quantity": -1 if res_dict["quantity"]=="" else int(res_dict["quantity"]),
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







