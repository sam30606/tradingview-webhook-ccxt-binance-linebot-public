def orderFlex(dist):
    flexContents={
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "ORDER",
        "weight": "bold",
        "color": "#1DB446",
        "size": "sm"
      },
      {
        "type": "text",
        "text": str(dist['symbol']),
        "weight": "bold",
        "size": "xxl",
        "margin": "md"
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "spacing": "sm",
        "contents": [
        {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "下單類型",
            "size": "md",
            "color": "#555555"
          },
          {
            "type": "text",
            "text": str(dist['ordertype']),
            "size": "md",
            "color": "#111111",
            "align": "end"
          }
        ]
        },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "方向",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": str(dist['side']),
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "下單數量",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": str(dist['amount']),
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "價格",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": str(dist['price']),
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          }
        ]
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "md",
        "contents": [
          {
            "type": "text",
            "text": "時間",
            "size": "xs",
            "color": "#aaaaaa",
            "flex": 0
          },
          {
            "type": "text",
            "text": str(dist['datetime']),
            "color": "#aaaaaa",
            "size": "xs",
            "align": "end"
          }
        ]
      }
    ]
  }
}

    return flexContents
