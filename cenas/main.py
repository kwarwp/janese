"""   Vitollino para Equipe UNESP 

.. codeauthor:: Equipe Suoygirls <supygirls@gmail.com>

.. version:: 20.01
     - Botões para cada tutorial;

"""
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
from cenas.imix import Inicial
#from cenas.ik import Passeio
from cenas.ik import Passeio

FUNDO = "https://img.freepik.com/vetores-gratis/fundo-branco-textura-elegante_23-2148415643.jpg?size=626&ext=jpg"

CALEND={"IMIX":"https://i.imgur.com/XmmzDHZ.png", 
        "IK":"https://i.imgur.com/9nieFUZ.png",
        "AKBAL":"XX",
        "KAN":"XX",
        "CHICCHAN":"XX",
        "CIMI":"XX",
        "MANIK":"XX",
        "LAMAT":"XX",
        "MALUC":"XX",
        "OC":"XX",
        "CHUEN":"XX",
        "EB":"XX",
        "AKBAL":"XX"
       }

STYLE["width"] = 900
STYLE["heigth"] = 900


class Estrutura():

    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.fundo.vai()
        """ Primeiro modo de criar um botão. Utiliza a função vai() do vitollino"""
        self.imix= Elemento(CALEND["IMIX"], tit="dia 17/08/2020", x=0, y=100, w=100, h=100, cena =self.fundo, vai=self.botao_17082020)
        """ Segundo modo de criar um botão"""
        self.ik= Elemento(CALEND["IK"], tit="dia 24/08/2020", x=150, y=100, w=100, h=100, cena =self.fundo)
        """Linka um evento a uma função através de uma keybind
           O 'elt' faz parte de um protocolo html do vitollino para anexar um elemento a outro
        """
        #self.ik.elt.bind("click", self.botao_24082020)
        
        self.ik.elt.onclick = self.botao_24082020 
        
    def botao_17082020(self, event=None):
        """ Função que será chamado no clique do IMIX"""
        Inicial().chama()
        
    def botao_24082020(self, event=None):
        """ Função que será chamado no clique do IK"""
        Passeio()

if __name__ == "__main__":        
    Estrutura()