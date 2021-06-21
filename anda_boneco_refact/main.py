# janese.anda_boneco_refact.main.py
# janese.anda_bonecoo.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

PERSONAGEM = "https://imgur.com/gfe9a1S.png"
FUNDO = "https://imgur.com/vaUUL1h.jpg"
MARCADOR_ESQUERDA = "https://imgur.com/hEF8XPG.png"
MARCADOR_DIREITA = "https://imgur.com/hEF8XPG.png"
MARCADOR_CIMA = "https://imgur.com/hEF8XPG.png"
MARCADOR_BAIXO = "https://imgur.com/hEF8XPG.png"


STYLE["width"] = 900
STYLE["heigth"] = 900


  

class Persona_control:
    """ Cria um elemento que anda a partir do clique no joystick
    
        self.nome_do_elemento = Persona_control(variavel_personagem, nome_do_fundo, 
                                                h =100, w=100, x=10, y=430, movi= 10)
        
        :param variavel_personagem:Requisita o nome da variável que guarda o link do personagem
        :param nome_do_fundo: Insere o personagem em um fundo pré-criado
        :param h: Valor que define a altura do personagem. Por padrão é 100
        :param w: Valor que define a largura do persongem. Por padrão é 100
        :param x: Valor que define a posição do personagem no eixo x. Por padrão é 10
        :param y: Valor que define a posição do personagem no eixo y. Por padrão é 430
        :param movi: Determina a quantidade de movimento do personagem. Por padrão é 10
    """
    def __init__(self, variavel_personagem, nome_do_fundo, h =100, w=100, x=10, y=430, movi= 10):
        self.x = x # Diz que o x acima é nomeado como self.x abaixo
        self.y = y # Diz que o y acima é nomeado como self.y abaixo
        self.h = h # Diz que o h acima é nomeado como self.h abaixo
        self.w = w # Diz que o w acima é nomeado como self.w abaixo
        
        self.movi = movi # Diz que o movi acima é nomeado como self.movi abaixo
        #self.variavel_personagem = variavel_personagem 
        
        self.persona = Elemento(variavel_personagem, h=self.h , w=self.w, x=self.x, y=self.y) # Cria uma instância da classe elemento
        self.persona.entra(nome_do_fundo) # utiliza o método entra() da classe Elemento para não ter que criar um atributo cena para a classe persona_control 
        
        #self.persona.x = self.x > Deixar de stand by para futuras averiguações
        #self.persona.y = self.y > Deixar de stand by para futuras averiguações
          
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
        self.persona.x = self.x = self.x - self.movi
        
    def anda_esquerda(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'esquerda' é clicado.
        """
        self.persona.x = self.x = self.x + self.movi
        
    def anda_cima(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'em cima' é clicado.
        """
        self.persona.y = self.y = self.y - self.movi
        
    def anda_baixo(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'embaixo' é clicado.
        """
        self.persona.y = self.y = self.y + self.movi

fundo = Cena(FUNDO) 
fundo.vai()
bonequinha = Persona_control(PERSONAGEM, fundo) 

