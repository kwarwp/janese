# janese.joystick_falso_2607.main.py

#Profa Gi :)

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto, Sala, Labirinto


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
MARCADOR_MEIO = "https://i.imgur.com/2pwjrxD.png"

PERSONAGEM = "https://i.imgur.com/3Im5DeO.png"
ITEM = "https://i.imgur.com/ZWKf0Dr.png"
MOCHILA = "https://imgur.com/8GZoEo9.png"




STYLE["width"]=1150
STYLE["height"]=400

#Cria Cenas

c11 = Cena(FUNDO_CENA1)
c12 = Cena(FUNDO_CENA2)
c13 = Cena(FUNDO_CENA3)
c14 = Cena(FUNDO_CENA4)

c21 = Cena(FUNDO_CENA5)
c22 = Cena(FUNDO_CENA6)
c23 = Cena(FUNDO_CENA7)
'''
# Cria Salas
# n = norte, s = sul, l = leste, o = oeste
# Mas serve só para se localizar, dá pra usar de outras formas
# Acho que dá pra fazer com lista também, mas to seguindo o que tava naquela documentação

s1 = Sala(n = c11, s = c12, l = c13, o = c14)
s2 = Sala(n = c21, s = c22, l = c23)

# Cria o labirinto de Salas
# c = centro, n = norte
la = Labirinto(c=s1,n=s2)
'''

cenas = [c11, c12, c13, c14, c21, c22, c23]
tam = 1

def pega(event = None):
    mochila = Elemento(MOCHILA, h=30 , w=30, x=1050, y=10)
    
    

def cena3(event = None):
    #la.centro.leste.vai()
    cenas[2].vai()
    texto_ = Texto(c13, txt = "Terceira Cena")
    texto_.vai()
    bonequinha = Persona_control(c13)
    botao = Elemento(MARCADOR_ESQUERDA, tit="Próxima Cena",
                           h=30 , w=30, x=1100, y=220, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = c13,
                           vai = cena4)

def cena2(event = None):
    #la.centro.sul.vai()
    cenas[1].vai()
    texto_ = Texto(c12, txt = "Segunda Cena")
    texto_.vai()
    bonequinha = Persona_control(c12)
    botao = Elemento(MARCADOR_ESQUERDA, tit="Próxima Cena",
                           h=30 , w=30, x=1100, y=220, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = c12,
                           vai = cena3)
    

def cena1():
    
    #la.centro.norte.vai()
    cenas[0].vai()
    #Para inserir pop up
    texto_ = Texto(c11, txt = "Primeira Cena")
    texto_.vai()
    bonequinha = Persona_control(c11)
    pega = Elemento(MARCADOR_MEIO, tit = "Não funciona", h=40 , w=40, x=1005, y=470, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = c11,
                           vai = pega)
    proxima = Elemento(MARCADOR_ESQUERDA, tit="Próxima Cena",
                           h=30 , w=30, x=1100, y=220, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = c11,
                           vai = cena2)

    
        
class Persona_control:
    """ Cria um elemento que anda a partir do clique no joystick
    
        self.nome_do_elemento = Persona_control( nome_do_fundo)
        
        :param nome_do_fundo: Insere o personagem em um fundo pré-criado
        
    """
    def __init__(self, nome_do_fundo):
        self.x = 10 # valor pré-estabelecido do x
        self.y = 430 # valor pré-estabelecido do y
        
        self.persona = Elemento(PERSONAGEM, tit = "Menina", h=100 , w=100, x=self.x, y=self.y) # cria Elemento 
        self.persona.entra(nome_do_fundo) # utiliza o método entra() da classe Elemento para não ter que criar um atributo cena para a classe persona_control 
                
        self.cima = Elemento(MARCADOR_CIMA, h=50 , w=50, x=1000, y=420, vai=self.anda_cima) #cria um elemento posicionado 'acima' no joystick
        self.cima.entra(nome_do_fundo)
        
        self.baixo = Elemento(MARCADOR_BAIXO, h=50 , w=50, x=1000, y=510, vai=self.anda_baixo) #cria um elemento posicionado 'abaixo' no joystick
        self.baixo.entra(nome_do_fundo)
        
        self.direita = Elemento(MARCADOR_DIREITA, h=50 , w=50, x=950, y=460,vai=self.anda_direita) #cria um elemento posicionado 'à direita' no joystick
        self.direita.entra(nome_do_fundo)
        
        self.esquerda = Elemento(MARCADOR_ESQUERDA, h=50 , w=50, x=1050, y=460, vai=self.anda_esquerda) #cria um elemento posicionado 'à esquerda' no joystick
        self.esquerda.entra(nome_do_fundo)
        
               
    def get_x(self):
        return self.persona.x
        
    def get_y(self):
        return self.persona.y
        
        

    def anda_direita(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'direita' é clicado.
        """
        if (self.persona.x > 10):
            self.persona.x = self.x = self.x - 20
        #self.persona.x = self.x - 10 > Deixar para averiguações posteriores
        #self.persona.x = self.x -= 10 > Deixar para averiguações posteriores
        
    def anda_esquerda(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'esquerda' é clicado.
        """
        if (self.persona.x < 1100):
            self.persona.x = self.x = self.x + 20
        
    def anda_cima(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'em cima' é clicado.
        """
        if (self.persona.y > 420):
            self.persona.y = self.y = self.y - 20
        
    def anda_baixo(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'embaixo' é clicado.
        """
        if (self.persona.y < 490):
            self.persona.y = self.y = self.y + 20

if __name__ == "__main__":  
    cena1()