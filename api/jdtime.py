import time
from datetime import datetime, timedelta
import requests
def jd_time():
    """
    从京东服务器获取时间戳
    """
    url = 'https://api.m.jd.com'
    resp = requests.get(url, verify=False)
    jd_timestamp = int(resp.headers.get('X-API-Request-Id')[-13:])
    print("jd_timestamp",jd_timestamp)
    return jd_timestamp

def local_time():
    """
    获取本地时间戳
    """
    local_timestamp = round(time.time() * 1000)
    print("local_timestamp",local_timestamp)

    return local_timestamp

def local_jd_time_diff():
    """
    计算本地与京东服务器时间差
    """
    return local_time() - jd_time()

# ttt=local_jd_time_diff()
# print(ttt)
