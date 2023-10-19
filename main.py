import json
from time import sleep
from api import jdtime
from api.mobileApi import JDAPi
from loguru import logger
from apscheduler.schedulers.blocking import BlockingScheduler
import time
from api.jdtime import local_jd_time_diff
import datetime
logger.add('./log/main_{time}.log',rotation="00:00",encoding='utf-8')
def getOrderUrl():
    url,token=jdApi.getToken()
    divideUrl=jdApi.getdivideUrlbyUNJump(url,token)
    if divideUrl==None:
        return None
    captchaUrl=jdApi.getCaptchaUrlbyDivide(divideUrl)
    if captchaUrl==None:
        return None
    skillUrl=jdApi.getSkillActionUrlbyCaptcha(captchaUrl)
    if divideUrl==None:
        return None
    return skillUrl
    

    # divideUrl=jdApi.getSkillUrl(url,token)
def loopSkill():
    timediff=local_jd_time_diff()
    sleepTime=1
    while 1:
        local_timestamp = round(time.time() * 1000)
        jdServerTime=local_timestamp-timediff
        # time_struct = time.gmtime(jdServerTime)
        dt = datetime.datetime.fromtimestamp(jdServerTime/1000)
        dtStr=dt.strftime("%Y-%m-%d %H:%M:%S.%f")
        h=dt.hour
        m=dt.minute
        s=dt.second
        sleep(sleepTime)
        # time_struct.
        if sleepTime==1:
            logger.info(f"当前时间:{dtStr}")
        #平时一秒执行一次
        #59的时候1毫秒执行1次
        if h>=11 and m>=59 and s>59:
            sleepTime=0.01
        if h>=12:
            break
    logger.info("当前时间，开始抢购...")
    retryTime=0
    retryMaxTime=200
    skillUrl=""
    
    while 1:
        skillUrl=getOrderUrl()
        if skillUrl=="https://marathon.jd.com/mobile/koFail.html" or skillUrl==None:
            retryTime=retryTime+1
            sleep(0.1)
            logger.info(f"获取抢购链接失败！，重试中,第{retryTime}次...")
            if retryTime>retryMaxTime:
                logger.info(f"抢购失败，重试次数{retryMaxTime}")
                break
        else:
            logger.info(f"获取抢购链接成功，链接地址:{skillUrl}")
            break
    if skillUrl=="":
        return "获取抢购链接失败，抢购结束"
    
    jdApi.doSkillAction(skillUrl)
    
    retryTime=0
    
    now=datetime.datetime.now()
    minute=now.minute
    while  1:
        result=jdApi.doOrderSumit()
        logger.info(result)
        try:
            resultCode=result["resultCode"]
            if resultCode==0:
                logger.info("抢购成功，请及时付款")
                break
            sleep(0.1)
            retryTime=retryTime+1
            logger.info(f"抢购失败，第次{retryTime}重试")
            if minute>=2:
                logger.info(f"抢购失败，重试次数{retryTime}")

                break
        except Exception as e:
            ee=str(e)[0:100]
            logger.info(f"抢购失败:{ee}")


def appoint():
    isAppoint=jdApi.isAppoint()
    logger.info(f"查询预约状态{isAppoint}")
   
    if isAppoint==False or isAppoint==None:
        r=jdApi.doAppoint()
        logger.info(f"预约结果{r}")
    
if __name__ == '__main__':
    jdApi=JDAPi()
    logger.info("程序启动完成")
    scheduler = BlockingScheduler()
    scheduler.add_job(appoint, 'cron',hour=11,minute=32,second=10)
    logger.info("预约任务创建完成")
    scheduler.add_job(loopSkill, 'cron',hour=11,minute=58,second=30)
    logger.info("抢购任务创建完成")
    # loopSkill()

    scheduler.start()
    # appoint()
    # loopSkill()
    # getOrderUrl()
    