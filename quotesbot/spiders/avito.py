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
        body = '''------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="category_group"

        7010
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="type"

        s
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="lang"

        fr
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="rooms"


        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="beds"


        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="size"


        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="brand"


        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="model"


        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="fuel"


        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="regdate"


        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="mileage"


        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="pfiscale"


        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="region"

        7
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="area"

        566
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="address"


        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="subject"

        eeeeeeeeeeeeeee
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="body"

        aoaoaoaoaoaoaoaoaoaoaoaoa
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="mandatory_cv"

        0
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="price"

        800 000
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="price_meter"

        0
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="images[]"; filename=""
        Content-Type: application/octet-stream


        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="company_ad"

        0
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="name"

        Nabil
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="email"

        ayoub.benlemlih@gmail.com
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="phone"

        0615016786
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="email_confirm"

        ayoub.benlemlih@gmail.com
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="passwd"


        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="account_type"

        0
        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="chosenVasId"


        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP
        Content-Disposition: form-data; name="chosenVAS"


        ------WebKitFormBoundaryvK2CBXmGBBLqBPsP--
        '''
        return scrapy.FormRequest(url="https://www2.avito.ma/ai/create/0",body=body,headers={'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryvK2CBXmGBBLqBPsP'},
                    callback=self.form)

    def form(self, response):
        self.logger.info(response.body)
        return
