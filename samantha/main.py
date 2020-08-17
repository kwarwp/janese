# janese.samantha.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE

FUNDO = "https://media.gazetadopovo.com.br/2019/10/31105652/star-wars-1724901_1920-960x540.jpg"
LIVRO = ""

STYLE["width"] = 900
STYLE["heigth"] = 900

class direita():

      def _init_(self):
            self.fundo = Cena(FUNDO)
            
      def chama(self):
            self.fundo.vai()
            
inicial().chama()