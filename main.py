import scrapy
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor



from loginform import fill_login_form


class keats(scrapy.Spider):



    name = 'login'
    start_urls = ['https://login-keats.kcl.ac.uk/']
    user="<required>"
    passw="<required>"
    list_1=[]

    def parse(self, response):

        args, url, method = fill_login_form(response.url, response.body, self.user, self.passw)

        return scrapy.FormRequest(url, method=method, formdata=args, callback=self.after_login)

    def after_login(self, response):

            for tab in response.css('div[id*="course"]'):
                PATH = '.title a::text'

                self.list_1.append(tab.css(PATH).extract_first())

           # self.showThings()

    def getList(self):
        return self.list_1



    def setInfo(self , ac , pas):
        self.user=ac
        self.passw=pas

    def getAc(self):
        return self.user
