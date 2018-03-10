import Crawler
from kivy.uix.screenmanager import Screen 

# TODO: Will need some validation and should not pass the user if the username/password is incorrect.
class LoginScreen(Screen):
    def set_crawl(self, crawl):
        self.crawl = crawl
            
    def login(self):
        Crawler.Spider.user = self.ids.input_username.text
        Crawler.Spider.passw = self.ids.input_password.text
        self.manager.current = 'grades'
        
        