from random import uniform
from fastapi import  HTTPException
class StockSimulation :
    def stock_price(self,status:str ,entry: float=0.0, exit: float=0.0, action : str=""):
        print(status,entry,exit,action,1)
        # case 1: It has no entry and no exit price.
        if entry <=0 and exit<=0 :
            return  round(uniform(400, 500), 2)
        
        # case 2: It has only an entry price.
        if action == "buy" and entry>=0 and exit<=0:
            if status == "open":
                return entry-(entry*.01)
            else:
                return round(uniform(entry, entry+(entry*.1)),2)
            
        if action == "sell" and entry>=0 and exit<=0:
            if status == "open":
                return entry+(entry*.01)
            else:
                return round(uniform(entry+(entry*.1), entry),2)    
            
        # case 3: It has only an exit price.
        if entry<=0 and exit>=0:
            raise HTTPException(status_code=400, detail="Entry price is required!")
            
        
        
        # case 4: It has both an entry and an exit price.    
        if entry >=0 and exit>=0 :
            if action == "buy" :
                if status == "open":
                    return round(uniform(entry-(entry*.1), exit+(exit*.1)),2)
                else:
                    return round(uniform(entry, exit+(exit*.1)),2)
            
            if action == "sell" :
                if status == "open":
                    return round(uniform(entry, exit-(exit*.1)),2)
                else:
                    return round(uniform(entry, exit-(exit*.1)),2)
                
        return -1        
                
                
                
                
