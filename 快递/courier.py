import requests,random
# 导入requests模块与random模块

def kuaidi100():

    number = input('请输入您的快递单号：')
    # input函数定义变量快递单号

    url = 'https://www.kuaidi100.com/autonumber/autoComNum'

    params = {
    # 定义请求参数
        'resultv2': '1',
        'text': number
    }

    res = requests.get(url,params=params)
    # 发起请求
    res_json = res.json()
    # 使用json()方法，将response对象，转为列表/字典

    company = res_json["auto"][0]["comCode"]
    # 获取物流公司代号

    print(company)
    a = random.randint(0,9999)
    params_number = {
        'type': str(company),
        'postid': str(number),
        'temp': '0.758836685259'+str(a),
        'phone': ''
    }
    headers = {  # 修改请求头
        'referer': 'https://www.kuaidi100.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '\
                'Chrome/74.0.3729.157 Safari/537.36',
        'Cookie': 'csrftoken=bnX05Pknxkt-eElVyJ8VafgZ0uYRkYbZEMIQ-7ucQZs; WWWID=WWW97F4EBF02B5FCE1E77DC5B130401C801; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1558876782,1558877068,1558877077,1558879531; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1558879531'
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
