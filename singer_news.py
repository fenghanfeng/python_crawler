import requests
from bs4 import BeautifulSoup
# 导入requests模块以及BeautifulSoup中的bs4模块

singer_name = input('请输入你想查询的歌手名：')
# 定义歌手们作为变量

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

params = {
'ct':'24',
'qqmusic_ver': '1298',
'new_json':'1',
'remoteplace':'sizer.yqq.song_next',
'searchid':'64405487069162918',
't':'0',
'aggr':'1',
'cr':'1',
'catZhida':'1',
'lossless':'0',
'flag_qc':'0',
'p':'1',
'n':'20',
'w':singer_name,
'g_tk':'5381',
'loginUin':'0',
'hostUin':'0',
'format':'json',
'inCharset':'utf8',
'outCharset':'utf-8',
'notice':'0',
'platform':'yqq.json',
'needNewCode':'0'    
}
# 歌手名是作为参数提交的，在参数中修改歌手名可以查询到不同的歌手json数据

headers = {
'origin':'https://y.qq.com',
# 请求来源
'referer':'https://y.qq.com/portal/search.html',
# 请求来源，携带的信息比“origin”更丰富
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
# 标记了请求从什么设备，什么浏览器上发出
}
# 定义请求头

res = requests.get(url,headers=headers,params=params)
# 使用get方法发起请求

res_json = res.json()
# 使用json()方法，将response对象，转为列表/字典

singer_mid = res_json['data']['zhida']['zhida_singer']['singerMID']
# 获取字典中singer_mid的值作为下一次请求的变量

headers_novel = {
'origin':'https://y.qq.com',
# 请求来源
'referer':'https://c.y.qq.com/xhr_proxy_utf8.html',
# 请求来源，携带的信息比“origin”更丰富
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
# 标记了请求从什么设备，什么浏览器上发出
}
# 定义请求头

rs = requests.get('https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_singer_desc.fcg?singermid='+singer_mid+'&utf8=1&outCharset=utf-8&format=xml&r=1559184246524',headers=headers_novel)
#发起请求

rs_html = BeautifulSoup(rs.text,'html.parser')
# 解析html

singer_novle = rs_html.find('desc').text
# 获取desc标签中的歌手信息并转换为字符串

print(singer_novle)
# 打印
    