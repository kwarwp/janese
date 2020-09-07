from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

FUNDO = "https://imgur.com/cf9dvHG.png"
BONEQUINHA = "https://imgur.com/Z8SiiTg.png"

STYLE["width"] = 900
STYLE["heigth"] = 900


class inicialesquerda():

    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.bonequinha = bonequinha(self.fundo)
        self.mais = Texto(self.fundo, txt = "Clique aqui") 
        
         
    def vai(self):
        self.fundo.vai()
               
class bonequinha():
    def __init__(self,fundo):
        self.boneca = Elemento(BONEQUINHA, texto = "Voe!", h=150 , w=250, x=50, y=200)
        self.x = 50
        self.c = 200
        self.boneca.vai = self.equacao1
        self.boneca.entra(fundo)
        
    def equacao1(self,*_):
        self.boneca.x = self.x = self.x+10
        self.boneca.y = self.x*2+self.c
    
if __name__ == "__main__":  
	inicialesquerda().vai()
        