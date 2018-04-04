

import scrapy
import requests

class LoginSpider(scrapy.Spider):
    name = 'avito'
    start_urls = ['https://www.avito.ma']

    def parse(self, response):

        url = 'https://www.avito.ma/account/login'
        rsp = requests.get(url)
        cookies =rsp.cookies
        data = {'email': 'ayoub.benlemlih@gmail.com', 'passwd': 'youssef2010', 'login': 'Se connecter'}
        r=requests.post('https://www.avito.ma/account/do_login',cookies=cookies ,data = data ,allow_redirects=True )
        self.logger.info(r.text)
        cookies.update(r.cookies)
        r2=requests.get('https://www2.avito.ma/ai/form/0')
        self.logger.info(r2.text)       
        return
    
    
