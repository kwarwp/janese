# janese.adda.main.py
#Bianca
#Ada Lovelace

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document

FUNDO = "https://i.imgur.com/KYKStgT.png"
PERSONAGEM = "https://imgur.com/E6lSl7l.gif"
PERSONAGEM1= "https://imgur.com/A6wdCYS.gif"
FOLHA = "https://i.imgur.com/upAN1GX.png"
PENA = "https://i.imgur.com/916QFLA.png"
MARCADOR_PROXIMO = "https://imgur.com/B9njEbl.png"
#MARCADOR_X = "https://imgur.com/kJ2MkuK.png"
MARCADOR_DIREITA = "https://imgur.com/GTnLEnS.png"
MARCADOR_ESQUERDA = "https://imgur.com/Nl7Qy9h.png"
MARCADOR_CIMA = "https://imgur.com/f2zfcvx.png"
MARCADOR_BAIXO = "https://imgur.com/QDx4zgx.png"
MARCADOR_PLAY = "https://i.imgur.com/qEbkWNJ.png"
#fase um
FUNDO_CENA1 = "https://i.imgur.com/kJBS3k9.jpg"
FUNDO_CENA2 = "https://imgur.com/wlXw3Xq.jpg"

#fase dois
FUNDO_CENA5 = "https://i.imgur.com/eQGB5Yi.jpg"
FUNDO_CENA6 = "https://imgur.com/BEyvnvd.jpg"

#fase 3
FUNDO_CENA11 = "https://i.imgur.com/EBbuTmf.jpg"
FUNDO_CENA12 = "https://imgur.com/XQhy1Yo.jpg"





STYLE["width"]=1350
STYLE["height"]=700

def teste():
    fundo = Cena(FUNDO_CENA2) 
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
        
        self.c11 = Cena(FUNDO_CENA1)
        self.c12 = Cena(FUNDO_CENA2)
        self.c13 = Cena(FUNDO_CENA3)
        self.c14 = Cena(FUNDO_CENA4)

        self.c21 = Cena(FUNDO_CENA5)
        self.c22 = Cena(FUNDO_CENA6)
        self.c23 = Cena(FUNDO_CENA7)
        self.c24 = Cena(FUNDO_CENA8)
        self.c25 = Cena(FUNDO_CENA9)
        self.c26 = Cena(FUNDO_CENA10)
        
        self.c31 = Cena(FUNDO_CENA11)
        self.c32 = Cena(FUNDO_CENA12)
        self.c33 = Cena(FUNDO_CENA13)
        self.c34 = Cena(FUNDO_CENA14)
        self.c35 = Cena(FUNDO_CENA15)

        #self.persona.x = self.x
        #self.persona.y = self.y
        
        """self.joystickfalso = Elemento(JOYSTICK_FALSO, h=100 , w=100, x=750, y=440) #cria um elemento posicionado 'acima' no joystick
        self.joystickfalso.entra(nome_do_fundo)"""
        
        self.marcadorx = Elemento(MARCADOR_X, h=70 , w=70, x=80, y=450) #cria um elemento posicionado 'acima' no joystick
        self.marcadorx.entra(nome_do_fundo)
        
                       
        self.cima = Elemento(MARCADOR_CIMA, h=70 , w=70, x=1200, y=420, vai=self.anda_cima) #cria um elemento posicionado 'acima' no joystick
        self.cima.entra(nome_do_fundo)
        
        self.baixo = Elemento(MARCADOR_BAIXO, h=70 , w=70, x=1200, y=510, vai=self.anda_baixo) #cria um elemento posicionado 'abaixo' no joystick
        self.baixo.entra(nome_do_fundo)
        
        self.direita = Elemento(MARCADOR_DIREITA, h=70 , w=70, x=1150, y=460,vai=self.anda_direita) #cria um elemento posicionado 'à direita' no joystick
        self.direita.entra(nome_do_fundo)
        
        self.esquerda = Elemento(MARCADOR_ESQUERDA, h=70 , w=70, x=1250, y=460, vai=self.anda_esquerda) #cria um elemento posicionado 'à esquerda' no joystick
        self.esquerda.entra(nome_do_fundo)
        
        self.persona = Elemento(PERSONAGEM, h=150 , w=150, x=self.x, y=self.y) # cria Elemento 
        self.persona.entra(nome_do_fundo) # utiliza o método entra() da classe Elemento para não ter que criar um atributo cena para a classe persona_control 
        self.persona1 = Elemento(PERSONAGEM1, h=0 , w=0, x=self.x, y=self.y) # cria Elemento
        self.persona1.entra(nome_do_fundo) 

    def anda_direita(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'direita' é clicado.
        """
        '''Quando necessário os personagens devem ser trocados - Um será zerado e o outro volta ao tamanho normal
        porém ambos devem ser atualizados nas posições para andarem sincronizados, isto para todas as funções 
        que alterem a posição do personagem'''
        
        self.persona1.h = 150
        self.persona1.w = 150
        
        self.persona.h = 0
        self.persona.w = 0
        
        if (self.persona.x > 0):
            self.persona.x = self.x = self.x - 20
            self.persona1.x = self.x = self.x - 20
        #self.persona.x = self.x - 10 > Deixar para averiguações posteriores
        #self.persona.x = self.x -= 10 > Deixar para averiguações posteriores
        
    def anda_esquerda(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'esquerda' é clicado.
        """
        self.persona1.h = 0
        self.persona1.w = 0
        
        self.persona.h = 150
        self.persona.w = 150
        
        if (self.persona.x + 20 < 1350):
            self.persona.x = self.x = self.x + 20
            self.persona1.x = self.x = self.x + 20
        
    def anda_cima(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'em cima' é clicado.
        """
        if (self.persona.y -20 > 80):
            self.persona.y = self.y = self.y - 20
            self.persona1.y = self.y = self.y - 20
        
    def anda_baixo(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'embaixo' é clicado.
        """
        if (self.persona.y + 20 < 500):
            self.persona.y = self.y = self.y + 20
            self.persona1.y = self.y = self.y + 20
if __name__ == "__main__":  
    teste()


