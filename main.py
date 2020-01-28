from kivy.app  import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.garden.mapview import MapView
from kivy.garden.mapview import MapMarkerPopup

class MyWin(MapView):
    pass

class MainApp(App):
    def build(self):
        return MyWin()


if __name__ == "__main__":
    MainApp().run()