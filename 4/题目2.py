from pickle import TRUE
import requests
import jieba
import jieba.analyse
from lxml import etree
import os
from sklearn.feature_extraction.text import TfidfVectorizer

import warnings
warnings.filterwarnings("ignore")

# tf-idf实现模式：模式1为jieba实现，模式2为jieba+sklearn实现
# 模式2使用了自己设置的停用词表，所以两种模式结果有所不同
MODE=1

# 分词停用词表
STOP_WORDS = os.path.join(os.getcwd(), "stop_words.txt")
# 待比较的关键字
KEY_WORD="国科大"
# 爬取文章页数
MAX_PAGE_NUM = 1
# 基本URL
BASE_URL = "http://www.ucas.edu.cn/site/26?pn="
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38"
    }

req = requests
# 添加关键字到jieba词典
jieba.add_word(KEY_WORD)

# 文章类
class Article():
    def __init__(self,title,link):
        self.title = title
        self.link = link
        # TF-IDF算法得出的top10关键字及对应得分
        self.top_25 = {}
        
    # 获取文章内容
    def GetText(self):
        content=""
        html = etree.HTML(req.get(url=self.link, headers=HEADERS,verify=False).text)
        texts_list = html.xpath(
                '/html/body/div[4]/div[1]/div/div[1]/div[2]/div[2]/p/span/text()')

        for text in texts_list:
            if(text!=''):
                content+=text+'\n'
        return content

    # 使用sklearn提取关键字
    def GetTFIDFBySklearn(self):
        text = self.GetText()
        words_list = []
        stopwords = [line.strip() for line in open(
            STOP_WORDS, 'r', encoding='utf-8').readlines()]
        
        # 分词（剔除停用词）
        for word in jieba.cut(text):
            if word not in stopwords and word.strip() != '':
                words_list.append(word.strip())
        
        # tf-idf
        data = [' '.join(words_list)]
        tfidf = TfidfVectorizer()
        res = tfidf.fit_transform(data)
        res=res.toarray()
        voc=tfidf.vocabulary_

        details = {str(key): float(res[0,voc[key]]) for key in voc.keys()}

        # keywords = sorted(details.items(),key=lambda x: x[1], reverse=TRUE)
        print("文章：%s 关键字提取完毕..." % (self.title))
        
        for i in range(25):
            max_temp=0
            for key in details.keys():
                if(details[key]>=max_temp and key not in self.top_25.keys()):
                    self.top_25[key] = details[key]
                    max_temp = details[key]
                
        print("=======================================")
        print("top 10 关键字为：")
        count=0
        for key in self.top_25.keys():
            count+=1
            print(key+"\t"+str(self.top_25[key]))
            if(count==10):
                break
        print("=======================================\n")

    # 直接使用jieba提取关键字
    def GetTFIDFByJieba(self):
        text = self.GetText()
 
        # jieba提取关键字
        keywords=jieba.analyse.extract_tags(
            text, topK=25, withWeight=True)
        
        print("文章：%s 关键字提取完毕..." % (self.title))

        print("=======================================")
        print("top 10 关键字为：")
        for i in range(25):
            if(i<10):
                print(keywords[i][0]+"\t"+str(keywords[i][1]))
            self.top_25[keywords[i][0]] = keywords[i][1]
        print("=======================================\n")


articles_list=[]

# 获取前MAX_PAGE_NUM页文章的标题和链接
def CreateArtiles():
    for i in range(1,MAX_PAGE_NUM+1):
        url=BASE_URL+str(i)
        html=etree.HTML(req.get(url=url,headers=HEADERS).text)
        titles = html.xpath('//html/body/div[4]/div[2]/div[2]/div[3]/p/a/@title')
        links = html.xpath('//html/body/div[4]/div[2]/div[2]/div[3]/p/a/@href')

        for j in range(len(titles)):
            articles_list.append(Article(titles[j],links[j]))
        print("第%d页文章收集完毕..."%i)

# 获取与关键字最接近的文章
def GetBestMathcedArticle(mode):
    tf_idf=0
    best_matched_article=Article

    for article in articles_list:
        if(mode==1):
            article.GetTFIDFByJieba()
        else:
            article.GetTFIDFBySklearn()
        if KEY_WORD in article.top_25.keys():
            if(article.top_25[KEY_WORD]>tf_idf):
                best_matched_article=article
                tf_idf = article.top_25[KEY_WORD]
    
    if(tf_idf==0):
        print("未找到和%s有关的文章...增大MAX_PAGE_NUM后再试试吧..."%KEY_WORD)
    else:
        print("已找到关键字最佳相似文章：")
        print("*********************************")
        print("关键字：%s\n文章标题：%s\n文章链接：%s\ntf-idf：%f" %
              (KEY_WORD, best_matched_article.title, best_matched_article.link,tf_idf))
        print("*********************************")



def main():
    CreateArtiles()
    
    GetBestMathcedArticle(MODE)
    
main()
