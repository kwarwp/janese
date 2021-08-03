# janese.joystick_falso_2607.main.py

#Profa Gi :)

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto


FUNDO_CENA1 = "https://i.imgur.com/WAjioMk.png"
FUNDO_CENA2 = "https://i.imgur.com/j9lBVbC.png"
FUNDO_CENA3 = "https://i.imgur.com/1LqdljV.png"
FUNDO_CENA4 = "https://i.imgur.com/vSSZBm0.png"
FUNDO_CENA5 = "https://i.imgur.com/36Eobvt.png"
FUNDO_CENA6 = "https://i.imgur.com/gsNVduh.png"
FUNDO_CENA7 = "https://i.imgur.com/n2NElc8.png"


MARCADOR_ESQUERDA = "https://i.imgur.com/ihnkAEk.png"
MARCADOR_DIREITA = "https://i.imgur.com/S7yT60m.png"
MARCADOR_CIMA = "https://i.imgur.com/0wQ4x2L.png"
MARCADOR_BAIXO = "https://i.imgur.com/MJtWXUb.png"

PERSONAGEM = "https://i.imgur.com/3Im5DeO.png"
Colecionavel = "https://imgur.com/ZWKf0Dr.png"
Mochila = "https://imgur.com/8GZoEo9.png"




STYLE["width"]=1150
STYLE["height"]=400


def teste():
    fundo = Cena(FUNDO_CENA1) 
    fundo.vai()
    bonequinha = Persona_control(fundo) 
     
    
        
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
                
        self.cima = Elemento(MARCADOR_CIMA, h=50 , w=50, x=1000, y=430, vai=self.anda_cima) #cria um elemento posicionado 'acima' no joystick
        self.cima.entra(nome_do_fundo)
        
        self.baixo = Elemento(MARCADOR_BAIXO, h=50 , w=50, x=1000, y=500, vai=self.anda_baixo) #cria um elemento posicionado 'abaixo' no joystick
        self.baixo.entra(nome_do_fundo)
        
        self.direita = Elemento(MARCADOR_DIREITA, h=50 , w=50, x=960, y=460,vai=self.anda_direita) #cria um elemento posicionado 'à direita' no joystick
        self.direita.entra(nome_do_fundo)
        
        self.esquerda = Elemento(MARCADOR_ESQUERDA, h=50 , w=50, x=1040, y=460, vai=self.anda_esquerda) #cria um elemento posicionado 'à esquerda' no joystick
        self.esquerda.entra(nome_do_fundo)
        
               
        
        
        

    def anda_direita(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'direita' é clicado.
        """
        self.persona.x = self.x = self.x - 20
        #self.persona.x = self.x - 10 > Deixar para averiguações posteriores
        #self.persona.x = self.x -= 10 > Deixar para averiguações posteriores
        
    def anda_esquerda(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'esquerda' é clicado.
        """
        self.persona.x = self.x = self.x + 20
        
    def anda_cima(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'em cima' é clicado.
        """
        self.persona.y = self.y = self.y - 20
        
    def anda_baixo(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'embaixo' é clicado.
        """
        self.persona.y = self.y = self.y + 20

if __name__ == "__main__":  
    teste()