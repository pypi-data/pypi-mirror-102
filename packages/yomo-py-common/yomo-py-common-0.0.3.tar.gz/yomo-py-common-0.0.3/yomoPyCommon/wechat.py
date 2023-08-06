import json
import urllib.parse
import urllib.request

class wechat():
    def __init_(self):
        pass

    def sendMsg(self, _msg, _debugMode=False):
       data = { 'data': f"{_msg}" }
       data = json.dumps(data)
       data = str(data)
       data = data.encode('utf-8')
       if _debugMode == True:
           print(f"WEVHAT MSG: {data}")
       else:
           req =  urllib.request.Request('http://192.168.1.152:3000/group/cryptonewstest', data=data)
           req.add_header('Content-Type', 'application/json')
           resp = urllib.request.urlopen(req, timeout=300)

if __name__ == "__main__":
    __wechat = wechat()
    __wechat.sendMsg("This is the test message")
