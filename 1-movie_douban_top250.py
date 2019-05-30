import requests,openpyxl
from bs4 import BeautifulSoup

movies_list = []

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'new title'
sheet['A1'] = '电影序号'
sheet['B1'] ='电影名'
sheet['C1'] ='电影评分'
sheet['D1'] ='电影简介'
sheet['E1'] ='下载链接'


for i in range(10):
    URL = 'https://movie.douban.com/top250?start='+ str(i*25) + '&filter='
    res = requests.get(URL)
    # print(res.status_code)

    movie_html = BeautifulSoup(res.text,'html.parser')

    movies_info = movie_html.find_all('div',class_='item')
    
    

    for movie in movies_info:
        movie_num = movie.find('em').text
        movie_name = movie.find('span',class_='title').text
        movie_score = movie.find('span',class_='rating_num').text
        movie_recommend = movie.find('span',class_='inq').text[1:-1]
        movie_url = movie.find('a')['href']
        

        sheet.append([movie_num,movie_name,movie_score,movie_recommend,movie_url])

wb.save('movies.xlsx')