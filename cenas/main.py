"""   Vitollino para Equipe UNESP 

.. codeauthor:: Equipe Suoygirls <supygirls@gmail.com>

.. version:: 20.01
     - Botões para cada tutorial;

"""
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
from cenas.imix import Inicial
#from cenas.ik import nome_a_definir__

FUNDO = "https://img.freepik.com/vetores-gratis/fundo-branco-textura-elegante_23-2148415643.jpg?size=626&ext=jpg"

CALEND={IMIX:"https://i.imgur.com/XmmzDHZ.png", 
            IK:"https://i.imgur.com/9nieFUZ.png",
           }

STYLE["width"] = 900
STYLE["heigth"] = 900


class Estrutura():

    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.fundo.vai()
        
        self.imix= Elemento(IMIX, tit="dia 17/08/2020", x=0, y=0, w=300, h=300, cena =self.fundo, vai=self.botao_17082020)
         
    def botao_17082020(self, event=None):
        """ Método que será chamado no clique do IMIX"""
        Inicial().chama()
        
    def botao_24082020(self, *_ ):
        """ Método que será chamado no clique do IK"""
        pass

        
if __name__ == "__main__":        
    Estrutura()