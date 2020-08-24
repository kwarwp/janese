from _spy.vitollino.main import Cena, Elemento, STYLE, texto

FUNDO = "https://images-americanas.b2w.io/produtos/01/00/img4/184202/8/184202888_1GG.jpg"


CALEND={"IMIX":"https://i.imgur.com/XmmzDHZ.png", 
        "IK":"https://i.imgur.com/9nieFUZ.png",
        "AKBAL":"XX",
        "KAN":"XX",
        "CHICCHAN":"XX",
        "CIMI":"XX",
        "MANIK":"XX",
        "LAMAT":"XX",
        "MALUC":"XX",
        "OC":"XX",
        "CHUEN":"XX",
        "EB":"XX",
        "AKBAL":"XX"
       }

STYLE["width"] = 900
STYLE["heigth"] = 900

class turmadaDireita():

     def __init__(self):
    
        self.fundo=Cena(FUNDO)
        self.fundo.vai()
        
        self.imix=Elemento(CALEND["IMIX"], tit="dia 17/08/2020", x=0, y=100, w=100, h=100, cena=self.fundo, vai=botao_17082020)
        
        def botao_17082020(self, event=None):
            Inicial().chama()
            
if __name__ == "__main__":
    turmadaDireita()