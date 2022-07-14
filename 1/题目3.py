from ntpath import join
import os
import re
import requests

HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
PAGE_NUM=2
URL = "https://list.jd.com/list.html?tid=1014398&page="
CWD = os.getcwd()
req = requests



def SavePic(pic_url,name,_class,page):
    
    if(not os.path.exists(os.path.join(CWD, "pics_from_JD"))):
        os.mkdir(CWD+"/pics_from_JD")
        os.makedirs(CWD+"/pics_from_JD"+"/small")
        os.makedirs(CWD+"/pics_from_JD"+"/big")
    path = os.path.join(
        CWD+"/pics_from_JD", _class, page+"_"+name+".jpg")
    try:
        f = open(path, "wb")
        data = req.get(pic_url, headers=HEADER).content
        f.write(data)
        f.close()
    except Exception as e:
        print(e)
# SavePic("https://img14.360buyimg.com/n0/jfs/t1/194751/15/16966/61334/610ba716E85c44a96/c42fb9e4ffa8bdd8.jpg", "test")

def main():
    print("========开始爬取京东手机图片========")
    print("页面数量："+str(PAGE_NUM))

    for i in range(PAGE_NUM):
        index = 2*i+1
        # 京东url中page全为奇数
        ResHtml = req.get(URL+str(index), headers=HEADER).content.decode()
        pat_img = 'data-lazy-img="(.*?)" />'
        small_imgurls_list=re.findall(pat_img,ResHtml)
        small_imgurls_list=["https:"+ i for i in small_imgurls_list]
        
        big_imgurls_list = [
            re.sub("img1[0-3]", "img14", i.replace("n7", "n0")) for i in small_imgurls_list]
        
        for j in range(small_imgurls_list.__len__()):
            SavePic(small_imgurls_list[j], str(j+1), "small", str(i+1))
            SavePic(big_imgurls_list[j], str(j+1), "big", str(i+1))
            print("第 %d 张图片已爬取完毕..." % (j+1))
        
        print("第 %d 页已爬取完毕，共 %d 张图片！" %
              (i+1, small_imgurls_list.__len__()))

if __name__=="__main__":
    main()
