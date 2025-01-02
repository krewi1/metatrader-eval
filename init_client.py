import os
import MetaTrader5 as mt5

def initialize_client():

    if not mt5.initialize(
        # replace with path to terminal.exe
        path=os.getenv("PATH_TO_TERMINAL_EXECUTABLE")
    ):
        print("initialize() failed")
        quit()

    if not mt5.login(
        login=os.getenv("LOGIN"),
        password=os.getenv("PASSWORD"),
        server=os.getenv("SERVER")
    ):
        print("failed to authorize")
        quit()