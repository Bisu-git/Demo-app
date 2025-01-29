from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty

class ListWidget(RecycleView):
    
    def update(self):
        self.data = [{'text': str(item)} for item in self.items]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.items = []

class RootWidget(BoxLayout):
    inputbutton = ObjectProperty(None)
    inputcontent = ObjectProperty(None)
    outputcontent = ObjectProperty(None)

    def add_item(self):

        if self.inputcontent.text.strip():
            formatted = f'. {self.inputcontent.text.strip()}'
            self.outputcontent.items.append(formatted)
            self.outputcontent.update()
            self.inputcontent.text = ""

class ProjectApp(App):
    def build(self):
        return RootWidget()

ProjectApp().run()