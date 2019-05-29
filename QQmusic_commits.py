import requests
# 引用requests模块
url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'

commentid = 'song_102065756_1152921504900584113_1559050971'

for i in range(5):
    params = {
    'g_tk': '654470638',
    'loginUin': '0',
    'hostUin': '0',
    'format': 'json',
    'inCharset': 'utf8',
    'outCharset': 'GB2312',
    'notice': '0',
    'platform': 'yqq.json',
    'needNewCode': '0',
    'cid': '205360772',
    'reqtype': '2',
    'biztype': '1',
    'topid': '102065756',
    'cmd': '8',
    'needmusiccrit': '0',
    'pagenum': str(i),
    'pagesize': '25',
    'lasthotcommentid': commentid,
    'domain': 'qq.com',
    'ct': '24',
    'cv': '10101010'
    }

    res_comment = requests.get(url,params=params)

    json_comment = res_comment.json()

    list_comment = json_comment['comment']['commentlist']

    for comment in list_comment:
        print(comment['rootcommentcontent'])

    commentid = list_comment[24]['commentid']