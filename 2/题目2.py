# 书名、价格
import requests
import sqlite3

Header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

# 类别的json接口
URL_FOR_JSON = "https://www.ptpress.com.cn/recommendBook/getRecommendBookListForPortal?bookTagId="
# 获取图书细节的json接口
BASE_URL = "https://www.ptpress.com.cn/bookinfo/getBookDetailsById?bookId="
req=requests
conn = sqlite3.connect('book.db')
cursor = conn.cursor()


def GetBookType(url):
    res=req.get(url)
    print(res.json())
    return [(i['name'], i['bookTagId']) for i in res.json()['data']]

def GetBookIDs(url):
    res = req.get(url)
    # print([ i['bookId'] for i in res.json()['data']])
    return [i['bookId'] for i in res.json()['data']]

def GetDetails(bookId):
    details = []
    for Id in bookId:
        res=req.get(BASE_URL+Id)
        data = res.json()
        details.append(data['data'])
    return details
    

def SaveInDataBase(details,type):
    for detail in details:
        name = detail['bookName']
        price = detail['price']
        discountPrice = detail['discountPrice']
        try:
            cursor.execute(
                "insert into book (name,price,discountPrice,type)values(?,?,?,?)", (name, price, discountPrice, type))
        except Exception as e:
            print(e)

    
    
    

def SaveInFile(details):
    with open("books_of_cs.txt","w") as f:
        for detail in details:
            name = detail['bookName']
            price = detail['price']
            discountPrice = detail['discountPrice']
            f.write("书名："+str(name)+" "+"原价："+str(price) +
                    " "+"折后价："+str(discountPrice)+" "+"\n")


def main():
    cursor.execute(
        'create table book (name varchar(20) primary key, type varchar(20), price varchar(20), discountPrice varchar(20))')

    book_types = GetBookType(
        'https://www.ptpress.com.cn/recommendBook/getRecommendTypeListForPortal')

    for i in book_types:
        book_ids = GetBookIDs(URL_FOR_JSON+i[1])
        details = GetDetails(book_ids)
        # SaveInFile(details)
        SaveInDataBase(details,i[0])
        print(i[0]+"类已爬取完毕！")

    cursor.close()
    conn.commit()
    conn.close()

if __name__=='__main__':
    main()
