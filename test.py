import requests
from bs4 import BeautifulSoup
from urllib.request import quote
import random


def kuaidi100():
    danhao = 71611805303617,
    # 通过单号知道是那个获取快递公司
    #url_type = "https: // www.kuaidi100.com / autonumber / autoComNum?resultv2 = 1 & text = 804748228366757669"
    url_type = 'https://www.kuaidi100.com/autonumber/autoComNum'
    params_type = {
        'resultv2': '1',
        'text': str(danhao)
    }
    
    kuai_type = requests.get(url_type, params=params_type)  # 请求url
    k_type = kuai_type.json()
    list_k = k_type["auto"][0]["comCode"]
    #print(list_k)#打印物流公司代号
    a = random.randint(0,9999)
    #获取快递公司物流信息
    url = 'https://www.kuaidi100.com/query'
    params = {
        'type': str(list_k),
        'postid': str(danhao),
        'temp': '0.758836685259'+ str(a),#这个数必须一直变化
        'phone': ''
    }
    headers = {  # 修改请求头
        'referer': 'https://www.kuaidi100.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Cookie': 'csrftoken=YXfXnwnYYINLRCT2WhuSvqirzsBoj65CjTdd9VHzH6w; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1559216556,1559216913,1559217298,1559217310; WWWID=F01638A90C219FA3F3A78253DA03E527; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1559217348'
        


    }
    kuaidi100 = requests.get(url,params = params ,headers=headers) #请求url
    kuaidi = kuaidi100.json()
    m = kuaidi100.status_code
    if m == 200:
        print("网络请求成功！")
    else:
        print("网络连接失败\n错误码:%d" %m)
    list_kuaidi =kuaidi["data"]
    print("快递单号：%s" %str(danhao))
    if list_kuaidi:
        print("时间                | 物流信息:")
    else:
        print("没有查到物流信息，请填写正确的运单号！")
    for str2 in list_kuaidi:
        wiliu = str2["context"]
        time = str2["time"]
        print(time+" |",wiliu)
        
   
kuaidi100()