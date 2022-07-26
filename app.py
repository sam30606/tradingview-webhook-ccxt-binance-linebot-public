from config import line_bot_api
from flask import Flask, request, jsonify, render_template
from tradingviewOrder import tradingview
from linebot.models import MessageEvent, TextMessage, TextSendMessage,FlexSendMessage
from setFlexMessage import orderFlex

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])

def main():
    tradingviewMsg=tradingview(request)
    if tradingviewMsg:
        if (tradingviewMsg['code']=='success'):
            order_response=tradingviewMsg.pop('order_response')

            for items in order_response:
                orderFlexContents=orderFlex(order_response[items])

                flex_message = FlexSendMessage(
                    alt_text='ORDER',
                    contents=orderFlexContents
                    
                )
                line_bot_api.broadcast(flex_message)

        return tradingviewMsg
    

 



if __name__ == "__main__":
    app.run()