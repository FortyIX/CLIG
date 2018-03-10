from kivy.uix.screenmanager import Screen 
from kivy.uix.listview import ListItemButton
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.logger import Logger

items = [
    {"name": "PPA", "grade": "-"},
    {"name": "4CCS1PL1 Electronics Application Project and Engineering Lab I(17~18 000001)", "grade": "-"},
    {"name": "4CCS1PPA Programming Practice and Applications(17~18 000001)", "grade": "78.2"}
]

class GradesListButton(ListItemButton):
    pass

class MyViewClass(RecycleDataViewBehavior, BoxLayout):
    name = StringProperty("")
    grade = StringProperty("")
    index = None

    def set_state(self, state, app):
        self.parent.parent.data[self.index]['selected'] = state

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(MyViewClass, self).refresh_view_attrs(rv, index, data)



class GradesScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.Grades = []
        self.Modules = []

    def set_crawl(self, crawl):
        self.crawl = crawl

    def modules(self):
        if len(self.Modules) == 0:
            self.Modules = []

            for i in range(0, len(self.crawl.scanner.getCourse())):
                name = self.crawl.scanner.getCourse()[i]
                if name is not None :
                    self.Modules.append({"name": name, "grade": ""})

        self.ids.grades.data = self.Modules
        pass

    def grades(self):
        if len(self.Grades) == 0:
            self.Grades = []

            for i in range(0, len(self.crawl.scanner.getCourse())):
                name = self.crawl.scanner.getGradeTitle()[i]
                grade = self.crawl.scanner.getGradeMarks()[i]
                if name is not None and grade is not None:
                    self.Grades.append({"name": name, "grade": grade})

        self.ids.grades.data = self.Grades


    def on_enter(self):
        self.ids.grades.data = items

        # TODO: make this call asynchronous, as now it hangs the UI. Because there are no thread is python.
        self.crawl.startCrawling()

        self.modules()
        Logger.info(self.grades)

