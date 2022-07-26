import json, config
from flask import Flask, request, jsonify, render_template
from ccxtAPI import order,usdtBalance,positions,setLever


def tradingview(request):
    order_response={}
    data = json.loads(request.data)

    if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
        return {
            "code": "error",
            "message": "Nice try, invalid passphrase"
        }

    symbol=data['ticker'][0:-8]+"/USDT"
    side = data['strategy']['order_action']
    price=data['strategy']['order_price']
    lever=data['strategy']['lever']

    if(positions(symbol)['entryPrice']):
        position=positions(symbol)
        existSide='buy' if(position['side'])=='long' else 'sell'
        if(existSide!=side):
            amount=position['contracts']
            order_response['exit']=order(symbol, side ,amount, price)
            order_response['exit']['ordertype']='exit'

    setLever(lever,symbol)
    amount =usdtBalance()/price*lever

    order_response['order'] = order(symbol, side ,amount, price)
    order_response['order']['ordertype'] ='order'

    if order_response:
        return {
            "code": "success",
            "message": "order executed",
            "order_response":order_response
        }
    else:
        print("order failed")

        return {
            "code": "error",
            "message": "order failed"
        }