from pydantic import BaseModel

class Strategy(BaseModel):
    strategy: str

    
class StrategyModel(BaseModel):
    scrip: str
    action: str
    entry: float
    exit: float
    entry_time: int
    exit_time: int
    quantity: int
    risk: float
    max_loss: float
    max_profit: float
    risk_reward: float


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

