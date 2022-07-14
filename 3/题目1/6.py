import requests

Header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

COOKIE = [
    {
        "domain": ".taobao.com",
        "expirationDate": 1663596112.198422,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_cc_",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "U%2BGCWk%2F7og%3D%3D",
        "id": 1
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "_l_g_",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "Ug%3D%3D",
        "id": 2
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1632636064.259613,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_m_h5_tk",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "3a219f608b5f9b5f370bcf4396d38180_1632040624346",
        "id": 3
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1632636064.259634,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_m_h5_tk_enc",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "ef35bfb64509c1f6cb21d66b99e657d6",
        "id": 4
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "_nk_",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "tb953803831502",
        "id": 5
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "_samesite_flag_",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "True",
        "id": 6
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "_tb_token_",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "b90e5453b8db",
        "id": 7
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "cancelledSubSites",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "empty",
        "id": 8
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 2262751264,
        "hostOnly": False,
        "httpOnly": False,
        "name": "cna",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "Zk9SGdQK/xwCASeYDwfEyG5T",
        "id": 9
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "cookie1",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "BxE3vzarRA4qJdZJxdXHLZRMm1fowQVnFFDS%2FU46bmY%3D",
        "id": 10
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "cookie17",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "UUpgRKuaNd0ZPQ9M8Q%3D%3D",
        "id": 11
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "cookie2",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "10f909677230a9cc45cd535aca383ec6",
        "id": 12
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "csg",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "1048d922",
        "id": 13
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "dnk",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "tb953803831502",
        "id": 14
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1947391313.257035,
        "hostOnly": False,
        "httpOnly": True,
        "name": "enc",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "GjCPviG19nocqJhzuNrAQalMaakLJIeVW6rm2Z8rAzrzMgJybKeU9K%2FojpPrkOAhd0%2FMhSHvY2vCUXqfk3at4LWKcfGHq3bMD4bfTOVEoQs%3D",
        "id": 15
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "existShop",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "MTYzMjAzMTMxMg%3D%3D",
        "id": 16
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1663596114.553023,
        "hostOnly": False,
        "httpOnly": False,
        "name": "hng",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "CN%7Czh-CN%7CCNY%7C156",
        "id": 17
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1647583327,
        "hostOnly": False,
        "httpOnly": False,
        "name": "isg",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "BHFxJsj7tEYt_hgDkfdlWR80gP0LXuXQdWXaclOGAThXepDMm6xDoEKQmA4csn0I",
        "id": 18
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1647583330,
        "hostOnly": False,
        "httpOnly": False,
        "name": "l",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "eBM8Lh84gYHyRKgbBOfwlurza77tAIRAguPzaNbMiOCP_ACe51ddW6FPeETwCnGVh6SkR35okuQ6BeYBqCVQUGiZIosM_Ckmn",
        "id": 19
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1634652112.198269,
        "hostOnly": False,
        "httpOnly": False,
        "name": "lgc",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "tb953803831502",
        "id": 20
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1632664914.27357,
        "hostOnly": False,
        "httpOnly": False,
        "name": "mt",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "ci=0_1",
        "id": 21
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "sg",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "212",
        "id": 22
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1663596112.198116,
        "hostOnly": False,
        "httpOnly": True,
        "name": "sgcookie",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "E100KduzkWTYtoWHGg6E%2Fy6BafbyXomwaFRCST%2BL7%2FKggzfL0R6fiZSvakiJmRjaTkUN4atptrtNNlTwrwSh%2B%2BQAMwP7wJeLJe%2FDQlS%2BD%2Fj%2BS%2Fw%3D",
        "id": 23
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "skt",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "95b706038217593b",
        "id": 24
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1639836112.198292,
        "hostOnly": False,
        "httpOnly": False,
        "name": "t",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "3178155a2a3433d03f036dabba10094a",
        "id": 25
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1647583330,
        "hostOnly": False,
        "httpOnly": False,
        "name": "tfstk",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "cr91Be2V-P4shVh4QhiU7zy5UzXca0zPcm76fQSK1XFQVy-1JsmQUaOvH9UFwmjC.",
        "id": 26
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1663135314,
        "hostOnly": False,
        "httpOnly": False,
        "name": "thw",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "cn",
        "id": 27
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1663596112.198392,
        "hostOnly": False,
        "httpOnly": False,
        "name": "tracknick",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "tb953803831502",
        "id": 28
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "uc1",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "cookie14=Uoe3dYEQjxUT7w%3D%3D&existShop=False&cookie15=UtASsssmOIJ0bQ%3D%3D&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&pas=0&cookie21=W5iHLLyFfoaZ",
        "id": 29
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1634652112.198243,
        "hostOnly": False,
        "httpOnly": True,
        "name": "uc3",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "vt3=F8dCujd8Ylmtac%2Bq2qE%3D&nk2=F5RMHKnEoIrVppHa8rc%3D&id2=UUpgRKuaNd0ZPQ9M8Q%3D%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D",
        "id": 30
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1634652112.198367,
        "hostOnly": False,
        "httpOnly": True,
        "name": "uc4",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "nk4=0%40FY4HWU%2BUqjaIiayU1%2FFO%2BOXT2T25dQ4lBA%3D%3D&id4=0%40U2gqy1rmXtJFsnWzffVhMJ1uB9Zhf3lu",
        "id": 31
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "unb",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "2212681787801",
        "id": 32
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1632117667,
        "hostOnly": False,
        "httpOnly": False,
        "name": "xlly_s",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "1",
        "id": 33
    }
]

# 不登录淘宝无法搜索，所以选择一个搜索得到的页面进行测试
TEST_URL = "https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.21814703.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=python&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest"


cookies={}
for i in COOKIE:
    cookies[i["name"]]=i["value"]

print(cookies)
session=requests.session()
session.headers=Header
cookies_jar = requests.utils.cookiejar_from_dict(
    cookies, cookiejar=None, overwrite=True)
session.cookies = cookies_jar
res=session.get(TEST_URL)

print(res.content.decode())

with open("taobao.txt","w",encoding="utf-8") as f:
    f.write(res.content.decode())
