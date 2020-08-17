from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

FUNDO = "https://i.imgur.com/oGWvqFK.jpg"
LIVRO = "https://i.imgur.com/vJ7YP8N.png"

STYLE["width"] = 900
STYLE["heigth"] = 900


class Lago():

    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.pessoa = Elemento(LIVRO, texto = "O cenário é mesmo bonito!", h=150 , w=150, x=150, y=120)
        self.mais = Texto(self.fundo, txt = "Alguém está observando este cenário!", foi = self.mostra_pessoa) 
        
    def mostra_pessoa(self, *_ ):
        self.pessoa.entra(self.fundo)
        
    def chama(self):
        self.fundo.vai()
        self.mais.vai()

if __name__ == "__main__":
    Lago().chama()
        
