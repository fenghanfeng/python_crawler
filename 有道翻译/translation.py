import requests
import hashlib
import time
import json
import random
# 导入模块

class Youdao(object):
    def __init__(self, msg):
        self.msg = msg
        # 传递进的需要翻译的内容
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        # 请求URL
        self.D = "@6f#X3=cCuncYssPsuRUE"
        # 需要加密字符串
        self.salt = self.get_salt()
        # 根据时间戳获取salt参数
        self.sign = self.get_sign()
        # 使用md5函数和其他参数，得到sign参数

    def get_md(self, value):
        '''md5加密'''
        m = hashlib.md5()
        # m.update(value)
        m.update(value.encode('utf-8'))
        return m.hexdigest()

    def get_salt(self):
        '''根据当前时间戳获取salt参数'''
        s = int(time.time() * 1000) + random.randint(0, 10)
        return str(s)

    def get_sign(self):
        '''使用md5函数和其他参数，得到sign参数'''
        s = "fanyideskweb" + self.msg + self.salt + self.D
        return self.get_md(s)

    def get_result(self):
        '''headers里面有一些参数是必须的，注释掉的可以不用带上'''
        headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=2056745280@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=1712718501.0168397; P_INFO=fhf_cn@163.com|1556795932|0|other|00&99|jix&1556754235&other#jix&360400#10#0#0|&0||fhf_cn@163.com; JSESSIONID=aaa5qD7zNnijO9xPMPvSw; ___rl__test__cookies=1559436364295',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }
        data = {
            'i': self.msg,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CL1CKBUTTON',
            'typoResult': 'true'
        }
        # 发起请求，获取对应的json数据
        html = requests.post(self.url, data=data, headers=headers)
        # 将获取的json数据转化为字典的格式
        infos = html.json()

        # 使用if语句进行条件判断，当不存在翻译内容时进行异常判断
        if 'translateResult' in infos:
            # try...except...语句异常处理
            try:
                result = infos['translateResult'][0][0]['tgt']
                print(result)
            except:
                pass

# 控制当前文件的调用方法，当作为脚本运行时条件为真，执行下面语句
if __name__ == '__main__':
    y = Youdao(input('请输入您想翻译的内容：'))
    y.get_result()