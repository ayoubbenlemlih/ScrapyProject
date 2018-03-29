import scrapy

class LoginSpider(scrapy.Spider):
    name = 'avito'
    start_urls = ['https://www2.avito.ma/ai/form/0']

    def parse(self, response):
        body = '''------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="category_group"
        7010
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="type"
        s
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="lang"
        fr
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="rooms"
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="beds"
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="size"
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="brand"
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="model"
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="fuel"
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="regdate"
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="mileage"
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="pfiscale"
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="region"
        13
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="area"
        1076
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="address"
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="subject"
        vvvvvvvvv
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="body"
        aaaaaaaaaaaaaaaaaaaaddddddddddddd
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="mandatory_cv"
        0
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="price"
        100 000
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="price_meter"
        0
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="images[]"; filename=""
        Content-Type: application/octet-stream
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="company_ad"
        0
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="name"
        Nabil
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="email"
        ayoub.benlemlih@gmail.com
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="phone"
        0615016786
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="passwd"
        youssef2010
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="account_type"
        0
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="chosenVasId"
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="chosenVAS"
        ------WebKitFormBoundary5M31VB0KGabpTJF8--
        '''
        return scrapy.FormRequest(url="https://www2.avito.ma/ai/create/5",body=body,headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'content-length': '2934', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary5M31VB0KGabpTJF8', 'cookie': '__cfduid=db6da7f35d2f815e74d37ccb035df7e101522248405; lang=fr; _ga=GA1.3.856739748.1522248357; _gid=GA1.3.1665003636.1522248357; _vwo_uuid_v2=D62DE969B11559A3E5ED2AF09984708CE|762d2ddb1ed66ca5dd7eaab9fe818325; xtvrn=$480796$; xtant=1; __auc=6874c6f51626d129550b2e3559e; _ga=GA1.2.1510719296.1522248364; _gid=GA1.2.529784021.1522248364; name=Nabil; phone=0615016786; subCat=7010; show_intro=1; SL_C_23361dd035530_KEY=9cf621164e82dae659d0e20eacd4e630c4fc56b4; s=mc1x22808dfabccd3ecc88589782029bd6b1fd885e40; __asc=6b80daae16270b2791025ee42ad; default_ca=5; sq=ca=5&w=10005; xsq=w=1&ca=5; fav_region1=5; mail=ayoub.benlemlih@gmail.com; xtan=-; _gat_UA-53541355-1=1; _pulse2data=c91e27a5-8049-4d24-928f-24972a23b530,v,x,1522314624815,eyJpc3N1ZWRBdCI6IjIwMTgtMDMtMjhUMTQ6NDZaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..Ie4FB21UYZ32iWwl9Xis9A.KBYJCjtdqgh9vnv_X_XTu6YWWcsvSk8Vd_lgU2z9l50NcnrtoOVy7M2elIJGnUFRSO5_uxqFlhzrBkAisHRDhPTyVKIGzQPt2oLS8B30c3y7vx227rijwedv-4MW4cUOCyIQathnmYqzEHAj7ETh4U4iVWuo3mqbyCzkg3FlthMFVeqm1tl2lJBuIya-rYtt_IrVgQNKlhde0uPlMOMHcDt5PfFIuwZgo691C8WCX8E.uotllUCF_-7H2YYhmgEbTQ,4010339457416935829,1522328124815,true,,eyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..ersmNiJyo3WRh2gbLA2BSzLGpRJz12H3H0Vkdec9Fc0; amplitude_idavito.ma=eyJkZXZpY2VJZCI6IjUyNGVlZDIyLTY3MDAtNDI5YS05YmQ3LTk5YjZhYWRiODYyOSIsInVzZXJJZCI6ImF5b3ViLmJlbmxlbWxpaEBnbWFpbC5jb20iLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE1MjIzMDkxNjAyMDgsImxhc3RFdmVudFRpbWUiOjE1MjIzMTM3MzE5MDUsImV2ZW50SWQiOjE3LCJpZGVudGlmeUlkIjoxNCwic2VxdWVuY2VOdW1iZXIiOjMxfQ==; _pulse2data=c91e27a5-8049-4d24-928f-24972a23b530,v,x,1522314631908,eyJpc3N1ZWRBdCI6IjIwMTgtMDMtMjhUMTQ6NDZaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..Ie4FB21UYZ32iWwl9Xis9A.KBYJCjtdqgh9vnv_X_XTu6YWWcsvSk8Vd_lgU2z9l50NcnrtoOVy7M2elIJGnUFRSO5_uxqFlhzrBkAisHRDhPTyVKIGzQPt2oLS8B30c3y7vx227rijwedv-4MW4cUOCyIQathnmYqzEHAj7ETh4U4iVWuo3mqbyCzkg3FlthMFVeqm1tl2lJBuIya-rYtt_IrVgQNKlhde0uPlMOMHcDt5PfFIuwZgo691C8WCX8E.uotllUCF_-7H2YYhmgEbTQ,4010339457416935829,1522328131908,true,,eyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..ersmNiJyo3WRh2gbLA2BSzLGpRJz12H3H0Vkdec9Fc0', 'origin': 'https://www2.avito.ma', 'referer': 'https://www2.avito.ma/ai/form/5', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'},
                    callback=self.after_login)
        

    def after_login(self, response):
        self.logger.info(response.body)
        return
