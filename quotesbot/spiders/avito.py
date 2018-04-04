

import scrapy
import requests

class LoginSpider(scrapy.Spider):
    name = 'avito'
    start_urls = ['https://www.avito.ma/account/login']

    def parse(self, response):
        files = {'name2': (None, 'content','text/plain')}
        no_file_multipart_req = requests.Request('POST', 'http://httpbin.org/anything' ,files=files).prepare()
        self.logger.info(no_file_multipart_req.body.decode('utf-8'))
        s = requests.Session()
        r=s.send(no_file_multipart_req)
        self.logger.info(r.text)
        return
    
    
