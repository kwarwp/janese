from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

FUNDO = "https://img.elo7.com.br/product/original/1D27E33/painel-cenario-mundo-encantado-frete-gratis-cenario.jpg"
LIVRO = "https://comunicamack.files.wordpress.com/2016/12/livro.png"

STYLE["width"] = 900
STYLE["heigth"] = 900


class inicial():

    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.livro = Elemento(LIVRO, texto = "Abra este livro!", h=150 , w=150, x=350, y=250)
        self.mais = Texto(self.fundo, txt = "Teste!", foi = self.mostra_livro) 
        
    def mostra_livro(self, *_ ):
        self.livro.entra(self.fundo)
        
    def chama(self):
        self.fundo.vai()
        self.mais.vai()
        
inicial().chama()
        
