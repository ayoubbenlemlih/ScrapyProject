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
            self.logger.error("Login failed")
            return
        self.logger.info("Login success")
        return
