import MetaTrader5 as mt5

from init_client import initialize_client

initialize_client()

account_info = mt5.account_info()
if account_info is not None:
    # display trading account data 'as is'
    print(account_info)
else:
    print("Failed to get account information")

mt5.shutdown()
quit()