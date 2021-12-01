# -*- coding: utf-8 -*-
# google.com, , DIRECT, f08c47fec0942fa0
# ca-app-pub-6991666817854079~5689719145
# ca-app-pub-6991666817854079/4184247549
# from kivy.config import Config
# Config.set('kivy', 'keyboard_mode', 'systemanddock')
# Config.set("kivy", "keyboard_mode", 'dock')

from kaki.app import App
from kivmob import KivMob
from kivy.core.window import Window
from kivy.uix.modalview import ModalView
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from kivymd.color_definitions import colors, palette
from kivymd.theming import ThemableBehavior
from kivymd.toast import toast
from kivymd.uix.snackbar import Snackbar
from screens.screenmanager import MainScreenManager
from random import randint
import pickle

Window.size = (1080 / 3, 1920 / 3)


class CNCMBaseDialog(ThemableBehavior, ModalView):
    pass


class CNCMDialogChangeTheme(CNCMBaseDialog):
    def set_list_colors_themes(self):
        for name_theme in palette:
            self.ids.rv.data.append(
                {
                    "viewclass": "CNCMOneLineLeftWidgetItem",
                    "color": get_color_from_hex(colors[name_theme]["500"]),
                    "text": name_theme,
                }
            )


class CNCFactorFreeApp(MDApp, App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        try:

            with open('data.json', 'rb') as fp:
                data = pickle.load(fp)

            self.theme_cls.primary_palette = data['Tema']

        except:

            my_dict = {"Tema": "BlueGray"}
            with open('data.json', 'wb') as fp:
                pickle.dump(my_dict, fp)

            with open('data.json', 'rb') as fp:
                data = pickle.load(fp)

            self.theme_cls.primary_palette = data['Tema']


        # ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green',
        # 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        self.theme_cls.color_accent = "Gray"
        self.theme_cls.theme_style = "Dark"
        self.dialog_change_theme = None
        self.icon = 'assets/Factor Logo.png'
        self.title = 'CNC Factor'



    def build(self):

        # Mostra os FPS
        # self.fps_monitor_start()

        self.root = MainScreenManager()
        self.root.set_current("TelaInicial")

        self.ads = KivMob('ca-app-pub-6991666817854079~6380597630')
        self.ads.new_banner("ca-app-pub-6991666817854079/7910135874", top_pos=False)
        self.ads.request_banner()
        self.ads.show_banner()



    def em_breve(self):
        Snackbar(text="Em desenvolvimento").open()

    def switch_theme_style(self, switchObject, switchValue):

        if (switchValue):

            self.theme_cls.theme_style = (
                "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
            )
            tema = self.theme_cls.theme_style
            toast(f"Tema {tema}")

        else:

            self.theme_cls.theme_style = (
                "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
            )
            tema = self.theme_cls.theme_style
            toast(f"Tema {tema}")

    def show_dialog_change_theme(self):
        if not self.dialog_change_theme:
            self.dialog_change_theme = CNCMDialogChangeTheme()
            self.dialog_change_theme.set_list_colors_themes()
        self.dialog_change_theme.open()

    def trocar_tema(self):
        temas = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green',
        'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']

        tema = randint(0, len(temas[:])-1)

        self.theme_cls.primary_palette = temas[tema]

        my_dict = {"Tema": f"{temas[tema]}"}
        with open('data.json', 'wb') as fp:
            pickle.dump(my_dict, fp)



# finally, run the app
if __name__ == "__main__":
    CNCFactorFreeApp().run()
