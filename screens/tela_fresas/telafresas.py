from kivymd.uix.screen import MDScreen
import math

class TelaFresas(MDScreen):

    def voltar_tela_inicial(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaInicial'

class TelaAvancoMesaF(MDScreen):
    pass

class TelaAvancoDenteF(MDScreen):
    pass

class TelaTorqueF(MDScreen):
    pass

class TelaVCF(MDScreen):

    def voltar_tela_fresas(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaFresas'

    def calcular(self):
        try:
            dm = float(self.ids.dm.text)
            n = float(self.ids.n.text)

            vc = ((dm * 3.14 * n) / 1000)

            if vc < 10000:
                self.ids.resultado.text = (f"{vc:.2f} m/min")
            else:
                self.ids.resultado.text = ("Dados fora da faixa")
        except:
            self.ids.resultado.text = '0.00 m/min'

class TelaVelFusoF(MDScreen):

    def voltar_tela_fresas(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaFresas'

    def calcular(self):
        try:
            vc = float(self.ids.vc.text)
            dm = float(self.ids.dm.text)

            n = ((vc * 1000) / (3.14 * dm))

            self.ids.resultado.text = (f"{n:.0f} rpm")
        except:
            self.ids.resultado.text = '0 rpm'

class TelaTaxaRemocaoF(MDScreen):

    def voltar_tela_fresas(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaFresas'

    def calcular(self):
        try:
            vc = float(self.ids.vc.text)
            ap = float(self.ids.ap.text)
            fn = float(self.ids.fn.text)

            q = (vc * ap * fn)

            self.ids.resultado.text = (f"{q:.2f} cm³/min")
        except:
            self.ids.resultado.text = '0.00 cm³/min'

class TelaPotenciaF(MDScreen):

    def voltar_tela_fresas(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaFresas'

    def calcular(self):
        try:
            vc = float(self.ids.vc.text)
            ap = float(self.ids.ap.text)
            fn = float(self.ids.fn.text)
            kc = float(self.ids.kc.text)

            pc = ((vc * ap * fn * kc)/(30 * (math.pow(10, 3))))

            self.ids.resultado.text = (f"{pc:.2f} kW")
        except:
            self.ids.resultado.text = '0.00 kW'

class TelaAvancoRotacaoF(MDScreen):

    def voltar_tela_fresas(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaFresas'

    def calcular(self):
        try:
            lm = float(self.ids.lm.text)
            fn = float(self.ids.fn.text)
            n = float(self.ids.n.text)

            tc = (lm / (fn * n))

            self.ids.resultado.text = (f"{tc:.2f} min")
        except:
            self.ids.resultado.text = '0.00 min'
