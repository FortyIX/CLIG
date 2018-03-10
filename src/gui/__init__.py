from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from gui.LoginScreen import LoginScreen
from gui.GradesScreen import GradesScreen

class KeatsApp(App):
    def set_crawl(self, crawl):
        self.crawl = crawl

    # TODO: find a way to evade passing the crawler to every screen. Use a singleton?
    def build(self):
        self.sm = ScreenManager()
        login = LoginScreen(name='login')
        login.set_crawl(self.crawl)

        grades = GradesScreen(name='grades')
        grades.set_crawl(self.crawl)

        self.sm.add_widget(login)
        self.sm.add_widget(grades)

        return self.sm


if __name__ == '__main__':
    KeatsApp().run()




