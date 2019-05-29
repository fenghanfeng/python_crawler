import requests
from bs4 import BeautifulSoup

movies_list = []

for i in range(10):
    URL = 'https://movie.douban.com/top250?start='+ str(i*25) + '&filter='
    res = requests.get(URL)
    # print(res.status_code)

    movie_html = BeautifulSoup(res.text,'html.parser')

    movies_info = movie_html.find_all('div',class_='item')
    
    

    for movie in movies_info:
        movie_num = movie.find('div',class_='pic').text[1:-5]
        movie_name = movie.find('span',class_='title').text
        movie_score = movie.find('span',class_='rating_num').text
        movie_recommend = movie.find('span',class_='inq').text[1:-1]
        movie_url = movie.find('a')['href']
        
        movies_list.append([movie_num,movie_name,movie_score,movie_recommend,movie_url])

print(movies_list)