import json
import urllib.parse
import urllib.request

class wechat():
    def __init__(self, _url):
        self.url = _url

    def sendMsg(self, _msg, _debugMode=False):
       data = { 'data': f"{_msg}" }
       data = json.dumps(data)
       data = str(data)
       data = data.encode('utf-8')
       if _debugMode == True:
           print(f"WEVHAT MSG: {data}")
       else:
           req =  urllib.request.Request(self.url, data=data)
           req.add_header('Content-Type', 'application/json')
           resp = urllib.request.urlopen(req, timeout=300)
