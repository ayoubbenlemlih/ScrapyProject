import scrapy

class LoginSpider(scrapy.Spider):
    name = 'avito'
    start_urls = ['https://www.avito.ma/account/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'email': 'ayoub.benlemlih@gmail.com', 'passwd': 'youssef2010', 'login': 'Se connecter'},callback=self.after_login
        )
    
    def after_login(self, response):
        # check login succeed before going on
        if "Nabil" not in response.body:
            self.logger.info("Login failed")
            return
        self.logger.info("Login success")
        self.logger.info("headers login"+str(response.request.headers))
        self.logger.info("body login"+str(response.request.body))
        return scrapy.Request (url = "https://www2.avito.ma/ai/form/0" ,headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7', 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'},
 callback = self.form,dont_filter=True)

    def form(self, response):
        self.logger.info("headers form"+str(response.request.headers))
        self.logger.info("body form"+str(response.request.body))
        
        body = '''------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="category_group"

        7010
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="type"

        s
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="lang"

        fr
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="rooms"


        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="beds"


        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="size"


        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="brand"


        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="model"


        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="fuel"


        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="regdate"


        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="mileage"


        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="pfiscale"


        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="region"

        17
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="area"

        154
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="address"


        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="subject"

        ffffffffffffffffffffffffffffffffffffff
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="body"

        dddddddddddddddddddddddddddddddddddd
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="mandatory_cv"

        0
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="price"

        100 000
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="price_meter"

        0
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="images[]"; filename=""
        Content-Type: application/octet-stream


        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="company_ad"

        0
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="name"

        Nabil
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="email"

        ayoub.benlemlih@gmail.com
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="phone"

        0615016786
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="email_confirm"

        ayoub.benlemlih@gmail.com
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="passwd"


        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="account_type"

        0
        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="chosenVasId"


        ------WebKitFormBoundary5tKbPFdKTvzi2zTy
        Content-Disposition: form-data; name="chosenVAS"


        ------WebKitFormBoundary5tKbPFdKTvzi2zTy--
        '''
        return scrapy.Request(url="https://www2.avito.ma/ai/create/0",method = 'POST',body = body,headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary5tKbPFdKTvzi2zTy',  'origin': 'https://www2.avito.ma', 'referer': 'https://www2.avito.ma/ai/form/0', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'},
                                  callback=self.create,dont_filter=True)

    def create(self, response):
        self.logger.info(response.body)
        self.logger.info("headers create"+str(response.request.headers))
        self.logger.info("body create"+str(response.request.body))        
        return
