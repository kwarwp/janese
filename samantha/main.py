from _spy.vitollino.main import Cena, Elemento, STYLE

FUNDO = "https://media.gazetadopovo.com.br/2019/10/31105652/star-wars-1724901_1920-960x540.jpg"
LIVRO = "https://i.pinimg.com/originals/3f/04/04/3f04040d3c0dabe712b06177bc8301b2.jpg"

STYLE["width"] = 900
STYLE["heigth"] = 900

class turmaDireita():

    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.livro = Elemento(LIVRO, texto = "Turma da direita :)", h=150, w=150, x=350, y=250, cena= self.fundo)
            
    def chama(self):
        self.fundo.vai()

if __name__ == "__main__":     
    turmaDireita().chama()