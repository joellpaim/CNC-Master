from kivymd.uix.screen import MDScreen
import math

class TelaMachos(MDScreen):

    def voltar_tela_inicial(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaInicial'

class TelaVelFusoR(MDScreen):

    def voltar_tela_machos(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaMachos'

    def calcular(self):
        try:
            vc = float(self.ids.vc.text)
            d = float(self.ids.d.text)

            n = ((vc*1000)/(3.14*d))

            self.ids.resultado.text = (f"{n:.0f} rpm")
        except:
            self.ids.resultado.text = '0 rpm'

class TelaFaixaAvancoR(MDScreen):

    def voltar_tela_machos(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaMachos'

    def calcular(self):
        try:
            p = float(self.ids.p.text)
            n = float(self.ids.n.text)

            vf = (p * n)

            self.ids.resultado.text = (f"{vf:.0f} mm/min")
        except:
            self.ids.resultado.text = '0 mm/min'

class TelaTorqueR(MDScreen):

    def voltar_tela_machos(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaMachos'

    def calcular(self):
        try:
            p = float(self.ids.p.text)
            d = float(self.ids.d.text)
            kc = float(self.ids.kc.text)

            md = ((math.pow(p, 2) * d * kc) / 8000)

            self.ids.resultado.text = (f"{md:.2f} Nm")
        except:
            self.ids.resultado.text = '0.00 Nm'

class TelaPotenciaR(MDScreen):

    def voltar_tela_machos(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaMachos'

    def calcular(self):
        try:
            md = float(self.ids.md.text)
            n = float(self.ids.n.text)

            p = ((md * 2 * 3.14 * n) / 60)

            self.ids.resultado.text = (f"{p:.0f} kW")
        except:
            self.ids.resultado.text = '0 kW'
