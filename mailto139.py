#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 03/08/2014

"""get weather information from 'www.weather.com.cn'
and send it to my 126 email which will notify me
through SMS
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
    r = requests.get('http://www.weather.com.cn/textFC/hb.shtml')
    #with open('weather.html','w') as f:
    #    f.write(r.text)
    issuetime = (re.findall(r'<dt>\s+(.+?)\s+<span',r.text,flags=re.S))[0]
    TJtable = (re.findall(r'<table\s+.+?</table>',r.text,flags=re.S))[1]
    TJtr = (re.findall(r'<tr>.+?</tr>',TJtable,flags=re.S))[2]
    sky = (re.findall(r'<td width="82">(.+?)</td>',TJtr,flags=re.S))[0]
    wind = (re.findall(r'<td width="168"><span>(.+?)</span><span class="conMidtabright">(.+?)</span>',TJtr,flags=re.S))[0]
    temperature = (re.findall(r'<td width="86">(.+?)</td>',TJtr,flags=re.S))[0]
    return '%s,今天天气%s,%s,%s,气温%s\nHave a NICE day!' %(issuetime,sky,wind[0],wind[1],temperature)

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
