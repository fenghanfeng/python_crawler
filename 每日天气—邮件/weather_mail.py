import requests
# 导入requests模块，用户发起请求
from bs4 import BeautifulSoup
# 引用bs4模块中的BeautifulSoup方法进行html解析

import smtplib 
# 导入smtplib模块，用户发送邮件
from email.mime.text import MIMEText
from email.header import Header
# 用户构建邮件

import schedule
import time
#引入schedule和time模块

# 获取当天的天气信息
def weather_spider():
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url='http://www.weather.com.cn/weather/101240201.shtml'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    comment = BeautifulSoup(res.text,'html.parser')

    tem = comment.find(class_='tem').text
    wea = comment.find(class_='wea').text
    return tem,wea

# 发送邮件
def send_mail():
    weather = weather_spider()


    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)

    account = input('请输入发送方邮箱地址：')
    password = input('请输入邮箱授权码：')
    qqmail.login(account,password)

    receiver= input('请输入接受方邮件地址：')

    content ='天气测试：' + weather[0] + weather[1]

    message = MIMEText(content, 'plain', 'utf-8')
    subject = '天气测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

# 设置定时任务
schedule.every(2).seconds.do(send_mail)

while True:
    schedule.run_pending()
    time.sleep(1)