import dotenv as d

import os
import MetaTrader5 as mt5

config = d.Dotenv(".env")

def initialize_client():

    if not mt5.initialize(
        # replace with path to terminal.exe
        path=config.get("PATH_TO_TERMINAL_EXECUTABLE")
    ):
        print("initialize() failed", mt5.last_error())
        quit()

    if not mt5.login(
        login=config.get("LOGIN"),
        password=config.get("PASSWORD"),
        server=config.get("SERVER")
    ):
        print("failed to authorize")
        quit()