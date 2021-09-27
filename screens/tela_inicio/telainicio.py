from kivymd.uix.screen import MDScreen
from kivmob import KivMob, TestIds
from kivy.uix.label import Label

class TelaInicial(MDScreen):


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

