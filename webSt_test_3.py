import websocket
import json

def webSt_Connect_Disconnect():
    
    # server url where websocket should connect
    ws_url = "ws://192.168.00.000:PORT/api"

    # data what send to server 
    request_data = [
        {
            "request": "authorize",
            "key": "0000" # need to add key
        },
        {
            "request": "get-devices",
            "id": "2",
            "type": ["remote-control", "valve-heating", "fancoil"],
            "status": "detailed",
            "area-as-array": True
        }
    ]

    # connect via webscoket
    ws = websocket.WebSocket()
    ws.connnect(ws_url)

    # counter of request_data 
    for i in range(10):
        ws.send(json.dumps(request_data)) 

        # uncomment to see what data is send like debug
        print(i, request_data)

    # disconnect from server
    ws.close()

webSt_Connect_Disconnect()


# Test result->
#
# 1 case: counter is -> 10 
# server looks ok
#
# 
# Some notice:
# json tested in test_J.py -> all tests ok
# 
# add -try- method
