

import scrapy
import requests

class LoginSpider(scrapy.Spider):
    name = 'avito'
    start_urls = ['https://www.avito.ma']

    def parse(self, response):
        headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                 'cache-control': 'max-age=0','origin': 'https://www2.avito.ma', 'referer': 'https://www2.avito.ma/ai/form/0', 'upgrade-insecure-requests': '1',
                 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        files = {'category_group': (None, '7010'),'type': (None, 's'),'lang': (None, 'fr'),'rooms': (None, '')
                ,'beds': (None, ''),'size': (None, ''),'brand': (None, ''),'model': (None, '')
                ,'fuel': (None, ''),'regdate': (None, ''),'mileage': (None, ''),'pfiscale': (None, '')
                ,'region': (None, '17'),'area': (None, '154'),'address': (None, ''),'subject': (None, 'ffffffffffffffffffffffffffffffffffffff')
                ,'body': (None, 'dddddddddddddddddddddddddddddddddddd'),'mandatory_cv': (None, '0'),'price': (None, '100 000')
                 ,'price_meter': (None, '0'),'images[]': ('', '','application/octet-stream'),'company_ad': (None, '0')
                ,'name': (None, 'Nabil'),'email': (None, 'ayoub.benlemlih@gmail.com'),'phone': (None, '0615016786')
                ,'email_confirm': (None, 'ayoub.benlemlih@gmail.com'),'passwd': (None, 'youssef'),'account_type': (None, '0'),'chosenVasId': (None, '')
                ,'chosenVAS': (None, '')}
        url = 'https://www2.avito.ma/ai/create/0'
        no_file_multipart_req = requests.Request('POST', url ,files=files).prepare()
        self.logger.info(no_file_multipart_req.body.decode('utf-8'))
        s = requests.Session()
        r=s.send(no_file_multipart_req)
        self.logger.info(r.text)
        return
    
    
