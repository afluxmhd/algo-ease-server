from pydantic import BaseModel

class Strategy(BaseModel):
    strategy: str

    
class StrategyModel(BaseModel):
    scrip: str
    action: str
    entry: float
    exit: float
    entry_time: str
    exit_time: str
    quantity: int
    risk: float
    max_loss: float
    max_profit: float
    risk_reward: float
    description:str


class StrategyDescription(BaseModel):
    scrip: str
    action: str
    entry: str
    exit: str
    entry_time: str
    exit_time: str
    quantity: str
    risk: str
    max_loss: str
    max_profit: str
    risk_reward: str

