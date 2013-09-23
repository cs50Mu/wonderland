#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

import smtplib,sys,requests,re
from email.mime.text import MIMEText

send_mail_host="smtp.126.com"      # 发送的smtp
send_mail_user="chunyumou"
send_mail_user_name="深蓝"
send_mail_pswd="ILoveLinux"
send_mail_postfix="126.com"  #发邮件的域名
get_mail_user="13821207300"
charset="utf-8"   # 若不设置这个，中文会出乱码

get_mail_postfix="139.com"
get_mail_host="pop.139.com"

def send_mail(subject,content):

    send_mail_address=send_mail_user_name+"<"+send_mail_user+"@"+send_mail_postfix+">"
    msg=MIMEText(content,"html",charset)
    msg['Subject']=subject    # 这里按说也要设置charset，不过目前没问题
    msg['From']=send_mail_address
    msg['to']=to_address="139SMSserver<"+get_mail_user+"@"+get_mail_postfix+">"
    try:
        stp = smtplib.SMTP()
        stp.connect(send_mail_host)
        stp.login(send_mail_user,send_mail_pswd)
        stp.sendmail(send_mail_address, to_address, msg.as_string())
        stp.close()
        return True
    except Exception,e:
        print str(e)
        return False

def getweather():

    reload(sys)
    sys.setdefaultencoding('utf-8')  # notice here
    r = requests.get('http://wap.weather.com.cn/wap/weather/101030100.shtml')
    #with open('weather.html','w') as f:
    #    f.write(r.text)
    issuetime = re.findall(r'<h3>(.+?)</h3>',r.text)
    time = re.findall(r'<dd>(.+?)<br',r.text)
    weather = re.findall(r'<dt>(.+?)<br />&nbsp;(.+?)</dt>',r.text)
    message = '%s，今天是%s，今天天气：%s，%s' %(issuetime[0],time[0],weather[0][0],weather[0][1])
    return message


#print issuetime,'\n\n',time,'\n\n',weather

#for (x,y) in weather:
#    print x,y,'\n'

#print '发布时间： %s\n今天是%s\n今天天气：%s,%s' %(issuetime[0],time[0],weather[0][0],weather[0][1])


if __name__ == '__main__': 
    if send_mail('新的一天开始了！',getweather()):
        print '发送成功'
    else:
        print '发送失败'


#if __name__ == '__main__': 
#    if len(sys.argv) != 3:
#        print "Usage: ./mailto139.py 'subject' 'content'"
#        sys.exit(-1)
#    if send_mail(sys.argv[1],sys.argv[2]):
#        print '发送成功'
#    else:
#        print '发送失败'
