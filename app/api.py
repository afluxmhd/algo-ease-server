from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def check_server():
    response = { "Status" : "AlgoEase Server is runningg.." }
    return response