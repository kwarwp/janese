from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

FUNDO = "https://imgur.com/cf9dvHG.png"
BONEQUINHA = "https://imgur.com/gfe9a1S.png"
INICIOMONTANHA = "https://imgur.com/hXur4Nv.png"

STYLE["width"] = 900
STYLE["heigth"] = 900


class inicialesquerda():
    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.zero = Elemento (INICIOMONTANHA, x=230 , y=620, cena=self.fundo)
        #self.planocartesiano = buscar uma imagem
        #self.bonequinha = bonequinha(self.fundo)
        self.mais = Texto(self.fundo, txt = "Clique aqui", foi=self.foi, A="3,5", B="-3,5")
        self.mais.vai()
        self.cf = dict(A=3.5, B=-3.5) 
        
    def foi(self,opcao):
        self.bonequinha = bonequinha(self.fundo, self.cf[opcao])
        #self.cf = dict(A = "(2,3)"
    def vai(self):
        self.fundo.vai()
               
class bonequinha():
    def __init__(self,fundo, opcao):
        self.boneca = Elemento(BONEQUINHA, texto = "Voe!", h=250 , w=250, x=100, y=400)
        self.x = 100
        self.c = 400
        self.a = opcao
        self.boneca.vai = self.equacao1
        self.boneca.entra(fundo)
        
    def equacao1(self,*_):
        self.boneca.x = self.x = self.x + 10 
        self.boneca.y = self.a*self.x+self.c
    
if __name__ == "__main__":  
	inicialesquerda().vai()
        