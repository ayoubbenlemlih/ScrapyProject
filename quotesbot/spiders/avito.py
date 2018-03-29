import scrapy

class LoginSpider(scrapy.Spider):
    name = 'example.com'
    start_urls = ['https://www.avito.ma/account/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'email': 'ayoub.benlemlih@gmail.com', 'passwd': 'youssef2010', 'login': 'Se connecter'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "Changez cela aujourd" not in response.body:
            self.logger.info("Login failed")
            return
        self.logger.info("Login success")
        #return scrapy.Request(url = "https://www.avito.ma/fr/account/deactivated_ads",callback=self.deactivated)
        return scrapy.FormRequest(url="https://www2.avito.ma/ai/create/0",headers={Content-Type:'multipart/form-data'},
                    formdata={'account_type':'0', 'address':'', 'area':'154', 'beds':'', 'body':'azazazazazazazazazazazazazaz', 'brand':'', 'category_group':'7010', 'chosenVAS':'', 'chosenVasId':'', 'company_ad':'0', 'email':'ayoub.benlemlih@gmail.com', 'fuel':'', 'images[]':'', 'lang':'fr', 'mandatory_cv':'0', 'mileage':'', 'model':'', 'name':'Nabil', 'passwd':'', 'pfiscale':'', 'phone':'0615016786', 'price':'10', 'price_meter':'0', 'regdate':'', 'region':'17', 'rooms':'', 'size':'', 'subject':'ddddddddd', 'type':'s', 'email_confirm' :'ayoub.benlemlih@gmail.com'},
                    callback=self.form)
    def deactivated(self, response):
        # check login succeed before going on
        if "Mercedes" not in response.body:
            self.logger.info("deactivated failed")
            return
        self.logger.info("deactivated success")
        return

    def form(self, response):
        self.logger.info(response.body)
        return
