from kivymd.uix.screen import MDScreen
from kivmob import KivMob


class TelaInicial(MDScreen):


    APP = 'ca-app-pub-6991666817854079~5689719145'
    BANNER = 'ca-app-pub-6991666817854079/4184247549'

    def call(self):
        self.ads = KivMob('ca-app-pub-6991666817854079~5689719145')
        self.ads.new_banner('ca-app-pub-6991666817854079/4184247549', top_pos=False)
        self.ads.request_banner()
        self.ads.show_banner()


    def call2(self):
        self.ads.hide_banner()

