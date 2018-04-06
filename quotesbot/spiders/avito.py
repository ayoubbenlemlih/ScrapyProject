import scrapy

class LoginSpider(scrapy.Spider):
    name = 'avito'
    start_urls = ['https://www.avito.ma/account/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'email': 'ayoub.benlemlih@gmail.com', 'passwd': 'youssef2010', 'login': 'Se connecter'},callback=self.after_login
        )
    
    def after_login(self, response):
        # check login succeed before going on
        if "Nabil" not in response.body:
            self.logger.info("Login failed")
            return
        self.logger.info("Login success")
        self.logger.info("headers login"+str(response.request.headers))
        self.logger.info("body login"+str(response.request.body))
        return scrapy.Request (url = "https://www2.avito.ma/ai/form/0" ,headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7', 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'},
 callback = self.form,dont_filter=True)

    def form(self, response):
        self.logger.info("headers form"+str(response.request.headers))
        self.logger.info("body form"+str(response.request.body))  
        url2 = 'https://www2.avito.ma/ai/create/0'
        url = 'https://httpbin.org/anything'
        return scrapy.FormRequest(url = url,method = 'POST',headers={'content-type': 'multipart/form-data','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0',   'origin': 'https://www2.avito.ma', 'referer': 'https://www2.avito.ma/ai/form/0', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'},
                                  formdata={'account_type':'0', 'address':'', 'area':'154', 'beds':'', 'body':'azazazazazazazazazazazazazaz', 'brand':'', 'category_group':'7010', 'chosenVAS':'insertion', 'chosenVasId':'62', 'company_ad':'0', 'email':'ayoub.benlemlih@gmail.com', 'fuel':'', 'images[]':'', 'lang':'fr', 'mandatory_cv':'0', 'mileage':'', 'model':'', 'name':'Nabil', 'passwd':'youssef2010', 'pfiscale':'', 'phone':'0615016786', 'price':'10', 'price_meter':'0', 'regdate':'', 'region':'17', 'rooms':'', 'size':'', 'subject':'ddddddddd', 'type':'s', 'email_confirm' :'ayoub.benlemlih@gmail.com','validate':'Déposez votre annonce »'},
                                  callback=self.create,dont_filter=True)

    def create(self, response):
        self.logger.info(response.body)
        self.logger.info("headers create"+str(response.request.headers))
        self.logger.info("body create"+str(response.request.body))        
        return
