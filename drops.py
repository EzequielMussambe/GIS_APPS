

from kivy.uix.screenmanager import Screen
from kivy.uix.dropdown  import DropDown

class MainDrop(DropDown):
    pass
class SearchTool(Screen):
        def __init__(self, **kwargs):
            super(SearchTool,self).__init__(**kwargs)
            self.maindrop=MainDrop()
            self.dorpoption=DropButton(source="images/001_12.png", size=[28,29],size_hint_x=None, size_hint_y=None,pos=(60,0))
            #(50, 810)
            self.add_widget(self.dorpoption)
            self.dorpoption.bind(on_release=self.maindrop.open)
