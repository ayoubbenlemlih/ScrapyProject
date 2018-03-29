import scrapy

class LoginSpider(scrapy.Spider):
    name = 'avito'
    start_urls = ['https://www.avito.ma/account/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'email': 'ayoub.benlemlih@gmail.com', 'passwd': 'youssef2010', 'login': 'Se connecter'},
            callback=self.form
        )
    def form(self, response):
        return scrapy.Request(url="https://www2.avito.ma/ai/form/0",
            callback=self.create,dont_filter=True
        )

    def create(self, response):
        # check login succeed before going on
        if "Nabil" not in response.body:
            self.logger.info("Login failed")
            return
        self.logger.info("Login success")
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

        
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="account_type"

        0
        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="chosenVasId"


        ------WebKitFormBoundary5M31VB0KGabpTJF8
        Content-Disposition: form-data; name="chosenVAS"


        ------WebKitFormBoundary5M31VB0KGabpTJF8--
        '''
        return scrapy.FormRequest(url="https://www2.avito.ma/ai/create/0",body=body,headers={'Content-Type':'multipart/form-data; boundary=------WebKitFormBoundary5M31VB0KGabpTJF8'},
                    callback=self.after_create,dont_filter=True)

    def after_create(self, response):
        self.logger.info(response.body)
        return
