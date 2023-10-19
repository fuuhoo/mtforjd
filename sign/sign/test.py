from email import header
import requests
from urllib.parse import urlencode
import time
from jdSign import getSignWithstv
base_url = "https://api.m.jd.com/client.action?"

t = time.time()
st = str(int(round(t * 1000)))


ep={"hdid":"JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw=","ts":st,"ridx":-1,"cipher":{"area":"CJDpCJOnCv80DtY2DV80DtY5EK==","d_model":"UwVubWvBCtLGcw8=","wifiBssid":"CNUzDzY2ZNc0YzCzCzGyCWO0DwVvCQU4YzvtCtPvCNY=","osVersion":"CJO=","d_brand":"WQvrb21f","screen":"CtS5DsenCNqm","uuid":"DJczEWU2DwPuDwDwYJOyDG==","aid":"DJczEWU2DwPuDwDwYJOyDG==","openudid":"DJczEWU2DwPuDwDwYJOyDG=="},"ciphertype":5,"version":"1.2.0","appname":"com.jingdong.app.mall"}

QueryString = {
    "functionId" : "genToken",
    "clientVersion" : "12.1.6",
    "client" : "android",
    "eid" : "eidA3e84812360sacXOyFYL7RzSoHKB6uKa4iHFzs4POXUYzjOnVvYofGycBrOdsifIwt1UwAVkAunyz709VQTMOypkJdxy6bvkxcIW0AL\/SAB56\/RdZ",
    "ef" : "1",
    "ep" :ep
}

uuid = "5739e66ad6cfa125"

headers = {
  'Cookie': 'wskey=AAJlI13fAED3bo2St9L3k7BtSWiOSmNW5GfFKKzCeCp_7CuVjWy-jmu70HjUVm_vf6NTe_M7NJUJ6cIlRV4QrLwvm7ysUZKF;whwswswws=JD012145b9dZY1rTRef5169699667634902jEiAj2LtRxRCNo4U_8O5WmfjEcI5F3Byg-7LI263gNkavW6r9dxbqwVA8XTLtcbjRTqO-MaBeZixii_WrRbrQQ1vvy3np~AAkNI4hyLEAAAAAAAAAAAAAAAAFc55mrWz6ElfwAAAAZmdXVob28;unionwsws={"devicefinger":"eidA3e84812360sacXOyFYL7RzSoHKB6uKa4iHFzs4POXUYzjOnVvYofGycBrOdsifIwt1UwAVkAunyz709VQTMOypkJdxy6bvkxcIW0AL\\/SAB56\\/RdZ","jmafinger":"JD012145b9dZY1rTRef5169699667634902jEiAj2LtRxRCNo4U_8O5WmfjEcI5F3Byg-7LI263gNkavW6r9dxbqwVA8XTLtcbjRTqO-MaBeZixii_WrRbrQQ1vvy3np~AAkNI4hyLEAAAAAAAAAAAAAAAAFc55mrWz6ElfwAAAAZmdXVob28"};pin_hash=-1263152894;',
  'Connection': 'keep-alive',
  'User-Agent': 'okhttp/3.12.16;jdmall;android;version/12.1.6;build/98973;',
  'X-Referer-Package': 'com.jingdong.app.mall',
  'Charset': 'UTF-8',
  'X-Referer-Page': 'com.jingdong.app.mall.WebActivity',
  'Accept-Encoding': 'br,gzip,deflate',
  'Cache-Control': 'no-cache',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Host': 'api.m.jd.com',
}



post_data = {
    "body" : '{"action":"to","to":"https%3A%2F%2Fdivide.jd.com%2Fuser_routing%3FskuId%3D100012043978%26from%3Dapp"}&'
}
def parse_url(inData : dict):
    return base_url + urlencode(inData) + "&" +  getSignWithstv(inData["functionId"], post_data["body"], uuid, inData["client"], inData["clientVersion"])

url = parse_url(QueryString)
r = requests.post(url, data = post_data,headers=headers)
print(r.text)


