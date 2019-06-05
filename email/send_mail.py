import smtplib
# 导入smtplib模块，发送邮件
from email.mime.text import MIMEText
# 从email包下的text文件中引入MIMEText方法，内容形式为纯文本、html页面
from email.mime.image import MIMEImage
# 内容形式为图片
from email.mime.multipart import MIMEMultipart
# 多形式组合，可包含文本和附件
from email.header import Header
# 用于构建邮件头
import csv
# 引用csv模块，用于读取邮箱信息

# from_addr = '1719311451@qq.com'
# password = 'wcpmjskcccncbiff'
# to_addr = 'fhf_cn@163.com'


# 发信方的信息：发信邮箱，QQ邮箱授权码
# 方便起见，你也可以直接赋值
from_addr = input('请输入登陆邮箱地址：')
password = input('请输入邮箱授权码：')

# 发信服务器
smtp_server = 'smtp.qq.com'

# 文本内容
text = '''这是一个测试的邮件
Hello World！
人生苦短...
'''


data = [['fhf','fhf_cn@163.com'],['fhf','1719311451@qq.com']]
# 待写入csv文件的收件人数据：人名+邮箱
# 记得替换成你要发送的名字和邮箱


# 写入收件人数据
with open('to_addr.csv','w',newline='') as f:
    writer = csv.writer(f)
    for r in data:
        writer.writerow(r)

# 读取收件人数据，并启动写信和发信流程
with open('to_addr.csv','r') as f:
    reader = csv.reader(f)
    for r in reader:
        to_addr = r[1]
        
        # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
        msg = MIMEText(text,'plain','utf-8')

        # 邮件头信息
        msg['From'] = Header(from_addr)
        msg['TO'] = Header(','.join(to_addr))
        msg['Subject'] = Header('python test')

        server = smtplib.SMTP_SSL(smtp_server)
        #如果端口是用SSL加密，请这样写代码。其中server是变量名
        server.connect(smtp_server, 465)
        #如果出现编码错误UnicodeDecodeError，你可以这样写：server.connect('smtp.qq.com', 465,'utf-8')
        server.login(from_addr, password) 
        # 登陆邮箱

        # try...except...语句异常处理
        try:
            server.sendmail(from_addr, to_addr, msg.as_string()) 
            # sendmail是“发送邮件”的意思，是发送邮件用的，sendmail()方法需要三个参数：发件人，收件人和邮件内容
            #from_addr：邮件发送地址，就是上面的username
            #to_addr：邮件收件人地址
            #msg.as_string()：为一个字符串类型 
            print('恭喜，发送成功')
        except:
            print('发送失败，请重试')

server.quit() 
# 关闭服务器