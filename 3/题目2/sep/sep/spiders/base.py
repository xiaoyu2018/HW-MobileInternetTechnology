import scrapy

# 输入自己的账户密码
USER_NAME="example@example.com"
PASS_WORD="password"

class BaseSpider(scrapy.Spider):
    name = 'base'
    allowed_domains = ['ucas.ac.cn']
    start_urls = ['http://sep.ucas.ac.cn/']
    
    def start_requests(self):
        url = self.start_urls[0]
        yield scrapy.Request(url=url,callback=self.parse,meta={"cookiejar":1})
    
    def parse(self, response):
        form = response.xpath(
            '//*[@id="time_line"]/div[1]/form/div[1]/div/div/div')
        post_data = {
            'userName': USER_NAME,
            'pwd': PASS_WORD,
            'sb': 'sb'
        }
        if(len(form)==3):
            yield scrapy.Request(url="http://sep.ucas.ac.cn/randomcode.jpg", 
            callback=self.before_login, 
            meta={"cookiejar": response.meta["cookiejar"], 'post_data':post_data}
            )
    
    def before_login(self, response):
        with open("code.jpg","wb") as f:
            f.write(response.body)
        
        code = input("请输入验证码，验证码图片为当前路径下code.jpg\n")
        post_data=response.meta['post_data']
        post_data['certCode'] = code

        yield scrapy.FormRequest(
            url='http://sep.ucas.ac.cn/slogin',
            callback=self.after_login,
            formdata=post_data,
            meta={"cookiejar": response.meta["cookiejar"]}
        )

    def after_login(self, response):
        lis = response.xpath('//*[@id="main-metro"]/ul/li')

        for li in lis:
            for a in li.xpath('./a'):
                print(a.xpath('./@title').extract_first())
