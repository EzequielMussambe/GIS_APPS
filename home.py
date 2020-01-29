from kivy.app  import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.garden.mapview import MapView
from kivy.garden.mapview import MapMarkerPopup

class HomeScreen(Screen):
    pass

class SearchTool(Screen):
    pass
class SchoolScreen(Screen):
    pass

class HospitalScreen(Screen):
    pass

class SupermarketScreen(Screen):
    pass

main_kv=Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        return main_kv


if __name__ == "__main__":
    MainApp().run()