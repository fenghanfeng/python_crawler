import requests
from bs4 import BeautifulSoup
from urllib.request import quote

movie_name = input('请输入你想要观看的电影名：')

movie_code = quote(movie_name.encode('gbk'))

url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+movie_code

res = requests.get(url)

movie_html = BeautifulSoup(res.text,'html.parser')

down_code = movie_html.find('div',class_='co_content8')

down_code_url = 'https://www.ygdy8.com' + down_code.find('a')['href']

rs = requests.get(down_code_url)

down_html = BeautifulSoup(rs.text,'html.parser')

down_code_novel = down_html.find('tbody')

down_url = down_code_novel.find('a')['href']

print(movie_name + '的下载地址为：' + down_url )


