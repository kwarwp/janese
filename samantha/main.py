from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

FUNDO = "https://i.imgur.com/v7dtxen.jpg"
BONECO = "https://imgur.com/gfe9a1S.png"
INICIO = "https://i.imgur.com/hXur4Nv.png"

STYLE["width"] = 900
STYLE["heigth"] = 900

class inicio():
    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.zero = Elemento(INICIO, x=230, y=620, cena = self.fundo, vai = self.comeca)
        self.boneco = boneco(self.fundo, 1)
        self.cf = dict(A=0.8, B=-4)
        self.comeca()
    def comeca(self, *_):
        self.boneco.x = 200
        self.mais = Texto(self.fundo, txt = "Clique aqui", foi=self.foi,  A="-0.8", B="-4")
        self.mais.vai()
        
    def foi(self,opcao):
        self.boneco.a = self.cf [opcao]
        self.boneco.x = 200
        self.boneco.y = 620
        self.boneco.aparece()
        
    def vai(self):
        self.fundo.vai()
        
class boneco():
    def __init__(self, fundo, opcao1, opcao2):
        self.x = opcao
        ## self.b = 400
        self.c = 500
        self.a = 200
        y = self.a*self.x+self.c
        self.bonequinha = Elemento(BONECO, h=250 , w=250, x=self.x, y=y)
        self.bonequinha.o = 0
        self.bonequinha.y = self.a*self.x+self.c
        self.bonequinha.x = self.x
        self.bonequinha.vai = self.equacao1
        self.bonequinha.entra(fundo)
        
    def aparece(self):
        self.bonequinha.o = 1
        
    def equacao1(self,*_):
        self.bonequinha.x = self.x = self.x + 10
        self.bonequinha.y = self.a*self.x+self.c

if __name__ == "__main__":
	inicio().vai()