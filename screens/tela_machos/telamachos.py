from kivymd.uix.screen import MDScreen

class TelaMachos(MDScreen):

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
                        vc = ((ve * 3.14 * dm) / 1000)
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
