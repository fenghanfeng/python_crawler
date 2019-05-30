import requests,csv
# 引用requests模块
from bs4 import BeautifulSoup
with open('movies_2.csv','a',newline='',encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['电影序号','电影名','电影评分','电影简介','下载链接'])
        for x in range(10):
                url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
                res = requests.get(url)
                bs = BeautifulSoup(res.text, 'html.parser')
                tag_num = bs.find_all('div', class_="item")
                # 查找包含序号，电影名，链接的<div>标签
                tag_comment = bs.find_all('div', class_='star')
                # 查找包含评分的<div>标签
                tag_word = bs.find_all('span', class_='inq')
                # 查找推荐语
                list_all = []
                for x in range(len(tag_num)):
                        list_movie = [tag_num[x].text[2:5], tag_num[x].find('img')['alt'], tag_comment[x].text[2:5], tag_word[x].text, tag_num[x].find('a')['href']]
                        list_all.append(list_movie)
                        writer.writerow(list_movie)
print(list_all)