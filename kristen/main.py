from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

FUNDO = "https://imgur.com/cf9dvHG.png"
BONEQUINHA = "https://imgur.com/Z8SiiTg.png"

STYLE["width"] = 900
STYLE["heigth"] = 900


class inicialesquerda():

    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.a = Texto(self.fundo, txt = "Clique aqui", A="10", B="20", C="30") 
        self.a.vai()
        self.bonequinha = bonequinha(self.fundo, self.a)
        
        
         
    def vai(self):
        self.fundo.vai()
               
class bonequinha():
    def __init__(self,fundo,a):
        self.boneca = Elemento(BONEQUINHA, texto = "Voe!", h=150 , w=250, x=200, y=300)
        self.x = 200
        self.c = 300
        self.a = a
        self.boneca.vai = self.equacao1
        self.boneca.entra(fundo)
        
    def equacao1(self,*_):
        self.boneca.x = self.x = self.x+10
        self.boneca.y = self.a+self.c
    
if __name__ == "__main__":  
	inicialesquerda().vai()
        