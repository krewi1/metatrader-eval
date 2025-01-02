import MetaTrader5 as mt5
from fastapi import FastAPI

from init_client import initialize_client

app = FastAPI()

initialize_client();

@app.get("/balance")
async def root():
    account_info = mt5.account_info()
    return {"balance": account_info.balance}