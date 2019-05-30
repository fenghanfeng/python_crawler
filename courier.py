import requests,random
# 导入requests模块与random模块
headers = {
# 定义请求头
    'Cookie':'TOKEN=5S3yKGakkhzGcBM6vZx8QdTMmLPeHqK7o2uSExpABLg; loginId=198567505; loginType=SELLER; loginName=18707024734; nickname=18707024734; loginEmail=null; loginMobile=18707024734; loginExt=null; auth=1; loginSession=1; WWWID=WWW3037F65A7E13669251391567BF530CC7; sortStatus=0; KDTIME=15613AE41D8453411EBC15DCABDA1E4D; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1559217298,1559217310,1559218107,1559218963; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1559218963',
    'Origin': 'https://www.kuaidi100.com',
    'Referer': 'https://www.kuaidi100.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

number = input('请输入您的快递单号：')
# input函数定义变量快递单号

def kuaidi100():

    url = 'https://www.kuaidi100.com/autonumber/autoComNum'

    params = {
    # 定义请求参数
        'resultv2': '1',
        'text': 'number'
    }

    res = requests.get(url,headers=headers,params=params)
    # 发起请求
    res_json = res.json()
    # 使用json()方法，将response对象，转为列表/字典

    company = res_json["auto"][0]["comCode"]
    # 获取物流公司代号

    print(company)

    params_number = {
        'type': company,
        'postid': str(number),
        'temp': '0.893963717657'+str(random.randint(1000,9999)),
        'phone': None
    }

    url_rs = 'https://www.kuaidi100.com/query'

    rs = requests.get(url_rs,headers=headers,params=params_number)

    rs_json = rs.json()

    m = rs.status_code

    if m == 200:
        print("网络请求成功！")
    else:
        print("网络连接失败\n错误码:%d" %m)

    content = rs_json["data"]


    print("快递单号：%s" %str(number))
    if content:
        print("时间 | 物流信息:")
    else:
        print("没有查到物流信息，请填写正确的运单号！")
    for str2 in content:
        road = str2["context"]
        time = str2["time"]
        print(time+" |",road)


kuaidi100()
