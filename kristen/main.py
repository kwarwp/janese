from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

FUNDO = "https://imgur.com/cf9dvHG.png"
BONEQUINHA = "https://imgur.com/gfe9a1S.png"

STYLE["width"] = 900
STYLE["heigth"] = 900


class inicialesquerda():
    def __init__(self):
        self.fundo = Cena(FUNDO)
        #self.bonequinha = bonequinha(self.fundo)
        self.mais = Texto(self.fundo, txt = "Clique aqui", foi=self.foi, A="10", B="20")
        self.mais.vai()
        self.cf = dict(A=10, B=20) 
    def foi(self,opcao):
        self.bonequinha = bonequinha(self.fundo, self.cf[opcao])
         
    def vai(self):
        self.fundo.vai()
               
class bonequinha():
    def __init__(self,fundo, opcao):
        self.boneca = Elemento(BONEQUINHA, texto = "Voe!", h=250 , w=250, x=50, y=200)
        self.x = 50
        self.c = 200
        self.a = opcao
        self.boneca.vai = self.equacao1
        self.boneca.entra(fundo)
        
    def equacao1(self,*_):
        self.boneca.x = self.x+10
        self.boneca.y = self.a*self.x+self.c
    
if __name__ == "__main__":  
	inicialesquerda().vai()
        