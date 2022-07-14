import re
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }

res = requests.get(
    "http://jhsjk.people.cn/", headers=headers, verify=False)

resHtml = res.content.decode()
# f = open("tmep.txt", "w", encoding='utf-8')
# f.write(resHtml)

# [\s\S]包括换行符的匹配
pat1 = '<div class="news-box">([\s\S]*?)</div>'
newsHtml = re.findall(pat1, resHtml)
pat2 = '<li>(.*?)</li>'
latestnews=re.findall(pat2,newsHtml[0])
# print(latestnews.__len__())

pat_title = "<span>(.*)</span>"
pat_link = 'href="(.*)" '
pat_source="来源：(.*)</i>"

f=open("人民网最新.txt","w")
for i in latestnews:
    title=re.findall(pat_title,i)
    link = re.findall(pat_link, i)
    source = re.findall(pat_source, i)
    # print(title)
    # print(link)
    # print(source)
    f.write("标题："+title[0]+" "+"链接："+"http://jhsjk.people.cn/"+link[0]+" "+"来源："+source[0]+"\n")
f.close()
