from kivy.app  import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.garden.mapview import MapView
from kivy.garden.mapview import MapMarkerPopup
from kivy.uix.button import ButtonBehavior
from kivy.uix.stacklayout import StackLayout
from kivy.uix.dropdown  import DropDown
from kivy.uix.image import Image
from kivy.uix.button import Button
#from drops import SearchTool
#from kivy.utils import utils
#import kivy.utils as utils

# Builder.load_string( """
# <MainDrop>:
#     canvas.before:
#         Color:
#             rgb: utils.get_color_from_hex("#35477d")
#         Rectangle:
#             size:self.size
#             pos:self.pos
#     CustomButton: 
#         text: 'Schools in Angola'
#         size_hint_y: None
#         height: 44
#         on_release:root.select('Schools in Angola')
#     CustomButton: 
#         text: 'Hospital in Angola'
#         size_hint_y: None
#         height: 44
#         on_release:root.select('Hospital in Angola')
        
#     CustomButton: 
#         text: 'Christian Churches'
#         size_hint_y: None
#         height: 44
#         on_release: root.select('Christian Churches')"""
# )
class MainDrop(DropDown):
    pass
class HomeScreen(Screen):
    pass

class DropButton(ButtonBehavior,Image):
    pass
class SchoolScreen(Screen):
    pass



class SearchButton(ButtonBehavior,Image):
    pass
class HospitalScreen(Screen):
    pass

class SupermarketScreen(Screen):
    pass

class SearchTool(Screen):
    pass
    # def __init__(self, **kwargs):
    #     super(SearchTool,self).__init__(**kwargs)
    #     self.maindrop=MainDrop()
    #     self.dorpoption=DropButton(source="images/001_12.png", size=[80,25],size_hint_x=None, size_hint_y=None,pos=(30,0))
    #     self.add_widget(self.dorpoption)
    #     self.dorpoption.bind(on_release=self.maindrop.open)

    # def novoas(self):
    #     self.maindrop.add_widget(Button(text="RREIDELAS", size=[20,20]))
    #     #(50, 810) size_hint_x=None, size_hint_y=None


main_kv=Builder.load_file("main.kv")

class MainApp(App):

    def build(self):
        return main_kv


if __name__ == "__main__":
    MainApp().run()