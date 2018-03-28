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
        return scrapy.Request(url = "https://www.avito.ma/fr/account/deactivated_ads",callback=self.deactivated)

    def deactivated(self, response):
        # check login succeed before going on
        if "Mercedes" not in response.body:
            self.logger.info("deactivated failed")
            return
        self.logger.info("deactivated success")
        return
