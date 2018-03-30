import scrapy

class LoginSpider(scrapy.Spider):
    name = 'avito'
    start_urls = ['https://www.avito.ma/account/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'email': 'ayoub.benlemlih@gmail.com', 'passwd': 'youssef2010', 'login': 'Se connecter'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "Nabil" not in response.body:
            self.logger.info("Login failed")
            return
        self.logger.info("Login success")
        self.logger.info("headers Login"+str(response.request.headers))
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
        return scrapy.FormRequest(url="https://www2.avito.ma/ai/create/0",body=body,
                     callback=self.form)

    def form(self, response):
        self.logger.info(response.body)
        self.logger.info("success form")
        self.logger.info("headers form"+str(response.request.headers))
        return
