from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.garden.mapview import MapView, MapMarkerPopup
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.chip import MDChip 
from kivy.uix.button import Button
from kivymd.uix.button  import MDRectangleFlatIconButton, MDFillRoundFlatIconButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
import fiona as f
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.properties import StringProperty
from kivymd.uix.list import ILeftBody, OneLineAvatarListItem
from kivymd.uix.list import OneLineAvatarListItem

# from kivy.config import Config
# Config.set('kivy','window_icon','path/to/icon.ico')

class NavigationItem(OneLineAvatarListItem):
    icon = StringProperty()

class CustomNavigationDrawerIconButton(OneLineAvatarListItem):
    source = StringProperty()

    def _set_active(self, active, nav_drawer):
        pass

class ContentNavigationDrawer(BoxLayout):
    pass

class Tools(BoxLayout):
    pass 
class SearchButton(ButtonBehavior,Image):
    pass
class MainApp(MDApp):
    def build(self):
        self.title="Angola Map"
        return Builder.load_file("luanda_map.kv")
       
    def on_start(self):
        pass
        #print("esssss")
        # files=f.open("C:/Users/emcfm/Downloads/Angola/gis_osm_pois_free_1.shp")
        # for s in files:
        #     if s["properties"]["fclass"].lower()=="hospital" or s["properties"]["fclass"].lower()=="doctors":
            
        #         box=MDFillRoundFlatIconButton(text="Class Name: {}\nName: {}\nCordinates: {} , {}".format(s["properties"]["fclass"],
        #         s["properties"]["name"],s["geometry"]['coordinates'][1],s["geometry"]['coordinates'][0]), 
        #         md_bg_color=[0,0,0,1], text_color=[0,0,0,1],size_hint=(None, 1),width=200, icon='hospital')
             
        #         marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
        #         marks.add_widget(box)
        #         self.root.ids.maps_hos.add_widget(marks)

        #     elif s["properties"]["fclass"].lower()=="school" or s["properties"]["fclass"].lower()=="university" or s["properties"]["fclass"].lower()=="college":
        #         marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
        #         box=MDFillRoundFlatIconButton(text="Class Name: {}\nName: {}\nCordinates: {} , {}".format(s["properties"]["fclass"],
        #         s["properties"]["name"],s["geometry"]['coordinates'][1],s["geometry"]['coordinates'][0]), 
        #         md_bg_color=[0,0,0,1], text_color=[0,0,0,1],size_hint=(None, 1),width=200, icon='school')
             
        #         marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
        #         marks.add_widget(box)
        #         self.root.ids.maps_sch.add_widget(marks)

        #     elif s["properties"]["fclass"].lower()=="bank":
        #         marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
        #         box=MDFillRoundFlatIconButton(text="Class Name: {}\nName: {}\nCordinates: {} , {}".format(s["properties"]["fclass"],
        #         s["properties"]["name"],s["geometry"]['coordinates'][1],s["geometry"]['coordinates'][0]), 
        #         md_bg_color=[0,0,0,1], text_color=[0,0,0,1],size_hint=(None, 1),width=200, icon='bank')
             
        #         marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
        #         marks.add_widget(box)
        #         self.root.ids.maps_ban.add_widget(marks)

        #     elif s["properties"]["fclass"].lower()=="supermarket" or s["properties"]["fclass"].lower()=="department_store":
        #         marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
        #         box=MDFillRoundFlatIconButton(text="Class Name: {}\nName: {}\nCordinates: {} , {}".format(s["properties"]["fclass"],
        #         s["properties"]["name"],s["geometry"]['coordinates'][1],s["geometry"]['coordinates'][0]), 
        #         md_bg_color=[0,0,0,1], text_color=[0,0,0,1],size_hint=(None, 1),width=200, icon='store')
             
        #         marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
        #         marks.add_widget(box)
        #         self.root.ids.maps_com.add_widget(marks)

        #     elif s["properties"]["fclass"].lower()=="hotel":
        #         marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
        #         box=MDFillRoundFlatIconButton(text="Class Name: {}\nName: {}\nCordinates: {} , {}".format(s["properties"]["fclass"],
        #         s["properties"]["name"],s["geometry"]['coordinates'][1],s["geometry"]['coordinates'][0]), 
        #         md_bg_color=[0,0,0,1], text_color=[0,0,0,1],size_hint=(None, 1),width=200, icon='city')
             
        #         marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
        #         marks.add_widget(box)
        #         self.root.ids.maps_hou.add_widget(marks)
    def reis(self):
        print("yes") 

if __name__ == "__main__":
    MainApp().run()