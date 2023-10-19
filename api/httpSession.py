
import re
from config.config import myconfig as config
import requests
class session():
    def __init__(self) -> None:
        self.session=self._init_session()
        self.setOriginHeader()
        self.setAgent()
        self.setCookies()


    def _init_session(self):
        session = requests.session()

        return session

    def getOriginHeader(self):    
        return  {
            'J-E-C': '%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1697342224152%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22pin%22%3A%22ZxV1aQ9l%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D',
            'X-Rp-Client': 'android_3.0.0',
            'jdgs': '{"b1":"b16693c8-e5b5-425a-bb08-7f6702f1ca12","b2":"3.2.4_0","b3":"2.1","b4":"svUDpKAumjk08GQzIdg8NfW7WdMCIOKvo2KmeWwPvZa2Nlqi4h1BVMNMk3dqJKP5fjzptB8eqchiZ6mHM1fIeYccbwyaOznPfCKHd59N87guA/rZX5XYyV4VZ0TDeq1IDoUmszyGXVlE0+j5MP+icVJ42Cd8tCQo4GPxJ92zT4TPLipoDnk0AKOwOsBnLxo4LBCkRl2ACXkVtzjGAuVywhKiUlDG6dlZoU3QAO/KUN6Ugwl3rCoxrRw/k0bXkNQLRDCB3JarvPUKfnq92iKeyUSNdfutX0pAFoLOemNFf/yK+cU6VPhVmBuy9bF19Hnv6ovnq0XmbUjdLI+wtGWSmJr/pQxLYmi7hVic8e0jX1r25M8J94rDcSzqU+LagR/+g9H0JfE=","b5":"017279f926ba6881c1a7a85808eb5e581e6be036","b7":"1697342443303","b6":"fe36a8b902f1dbdee8575e6a73263660754e4f06"}',
            'Connection': 'keep-alive',
            'X-Referer-Package': 'com.jingdong.app.mall',
            'Charset': 'UTF-8',
            'X-Referer-Page': 'com.jingdong.app.mall.WebActivity',
            'Accept-Encoding': 'br,gzip,deflate',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'api.m.jd.com'
            }
    def getAgentHeader(self):
        return {"User-Agent": config.get("agent")}
    def getCookieHeader(self):
        return {"Cookie": config.get("cookie")}
    
    
    
    def setOriginHeader(self):
        self.session.headers=self.getOriginHeader()
    def setAgent(self):
        self.session.headers.update(self.getAgentHeader())
    def setCookies(self):
         self.session.headers.update(self.getCookieHeader())
       