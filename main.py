from exchange import connect_indodax
from defi.read_token import read_token_balance

def start_session():
    print("Initializing bot session...")

    # CEX example
    indodax = connect_indodax()
    saldo = indodax.fetch_balance()
    print("Saldo Indodax:", saldo)

    # DeFi example
    wallet = '0xYourWalletAddressHere'
    usdt_address = '0x55d398326f99059fF775485246999027B3197955'
    usdt_balance = read_token_balance(usdt_address, wallet)
    print(f"Saldo USDT di BSC: {usdt_balance}")

if __name__ == "__main__":
    start_session()
