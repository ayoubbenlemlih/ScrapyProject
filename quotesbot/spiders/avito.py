

import scrapy
import requests

class LoginSpider(scrapy.Spider):
    name = 'avito'
    start_urls = ['https://www.avito.ma']

    def parse(self, response):

        url = 'https://www.avito.ma/account/login'
        data = {'email': 'ayoub.benlemlih@gmail.com', 'passwd': 'youssef2010', 'login': 'Se connecter'}
        r=requests.post('https://www.avito.ma/account/do_login',data = data ,allow_redirects=True )
        self.logger.info(r.text)
        return
    
    
