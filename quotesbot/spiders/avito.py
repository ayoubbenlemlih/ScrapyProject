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
        return scrapy.FormRequest(url="https://www2.avito.ma/ai/create/5",body=body,headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'content-length': '2934', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary5M31VB0KGabpTJF8', 'cookie': '__cfduid=deb2df73985aa2cc88ec2291341f303531522327088; s=mc1xb6a5edde5bcbde47d1992ba5222af9dd4c7d5bae; xtvrn=$480796$; xtan=-; xtant=1; show_intro=1; _ga=GA1.3.118621699.1522327041; _gid=GA1.3.1611307281.1522327041; _gat_UA-53541355-1=1; _vwo_uuid_v2=D6DFCE59562197F76B9E5F781331FAEFB|d6e4f31e3d775dcf860392a9aea9a4d4; __asc=b372b78116271c334d8838b6459; __auc=b372b78116271c334d8838b6459; SL_C_23361dd035530_KEY=9cf621164e82dae659d0e20eacd4e630c4fc56b4; amplitude_idavito.ma=eyJkZXZpY2VJZCI6IjI5MmJmZjY4LTRmODItNGQwYS1hY2JlLTk5YTkyNmEyMmQzZSIsInVzZXJJZCI6bnVsbCwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNTIyMzI3MDQwMjQ2LCJsYXN0RXZlbnRUaW1lIjoxNTIyMzI3MDQ5NjY5LCJldmVudElkIjoyLCJpZGVudGlmeUlkIjoyLCJzZXF1ZW5jZU51bWJlciI6NH0=; _pulse2data=3c1c2c82-ce2f-49a6-ab9d-bb205028b838,v,x,1522327949673,eyJpc3N1ZWRBdCI6IjIwMTgtMDMtMjlUMTI6MzhaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..CRehAuNNHWEa18-FgMGI6A.ywNMOrvWnvM48rJ_Kvln8Hj9m8rYfwLsHc8XyOICAAx-scvQOYFDU44WMNF7RxqUs7B2_22-7uYhZyJ-rJ_UcupWlgDWuMn6qZ8ybUDugcZhUwyvd-trNuXT5U1bXUPAMfv4K3hJnseXq5nAU3pvI1FJng75Gq42vk8b3vHT1LsXPji03zbKVDuyU5ad1oRM0FvQnjvvpSf9N4ePBAEWjw.-qJvv1qgL342wCsEm82zDg,,1522341449673,true,unresolved,eyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..hesWYn4in2tOlHrrv6yjn3jc_Lid49f_NZvq27doj8U; subCat=7010', 'origin': 'https://www2.avito.ma', 'referer': 'https://www2.avito.ma/ai/form/5', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'},
                    callback=self.after_login)
        

    def after_login(self, response):
        self.logger.info(response.body)
        return
