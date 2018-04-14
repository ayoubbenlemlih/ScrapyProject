import scrapy
import requests
import urllib
class LoginSpider(scrapy.Spider):
    name = 'avito'
    start_urls = ['https://www.avito.ma']

    def parse(self, response):

        url = 'https://www.avito.ma/account/login'
        headers={'authority':'www2.avito.ma','method':'GET','path':'/account/login','scheme':'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','upgrade-insecure-requests': '1',
                 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        rsp = requests.get(url,headers=headers)
        cookies =rsp.cookies
        data = {'email': 'ayoub.benlemlih@gmail.com', 'passwd': 'youssef2010', 'login': 'Se connecter'}
        r=requests.post('https://www.avito.ma/account/do_login',cookies=cookies ,data = data ,allow_redirects=False )
        #self.logger.info(r.text)
        cookies.update(r.cookies)
        r2=requests.get('https://www2.avito.ma/ai/form/0',cookies=cookies,headers=headers)
        #self.logger.info(r2.text)
        cookies.update(r2.cookies)
        
        headers={'authority':'www2.avito.ma','method':'POST','path':'/ai/create/0','scheme':'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                 'cache-control': 'max-age=0','origin': 'https://www2.avito.ma', 'referer': 'https://www2.avito.ma/ai/form/0', 'upgrade-insecure-requests': '1',
                 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
      #  img =  urllib.request.urlopen('https://www.avito.ma/thumbs/26/2665577777.jpg')
        
        files = {'category_group': (None, '7010'),'type': (None, 's'),'lang': (None, 'fr'),'rooms': (None, '')
                ,'beds': (None, ''),'size': (None, ''),'brand': (None, ''),'model': (None, '')
                ,'fuel': (None, ''),'regdate': (None, ''),'mileage': (None, ''),'pfiscale': (None, '')
                ,'region': (None, '17'),'area': (None, '154'),'address': (None, ''),'subject': (None, 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesept')
                ,'body': (None, '•	Dzazzzzzzzzzzzz \n •	zaddzzzzzzz'),'mandatory_cv': (None, '0'),'price': (None, '100 000')
                 ,'price_meter': (None, '0'),'images_urls[]': (None, '2665577777.jpg'),'images[]': ('', '','application/octet-stream'),'company_ad': (None, '0')
                ,'name': (None, 'Ayoub'),'email': (None, 'ayoub.benlemlih@gmail.com'),'phone': (None, '0615016786')
                ,'email_confirm': (None, 'a.benlemlih@mgpap.org.ma'),'passwd': (None, ''),'account_type': (None, '0'),'chosenVasId': (None, '62')
                ,'chosenVAS': (None, 'insertion'),'validate': (None, 'Déposez votre annonce »') }
        url = 'https://www2.avito.ma/ai/create/0'
        p = requests.Request('POST', url ,files=files,cookies=cookies,headers=headers).prepare()
        self.logger.info(p.body.decode('utf-8'))
        s = requests.Session()
        r3=s.send(p,allow_redirects= True)
        cookies.update(r3.cookies)
        #self.logger.info(cookies)
        self.logger.info(r3.text)
        return
