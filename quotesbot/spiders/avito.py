

import scrapy
import requests

class LoginSpider(scrapy.Spider):
    name = 'avito'
    start_urls = ['https://www.avito.ma']

    def parse(self, response):

        url = 'https://www.avito.ma/account/login'
        rsp = requests.get(url)
        cookies =rsp.cookies
        self.logger.info(cookies)
        data = {'email': 'ayoub.benlemlih@gmail.com', 'passwd': 'youssef2010', 'login': 'Se connecter'}
        r=requests.post('https://www.avito.ma/account/do_login',cookies=cookies ,data = data ,allow_redirects=False )
        self.logger.info(r.text)
        cookies.update(r.cookies)
        self.logger.info(cookies)
        r2=requests.get('https://www2.avito.ma/ai/form/0',cookies=cookies)
        self.logger.info(r2.text)
        cookies.update(r2.cookies)
        cookiesspecial = 'mail=ayoub.benlemlih%40gmail.com; name=Nabil; phone=0615016786; amplitude_idavito.ma=eyJkZXZpY2VJZCI6IjExZjNiYjVjLTU5ODQtNGUyZC05ZWMzLWI1NTJkZTI4ZWZlYyIsInVzZXJJZCI6bnVsbCwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNTIyODU1OTE0NTgzLCJsYXN0RXZlbnRUaW1lIjoxNTIyODU1OTE1MDA5LCJldmVudElkIjoxLCJpZGVudGlmeUlkIjoxLCJzZXF1ZW5jZU51bWJlciI6Mn0=; xtvrn=$480796$; xtan=1-2282924; xtant=1; show_intro=1; _ga=GA1.3.12530522.1522855916; _gid=GA1.3.400564888.1522855916; __asc=5babbb37162914931af2a5f2ded; __auc=5babbb37162914931af2a5f2ded; _vwo_uuid_v2=DF390B6F66BC3E7A080C36FF6C1544266|22f3efb3cf3d11915444498175427bab; _pulse2data=49b44225-5019-407a-b5e6-79e5c8f4304e,v,x,1522856816339,eyJpc3N1ZWRBdCI6IjIwMTgtMDQtMDRUMTU6MzJaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..ETer67QMHjZRUUmu4jqZcQ.zKpJuZbWXoSHGL8xWU48waGCeyDjiw6S5T_dAwIhtN3TF7Bho5zJeYVrxM-J_Oc7Q8QcY7PfSeFnegKBx-cV6uUjk_PsLBAi4IFCI3C8iuXNmRfbi33tZo4n4KCw1F02o_BBwO0-kOv4xz0ZMbRlDuZawDM-9tmKkApb7GVCBCt0al22jF7yQFyjwFEgwsGyklzNIzpfIiJyIDoYSM8hrQ.lDNsZoUqDHaIWDKDIuxjOA,,1522870316339,true,unresolved,eyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..CBPtTVB-Bu36Gw2RAfWZBT8rRFakitxcI5NZOZhHE7Q; SL_C_23361dd035530_VID=n64h0oR2KY8w; SL_C_23361dd035530_KEY=9cf621164e82dae659d0e20eacd4e630c4fc56b4; SL_C_23361dd035530_SID=T3rPaoq4NYAu'
        cookies.update(cookiesspecial.cookies)
        self.logger.info(cookies)
        
        headers={'authority':'www2.avito.ma','method':'POST','path':'/ai/create/0','scheme':'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
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
                ,'email_confirm': (None, 'ayoub.benlemlih@gmail.com'),'passwd': (None, 'youssef2010'),'account_type': (None, '0'),'chosenVasId': (None, '')
                ,'chosenVAS': (None, '')}
        url = 'https://www2.avito.ma/ai/create/0'
        url2 = 'http://httpbin.org/cookies'
        no_file_multipart_req = requests.Request('POST', url ,files=files,cookies=cookies,headers=headers).prepare()
        self.logger.info(no_file_multipart_req.body.decode('utf-8'))
        s = requests.Session()
        r=s.send(no_file_multipart_req,allow_redirects= True)
        cookies.update(r.cookies)
        self.logger.info(cookies)
        self.logger.info(r.text)
        return
    
    
