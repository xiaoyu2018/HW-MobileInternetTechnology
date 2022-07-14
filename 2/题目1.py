import requests
from lxml import etree
import re

Header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
URL = "https://www.ucas.ac.cn/"

response = requests.get(URL, headers=Header,verify=False)

# print(response)
# with open("official_site_of_ucas.txt","w",encoding="utf-8") as f:
#     f.write(response.content.decode())
# f = open("official_site_of_ucas.txt","r",encoding="utf-8")

original_html = response.content.decode()
reduced_html = re.findall(
    '<li class="mainlevel">[\s\S]*</ul>\s*</li>', original_html)[0]
# print(reduced_html)

dom_tree = etree.HTML(reduced_html)
top_levels = dom_tree.xpath('//li[@class="mainlevel"]')
# print(top_levels)

top_text_list=[]
subordinates_text_list=[]
for tl in top_levels:
    top_text=tl.xpath("./a/text()")
    top_text_list.append(top_text[0])
    subordinates_text = tl.xpath("./ul/li/a/text()")
    # print(subordinates_text)
    subordinates_text_list.append(subordinates_text)


for i in range(top_text_list.__len__()):
    print(top_text_list[i])
    for j in subordinates_text_list[i]:
        print("---"+j)
