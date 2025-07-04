from defi.web3_connect import connect_bsc

def read_token_balance(token_address, wallet):
    w3 = connect_bsc()
    erc20_abi = [...]  # masukkan ABI ERC20 minimal balanceOf, decimals

    token_contract = w3.eth.contract(address=token_address, abi=erc20_abi)
    balance = token_contract.functions.balanceOf(wallet).call()
    decimals = token_contract.functions.decimals().call()

    return balance / (10 ** decimals)
