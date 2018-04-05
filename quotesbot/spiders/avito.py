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
        
        body = '''--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="body"



dddddddddddddddddddddddddddddddddddd

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="chosenVAS"



insertion

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="mileage"





--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="account_type"



0

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="email_confirm"



a.benlemlih@mgpap.org.ma

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="brand"





--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="price_meter"



0

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="pfiscale"





--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="price"



100 000

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="phone"



0615016786

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="chosenVasId"



62

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="rooms"





--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="images[]"; filename=""

Content-Type: application/octet-stream





--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="address"





--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="validate"



Déposez votre annonce »

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="mandatory_cv"



0

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="size"





--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="lang"



fr

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="name"



Ayoub

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="area"



154

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="category_group"



7010

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="regdate"





--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="email"



a.benlemlih@mgpap.org.ma

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="beds"





--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="passwd"



youssef2010

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="company_ad"



0

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="fuel"





--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="model"





--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="subject"



wwwwwwwwwwwwwwwwwwwwwwwwwwww

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="type"



s

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="region"



17

--d14317c588fc4e8894b25ef021714a40

Content-Disposition: form-data; name="images_urls[]"



2665577777.jpg

--d14317c588fc4e8894b25ef021714a40--
'''
        return scrapy.Request(url="https://www2.avito.ma/ai/create/0",method = 'POST',body = body,headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'content-type': 'multipart/form-data; boundary=d14317c588fc4e8894b25ef021714a40',  'origin': 'https://www2.avito.ma', 'referer': 'https://www2.avito.ma/ai/form/0', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'},
                                  callback=self.create,dont_filter=True)

    def create(self, response):
        self.logger.info(response.body)
        self.logger.info("headers create"+str(response.request.headers))
        self.logger.info("body create"+str(response.request.body))        
        return
