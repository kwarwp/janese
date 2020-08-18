# janese.danae.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE

FUNDO = "https://i.imgur.com/aisVckn.jpg"
LIVRO = "https://i.imgur.com/vJ7YP8N.png"

STYLE["width"] = 900
STYLE["heigth"] = 900

class Lago():

    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.livro = Elemento(LIVRO, texto = "Turma da direita :)", h=150, w=150, x=350, y=250, cena= self.fundo)
            
    def chama(self):
        self.fundo.vai()
            
turmaDireita().chama()