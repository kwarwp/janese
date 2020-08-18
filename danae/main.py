# janese.danae.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE

FUNDO = "https://i.imgur.com/aisVckn.jpg"
LIVRO = "https://i.imgur.com/vJ7YP8N.png"

STYLE["width"] = 900
STYLE["heigth"] = 900

class Lago():

    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.livro = Elemento(LIVRO, texto = "Olhado tudo com atenção!)", h=150, w=150, x=550, y=120, cena= self.fundo)
            
    def vai(self):
        self.fundo.vai()

if __name__ == "__main__":
    Lago().vai()