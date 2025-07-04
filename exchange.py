import ccxt
import os
from dotenv import load_dotenv

load_dotenv()

def connect_indodax():
    exchange = ccxt.indodax({
        'apiKey': os.getenv('INDODAX_API_KEY'),
        'secret': os.getenv('INDODAX_SECRET_KEY'),
        'enableRateLimit': True,
    })
    return exchange
