from kivymd.uix.screen import MDScreen
import math


class TelaBrocas(MDScreen):

    def limpar(self):
        self.ids.dm.text = ""
        self.ids.vc.text = ""
        self.ids.ve.text = ""
        self.ids.avre.text = ""
        self.ids.av.text = ""
        
    def calcular(self):
        try:
            
            
            dm = self.ids.dm.text
            try:
                dm = float(dm)
                print(f"{dm:.2f}")
            except:
                print("dm inválido")

                ve = self.ids.ve.text
                avre = self.ids.avre.text
                av = self.ids.av.text

                if av == "" and ve != "" and avre != "":
                    try:
                        avre = float(avre)
                        ve = float(ve)

                        av = (avre * ve)
                        self.ids.av.text = (f"{av:.0f}")
                    except:
                        print("av inválido")

                elif avre == "" and ve != "" and av != "":
                    try:
                        av = float(av)
                        ve = float(ve)

                        avre = (av / ve)
                        self.ids.avre.text = (f"{avre:.2f}")
                    except:
                        print("avre inválido")


            vc = self.ids.vc.text
            ve = self.ids.ve.text

            avre = self.ids.avre.text
            av = self.ids.av.text


            if vc == "":
                try:
                    ve = float(ve)

                    if ve >= 1:
                        vc = ((ve * 3.14 * dm)/1000)
                        self.ids.vc.text = (f"{vc:.0f}")

                except:
                    print("vc inválido")

            elif ve == "":
                try:
                    vc = float(vc)

                    if vc >= 1:
                        ve = ((vc * 318) / dm)
                        self.ids.ve.text = (f"{ve:.0f}")

                except:
                    print("ve inválido")

            elif av == "" and ve != "" and avre != "":
                try:
                    avre = float(avre)
                    ve = float(ve)

                    av = (avre * ve)
                    self.ids.av.text = (f"{av:.0f}")
                except:
                    print("av inválido")

            elif avre == "" and ve != "" and av != "":
                try:
                    av = float(av)
                    ve = float(ve)

                    avre = (av / ve)
                    self.ids.avre.text = (f"{avre:.2f}")
                except:
                    print("avre inválido")


            
        except Exception as e:
            print(f"Erro: {e}")

    def voltar_tela_inicial(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaInicial'



class TelaVC(MDScreen):

    def voltar_tela_brocas(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaBrocas'

    def calcular(self):
        try:
            dc = float(self.ids.dm.text)
            n = float(self.ids.ve.text)

            vc = ((dc*3.14*n)/1000)
            if vc < 10000:
                self.ids.resultado.text = (f"{vc:.2f} m/min")
            else:
                self.ids.resultado.text = ("Dados fora da faixa")
        except:
            self.ids.resultado.text = '0.00 m/min'

class TelaVelFuso(MDScreen):

    def voltar_tela_brocas(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaBrocas'

    def calcular(self):
        try:
            dc = float(self.ids.dm.text)
            vc = float(self.ids.vc.text)

            n = ((vc*1000)/(3.14*dc))

            self.ids.resultado.text = (f"{n:.0f} rpm")
        except:
            self.ids.resultado.text = '0 rpm'

class TelaTaxaPenetracao(MDScreen):

    def voltar_tela_brocas(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaBrocas'

    def calcular(self):
        try:
            fn = float(self.ids.fn.text)
            n = float(self.ids.n.text)

            vf = (fn * n)

            self.ids.resultado.text = (f"{vf:.0f} m/min")
        except:
            self.ids.resultado.text = '0 m/min'

class TelaAvancoRotacao(MDScreen):

    def voltar_tela_brocas(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaBrocas'

    def calcular(self):
        try:
            vf = float(self.ids.vf.text)
            n = float(self.ids.n.text)

            fn = (vf / n)

            self.ids.resultado.text = (f"{fn:.2f} mm/rot")
        except:
            self.ids.resultado.text = '0.00 mm/rot '

class TelaTaxaRemocaoMetal(MDScreen):

    def voltar_tela_brocas(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaBrocas'

    def calcular(self):
        try:
            dc = float(self.ids.dc.text)
            vc = float(self.ids.vc.text)
            fn = float(self.ids.fn.text)

            q = ((dc * fn * vc)/4)

            self.ids.resultado.text = (f"{q:.2f} cm³/min")
        except:
            self.ids.resultado.text = '0.00 cm³/min'

class TelaPotenciaLiquida(MDScreen):

    def voltar_tela_brocas(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaBrocas'

    def calcular(self):
        try:
            dc = float(self.ids.dc.text)
            vc = float(self.ids.vc.text)
            fn = float(self.ids.fn.text)
            kc = float(self.ids.kc.text)

            pc = ((fn * vc * dc * kc)/(240*(math.pow(10, 3))))

            self.ids.resultado.text = (f"{pc:.2f} kW")
        except:
            self.ids.resultado.text = '0.00 kW'

class TelaTorque(MDScreen):

    def voltar_tela_brocas(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaBrocas'

    def calcular(self):
        try:
            pc = float(self.ids.pc.text)
            n = float(self.ids.n.text)

            mc = ((pc * 30 * (math.pow(10, 3)))/(3.14 * n))

            self.ids.resultado.text = (f"{mc:.2f} Nm")
        except:
            self.ids.resultado.text = '0.00 Nm'

class TelaTempoUsinagem(MDScreen):

    def voltar_tela_brocas(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'TelaBrocas'

    def calcular(self):
        try:
            lm = float(self.ids.lm.text)
            vf = float(self.ids.vf.text)

            tc = (lm / vf)

            self.ids.resultado.text = (f"{tc:.2f} min")
        except:
            self.ids.resultado.text = '0.00 min'



            

                   