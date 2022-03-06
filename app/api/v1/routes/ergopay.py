import requests 
import json
import typing as t

from starlette.responses import JSONResponse
from fastapi import APIRouter, status, Path, Request
from pydantic import BaseModel
from time import time
from datetime import datetime
from datetime import datetime
from config import Config, Network # api specific config
from wallet import Wallet

CFG = Config[Network]

ergopay_router = r = APIRouter()

#region BLOCKHEADER
"""
Ergopay API
---------
Created: vikingphoenixconsulting@gmail.com
On: 20220218
Purpose: Allow mobile ergo dApp payments
"""
#endregion BLOCKHEADER

#region INIT
DEBUG = True # CFG.debug
st = time() # stopwatch

headers = {
    "api_key": CFG.ergopadApiKey,
    "Content-Type": "application/json"
}

# con = psycopg.create_engine(CFG.connectionString)
#endregion INIT

#region LOGGING
import logging
level = (logging.WARN, logging.DEBUG)[DEBUG]
logging.basicConfig(format='{asctime}:{name:>8s}:{levelname:<8s}::{message}', style='{', level=level)

import inspect
myself = lambda: inspect.stack()[1][3]
#endregion LOGGING

class ErgoPayResponse:
    def __init__(self, address):
        self.address = address

    message: str = '',
    messageSeverity: str = 'NONE', # NONE, INFORMATION, WARNING, ERROR
    reducedTx: str = '',
    replyTo: str = '',

#region ROUTES
# stake??

# vest??

# purchase??
@r.get("/purchase/{sessionId}/{address}", name="ergopay:ergopay")
def ergopay(sessionId:str, address:str=''):
    ergopayResponse = ErgoPayResponse(address)
    ergopayResponse.replyTo = 'ergopad'
    ergopayResponse.message = sessionId
    ergopayResponse.messageSeverity = 'NONE'

    # get session info
    ergs = .1

    # find transaction from ergopay
    try:
        tx = { 
            "requests": [ 
                { 
                    "address": address, 
                    "value": int((ergs)*(10**9)),
                }
            ], 
            "inputs": [], 
            "dataInputs": [], 
            "fee": 10**6 
        }
        logging.debug(CFG.apiKey)
        logging.debug(json.dumps(tx))
        out = requests.post('http://52.12.102.149:9053/wallet/transaction/generateUnsigned', headers=headers, json=tx).json()
        logging.debug(out)
        box = requests.get('http://52.12.102.149:9053/wallet/boxes/unspent?minConfirmations=-1&minInclusionHeight=0', headers=headers).json()
        logging.debug(box)
        creationHeight = requests.get('http://52.12.102.149:9053/info', headers=headers).json()['headersHeight']
        logging.debug(creationHeight)

        inputs = []
        for b in box:
            logging.debug(b)
            i = b['box']
            i['extension'] = {}
            inputs.append(i)
        
        outputs = []
        for o in out['outputs']:
            o = {
                'value': o['value'],
                'ergoTree': o['ergoTree'],
                'assets': o['assets'],
                'additionalRegisters': o['additionalRegisters'],
                'creationHeight': creationHeight,
            }
            outputs.append(o)
        
        utx = {
            'inputs': inputs,
            'outputs': outputs,
            'dataInputs': out['dataInputs']
        }
        ergopayResponse.reducedTx = utx

        return ergopayResponse.__dict__    

    except:
        res = ErgoPayResponse(None)
        res.message = 'invalid'
        res.messageSeverity = 'ERROR'

        return ergopayResponse.__dict__

@r.get("/hello/{address}", name="ergopay:ergopay")
async def hello(address):
    hi = ErgoPayResponse(address)
    hi.message = 'hello world'

    return hi.__dict__
