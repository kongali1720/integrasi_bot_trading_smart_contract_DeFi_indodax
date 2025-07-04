from web3 import Web3

def connect_bsc():
    w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
    if w3.isConnected():
        print("Terhubung ke BSC")
    else:
        print("Gagal terhubung ke BSC")
    return w3
