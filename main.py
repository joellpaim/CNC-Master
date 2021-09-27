# -*- coding: utf-8 -*-

import os
import kivy
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar

kivy.require('1.9.1')

#Window.size = (360, 640)


# main app class for kaki app with kivymd modules
class CNCMasterApp(MDApp, App):


    DEBUG = 1 # set this to 0 make app not working

    # *.kv para acompanhar
    KV_FILES = {
        os.path.join(os.getcwd(), "screens/screenmanager.kv"),
        os.path.join(os.getcwd(), "screens/tela_inicio/telainicio.kv"),
        os.path.join(os.getcwd(), "screens/tela_brocas/telabrocas.kv"),
        os.path.join(os.getcwd(), "screens/tela_machos/telamachos.kv"),
        os.path.join(os.getcwd(), "screens/tela_insertos/telainsertos.kv"),
        
    }

    # classes para acompanhar dos arquivos *.py
    CLASSES = {
        "MainScreenManager": "screens.screenmanager",
        "TelaInicial": "screens.tela_inicio.telainicio",
        "TelaBrocas": "screens.tela_brocas.telabrocas",
        "TelaMachos": "screens.tela_machos.telamachos",
        "TelaInsertos": "screens.tela_insertos.telainsertos",
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]



    def build_app(self):
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.color_accent = "Cyan"
        self.theme_cls.theme_style = "Light"

        self.icon = 'assets/icone.png'
        self.title = 'CNC Master'
        #Mostra os FPS
        #self.fps_monitor_start()

        return Factory.MainScreenManager()

    def calcular(self):
        Snackbar(text="Funfou").open()




# finally, run the app
if __name__ == "__main__":
    CNCMasterApp().run()