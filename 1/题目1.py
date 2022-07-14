import urllib
import re

import urllib.request
import re
data = urllib.request.urlopen(
    "http://www.ucas.ac.cn/site/37").read().decode("utf-8")

pat_email="Email：(.*)</p>"
pat_tel="联系电话：(.*)</p>"

email=re.findall(pat_email,data)
tel = re.findall(pat_tel, data)

print("邮件："+email[0])
print("电话："+tel[0])
