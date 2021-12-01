import json

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

class MainScreenManager(ScreenManager):

    previous_screen = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self._goto_previous_screen)
        # getting screens data from screens.json
        with open("screens.json") as f:
            self.screens_data = json.load(f)

    def set_current(self, screen_name, side="left"):
        """
        If you need to use more screens in your app,
        Create your screen files like below:
            1. Create screen_file.py in libs/uix/baseclass/
            2. Create screen_file.kv in libs/uix/kv/
            3. Add the screen details in screens.json like below:
                {
                    ...,
                    "screen_name": {
                        "import": "from libs.uix.baseclass.screen_py_file import ScreenObjectName",
                        "object": "ScreenObjectName()",
                        "kv": "libs/uix/kv/screen_kv_file.kv"
                    }
                }

                Note: In .JSON you must not use:
                        * Unneeded Commas
                        * Comments
        """

        # checa se a tela ja foi adicionada ao Screenmanager
        if not self.has_screen(screen_name):
            screen = self.screens_data[screen_name]
            # carrega o arquivo kv
            Builder.load_file(screen["kv"])
            # importa a classe da tela dinamicamente
            exec(screen["import"])
            # calls the screen class to get the instance of it
            screen_object = eval(screen["object"])
            # automatically sets the screen name using the arg that passed in set_current
            screen_object.name = screen_name
            # Finalmente adiciona a tela para o Screenmanager
            self.add_widget(screen_object)

        # Salva a informação da ultima tela
        self.previous_screen = {"name": self.current, "side": side}
        # Configura a direção da transição
        self.transition.direction = side
        # sets to the current screen
        self.current = screen_name

    def _goto_previous_screen(self, instance, key, *args):
        if key == 27:
            self.goto_previous_screen()
            return True

    def goto_previous_screen(self):
        #print(self.previous_screen)
        #print(self.current)
        if self.previous_screen:
            if self.current == "TelaInicial":
                #print('sair')
                exit()
            else:
                self.set_current(
                    self.previous_screen["name"],
                    side="right" if self.previous_screen["side"] == "left" else "left",
                )
                self.previous_screen = None
        else:
            self.set_current("TelaInicial", "right")


