from kivymd.uix.screen import MDScreen
from kivmob import KivMob
from kivy.uix.label import Label

from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout

from kivy.properties import ListProperty, StringProperty
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.toast import toast
from kivy.uix.widget import Widget
from kivymd.uix.list import (
    ILeftBody,
    IRightBodyTouch,
    OneLineAvatarListItem,
    OneLineIconListItem,
    TwoLineAvatarListItem,
)


from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation


#Classes

class CNCMOneLineLeftAvatarItem(OneLineAvatarListItem):
    divider = None
    source = StringProperty()

class CNCMTwoLineLeftAvatarItem(TwoLineAvatarListItem):
    icon = StringProperty()
    secondary_font_style = "Caption"

class CNCMTwoLineLeftIconItem(TwoLineAvatarListItem):
    icon = StringProperty()

class CNCMOneLineLeftIconItem(OneLineAvatarListItem):
    icon = StringProperty()

class CNCMOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()

class CNCMOneLineLeftWidgetItem(OneLineAvatarListItem):
    color = ListProperty()

class LeftWidget(ILeftBody, Widget):
    pass

class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass

class TelaInicial(MDScreen):

    #Informações para ADS
    APP = 'ca-app-pub-6991666817854079~5689719145'
    BANNER = 'ca-app-pub-6991666817854079/4184247549'

    def call(self):
        self.ads = KivMob(self.APP)
        self.ads.new_banner(self.BANNER, top_pos=False)
        self.ads.request_banner()
        self.ads.show_banner()
        return Label(text='Banner Ad Demo')

    def call2(self):
        self.ads.hide_banner()

    def voltar(self):
        self.manager.transition.direction = 'right'
        self.ids.screen_manager.current = 'scr 1'

    def switch_callback(self, switchObject, switchValue):

        # Switch value are True and False
        if (switchValue):
            toast('Modo Polegada')
        else:
            toast('Modo MM')



class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()




