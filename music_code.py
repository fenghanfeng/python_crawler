import requests,html
# 导入requests与html模块

for i in range(1,6):
# 循环五次，获取前五页的数据
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p='+str(i)+'&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
    # 拼接url
    res = requests.get(url)
    # 调用get方法，获取返回的response对象
    json_music = res.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    # 一层一层地取字典，获取歌单列表
    for music in list_music:
    # list_music是一个列表，music是它里面的元素
        music_id = music['id']
        music_mid = music['mid']

        url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
        # 这是请求歌词的url
        headers = {
            'origin':'https://y.qq.com',
            # 请求来源
            'referer':'https://y.qq.com/n/yqq/song/'+music_mid+'.html',
            # 请求来源，携带的信息比“origin”更丰富
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            # 标记了请求从什么设备，什么浏览器上发出
            }
        params = {
        'nobase64': '1',
        'musicid': str(music_id),
        '-': 'jsonp1',
        'g_tk': '654470638',
        'loginUin': '1719311451',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
        }

        res_music = requests.get(url,headers=headers,params=params)
        # 发起请求

        res_music_json = res_music.json()
        # 使用json()方法，将response对象，转为列表/字典

        content = res_music_json['lyric']
        # 取出字典中的歌词

        print(html.unescape(content))
        # html.unescape()方法就可以输出html中的实体字符
