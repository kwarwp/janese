from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

FUNDO = "https://imgur.com/cf9dvHG.png"
BONEQUINHA = "https://imgur.com/gfe9a1S.png"
INICIOMONTANHA = "https://imgur.com/hXur4Nv.png"

STYLE["width"] = 900
STYLE["heigth"] = 900


class inicialesquerda():
    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.zero = Elemento (INICIOMONTANHA, x=230 , y=620, cena=self.fundo, vai=self.comeca)
        self.bonequinha = bonequinha(self.fundo, 1)
        self.cf = dict(A=-1,3655, B=-4) 
        #self.planocartesiano = buscar uma imagem
        #self.bonequinha = bonequinha(self.fundo)
        self.comeca()
    def comeca(self, *_):
        self.bonequinha.x = 200
        self.mais = Texto(self.fundo, txt = "Clique aqui", foi=self.foi, A="-1,3655", B="-4")
        self.mais.vai()
       
        
    def foi(self,opcao):
        self.bonequinha.a = self.cf [opcao]
        self.bonequinha.x = 200
        self.bonequinha.y = 620
        self.bonequinha.aparece()
        #self.cf = dict(A = "(2,3)"
    def vai(self):
        self.fundo.vai()
               
class bonequinha():
    def __init__(self,fundo, opcao):
        self.x = 50
        self.c = 500
        self.a = opcao
        y = self.a*self.x+self.c
        self.boneca = Elemento(BONEQUINHA, h=250 , w=250, x=self.x, y=y)
        self.boneca.o = 0
        self.boneca.y = self.a*self.x+self.c
        self.boneca.x = self.x
        self.boneca.vai = self.equacao1
        self.boneca.entra(fundo)
        
    def aparece(self):
        self.boneca.o = 1
        
    def equacao1(self,*_):
        self.boneca.x = self.x = self.x -5,457
        self.boneca.y = self.a*self.x+self.c
        
    
if __name__ == "__main__":  
	inicialesquerda().vai()
        