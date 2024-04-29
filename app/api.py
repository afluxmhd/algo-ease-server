from fastapi import FastAPI, HTTPException
from app.strategy.routers import router as strategy_router
from app.stocks.routers import router as stocks_router

app = FastAPI()

@app.get("/")
async def check_server():
    response = { "Status" : "AlgoEase Server is runningg.." }
    return response


app.include_router(strategy_router, tags=["NLP"])
app.include_router(stocks_router, tags=["Stocks"])