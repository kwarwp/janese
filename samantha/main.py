# janese.samantha.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE

fundo = "https://www.google.com/url?sa=i&url=https%3A%2F%2Foglobo.globo.com%2Fcultura%2Fentenda-em-que-ordem-assistir-star-wars-a-cronologia-dos-filmes-24136182&psig=AOvVaw0ROUJDdxU6-ECOVaclCzKr&ust=1597793213656000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLjDquuxo-sCFQAAAAAdAAAAABAD"

STYLE["width"] = 900
STYLE["heigth"] = 900

class inicial():

      def _init_(self):
            self.fundo = Cena(FUNDO)
            
      def chama(self):
            self.fundo.vai()
            
inicial().chama()