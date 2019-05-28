import requests
# 导入requests模块
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

res = requests.get('http://www.xiachufang.com/explore/')
# 获取数据
res = res.text
# 转换为字符串格式
res_food = BeautifulSoup(res,'html.parser')
# 解析数据

foods_all = res_food.find_all('div',class_='info pure-u')
# 查找最小父级标签

foods_list = []
# 创建一个列表存储各中菜品信息

for food_all in foods_all:


    food_name = food_all.find('p',class_='name').text[17:-13]
    # 菜名，使用[17:-13]切掉了多余的信息

    food_url = 'http://www.xiachufang.com/explore/'+ food_all.find('a')['href']
    # 获取URL

    food_Ingred = food_all.find('p',class_='ing ellipsis').text[1:-1]
    # 食材，使用[1:-1]切掉了多余的信息

    food_list = [food_name,food_url,food_Ingred]

    foods_list.append(food_list)
    # 将菜名、URL、食材，封装为列表，添加进foods_list

print(foods_list)
# 打印


