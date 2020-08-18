from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

FUNDO = "https://macmagazine.uol.com.br/wp-content/uploads/2015/04/16-floresta.jpg"
LIVRO = "https://oamor.com.br/wp-content/uploads/2018/12/Quando-a-borboleta-rompe-o-casulo-2-830x450.jpg"

STYLE["width"] = 900
STYLE["heigth"] = 900


class inicialesquerda():

    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.livro = Elemento(LIVRO, texto = "Voe!", h=350 , w=350, x=150, y=250)
        self.mais = Texto(self.fundo, txt = "Clique aqui", foi = self.mostra_livro) 
        
    def mostra_livro(self, *_ ):
        self.livro.entra(self.fundo)
        
    def chama(self):
        self.fundo.vai()
        self.mais.vai()
        
inicialesquerda().chama()
        