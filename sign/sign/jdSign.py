from random import randint
import time
import uuid
from sign.sign.TenMagic16 import TenMagic16
from sign.sign.TenMagic32 import TenMagic32
from sign.sign.TenSeattos import TenSeattos

from sign.sign.Utils import *

def encrypt(data, data_len, encryptId, offset):
    encryptType = [0, 1, 2][offset:] + [0, 1, 2][0:offset]
    encrypt = encryptType[encryptId]
    switcher = {
        0: TenMagic32,
        1: TenMagic16,
        2: TenSeattos
    }
    
    return switcher[encrypt](data, data_len)

def getSignTest(functionId, body, uuid, client, clientVersion):  
    st = "1696996798818"
    # encryptId = randint(0, 2)
    # offset = randint(0, 2)
    encryptId=0
    offset=0
    sv = "1" + str(offset) + str(encryptId)
    data = "&".join(("functionId="+functionId, "body="+body, "uuid="+uuid,"client="+client, "clientVersion="+clientVersion, "st="+st, "sv="+sv))
    sign = hash(encrypt(data, len(data), encryptId, offset))
    print("st=" + st + "&sign=" + sign + "&sv=" + sv)
    return sign

def getSign(functionId, body, uuid, client, clientVersion):  
    t = time.time()
    st = str(int(round(t * 1000)))
    encryptId = randint(0, 2)
    offset = randint(0, 2)
    sv = "1" + str(offset) + str(encryptId)
    data = "&".join(("functionId="+functionId, "body="+body, "uuid="+uuid, "client="+client, "clientVersion="+clientVersion, "st="+st, "sv="+sv))
    sign = hash(encrypt(data, len(data), encryptId, offset))
    print("st=" + st + "&sign=" + sign + "&sv=" + sv)
    return sign

def getSignWithstv(functionId, body, uuid, client, clientVersion):  
    t = time.time()
    st = str(int(round(t * 1000)))
    encryptId = randint(0, 2)
    offset = randint(0, 2)
    sv = "1" + str(offset) + str(encryptId)
    data = "&".join(("functionId="+functionId, "body="+body, "uuid="+uuid, "client="+client, "clientVersion="+clientVersion, "st="+st, "sv="+sv))
    sign = hash(encrypt(data, len(data), encryptId, offset))
    print("st=" + st + "&sign=" + sign + "&sv=" + sv)
    return "st=" + st + "&sign=" + sign + "&sv=" + sv
#test

def main():
    functionId = "genToken"
    clientVersion = "12.1.6"
    client = "android"
    uuid = '换成你的uuid'
    body = '{"action":"to","to":"https%3A%2F%2Fdivide.jd.com%2Fuser_routing%3FskuId%3D100012043978%26from%3Dapp"}'
    #070353ead481921bf1e5668fb0821134
    #st=1696996798818
    #sv=100
    getSignTest(functionId, body, uuid, client, clientVersion)
if __name__ == "__main__":
    main()
