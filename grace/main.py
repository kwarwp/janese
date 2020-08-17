from _spy.vitollino.main import Cena, Elemento, STYLE

FUNDO = "https://img.elo7.com.br/product/original/1D27E33/painel-cenario-mundo-encantado-frete-gratis-cenario.jpg"


class inicial():

    def __init__(self):
        self.fundo = Cena(FUNDO)
        
    def chama(self):
        self.fundo.vai()
        
inicial().chama()
        
