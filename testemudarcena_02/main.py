# janese.testemudarcena_02.main.py
# janese.anda_bonecoo.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

PERSONAGEM = "https://imgur.com/gfe9a1S.png"
FUNDO = "https://imgur.com/vqBDMtH.jpg"
JOYSTICK_FALSO = "https://imgur.com/KiYDtv2.png"
MARCADOR_X = "https://imgur.com/kJ2MkuK.png"
MARCADOR_ESQUERDA = "https://imgur.com/hEF8XPG.png"
MARCADOR_DIREITA = "https://imgur.com/hEF8XPG.png"
MARCADOR_CIMA = "https://imgur.com/hEF8XPG.png"
MARCADOR_BAIXO = "https://imgur.com/hEF8XPG.png"


STYLE["width"] = 900
STYLE["heigth"] = 900


def teste():
    fundo = Cena(FUNDO) 
    fundo.vai()
    bonequinha = Persona_control( fundo) 
        
class Persona_control:
    """ Cria um elemento que anda a partir do clique no joystick
    
        self.nome_do_elemento = Persona_control( nome_do_fundo)
        
        :param nome_do_fundo: Insere o personagem em um fundo pré-criado
        
    """
    def __init__(self, nome_do_fundo):
        self.x = 10 # valor pré-estabelecido do x
        self.y = 430 # valor pré-estabelecido do y
        
        self.persona = Elemento(PERSONAGEM, h=100 , w=100, x=self.x, y=self.y) # cria Elemento 
        self.persona.entra(nome_do_fundo) # utiliza o método entra() da classe Elemento para não ter que criar um atributo cena para a classe persona_control 
        
        #self.persona.x = self.x
        #self.persona.y = self.y
        
        self.joystickfalso = Elemento(JOYSTICK_FALSO, h=150 , w=150, x=720, y=420) #cria um elemento posicionado 'acima' no joystick
        self.joystickfalso.entra(nome_do_fundo)
        
        self.marcadorx = Elemento(MARCADOR_X, h=70 , w=70, x=80, y=450) #cria um elemento posicionado 'acima' no joystick
        self.marcadorx.entra(nome_do_fundo)
        
        self.cima = Elemento(MARCADOR_CIMA, h=40 , w=40, x=780, y=450, vai=self.anda_cima) #cria um elemento posicionado 'acima' no joystick
        self.cima.entra(nome_do_fundo)
        
        self.baixo = Elemento(MARCADOR_BAIXO, h=40 , w=40, x=780, y=530, vai=self.anda_baixo) #cria um elemento posicionado 'abaixo' no joystick
        self.baixo.entra(nome_do_fundo)
        
        self.direita = Elemento(MARCADOR_DIREITA, h=40 , w=40, x=720, y=490,vai=self.anda_direita) #cria um elemento posicionado 'à direita' no joystick
        self.direita.entra(nome_do_fundo)
        
        self.esquerda = Elemento(MARCADOR_ESQUERDA, h=40 , w=40, x=840, y=490, vai=self.anda_esquerda) #cria um elemento posicionado 'à esquerda' no joystick
        self.esquerda.entra(nome_do_fundo)

    def anda_direita(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'direita' é clicado.
        """
        self.persona.x = self.x = self.x - 10
        #self.persona.x = self.x - 10 > Deixar para averiguações posteriores
        #self.persona.x = self.x -= 10 > Deixar para averiguações posteriores
        
    def anda_esquerda(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'esquerda' é clicado.
        """
        self.persona.x = self.x = self.x + 10
        
    def anda_cima(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'em cima' é clicado.
        """
        self.persona.y = self.y = self.y - 10
        
    def anda_baixo(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'embaixo' é clicado.
        """
        self.persona.y = self.y = self.y + 10

if __name__ == "__main__":  
    teste()