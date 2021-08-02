# janese.testemudarcena.main.py
# janese.anda_bonecoo.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

cont = 0
class Eventos:
    CENA_01 = "https://imgur.com/Yemi2Ln.png"
    CENA_02 = "https://imgur.com/D3HMo5Y.png"
    CENA_03 = "https://imgur.com/4EvUuOb.png"
    CENA_04 = "https://imgur.com/lVWFf30.png"
    CENA_05 = "https://imgur.com/uy6TbIK.png"
    CENA_06 = "https://imgur.com/v8WAwmK.png"
    CENA_07 = "https://imgur.com/BMFvkll.png"
    CENA_08 = "https://imgur.com/PvLmT3r.png"
    CENA_09 = "https://imgur.com/9YzRfCk.png"
    
    listaFase = [CENA_02,    #listaFase = [local_imagem_fase,...]
                 CENA_03,
                 CENA_04,
                 CENA_05,
                 CENA_06,
                 CENA_07,
                 CENA_08,
                 CENA_09,]
                  
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
    
    def __init__(self):
        self.x = 10
        self.y = 430
        self.ambiente = Cena(self.CENA_01)
        self.boneco = Elemento(self.PERSONAGEM, x=self.x1, y=self.y1, cena=self.ambiente)
        document.bind("keydown", self.anda_boneco)  # captura o evento de teclado
           
    def vai(self):
        """ mostra corredor do labirinto """
        self.ambiente.vai()

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
        
        #self.persona.x = self.x
        #self.persona.y = self.y
        
        self.joystickfalso = Elemento(JOYSTICK_FALSO, h=100 , w=100, x=750, y=440) #cria um elemento posicionado 'acima' no joystick
        self.joystickfalso.entra(nome_do_fundo)
        
        self.marcadorx = Elemento(MARCADOR_X, h=70 , w=70, x=80, y=450) #cria um elemento posicionado 'acima' no joystick
        self.marcadorx.entra(nome_do_fundo)
        
        self.cima = Elemento(MARCADOR_CIMA, h=40 , w=40, x=780, y=450, vai=self.anda_cima) #cria um elemento posicionado 'acima' no joystick
        self.cima.entra(nome_do_fundo)
        
        self.baixo = Elemento(MARCADOR_BAIXO, h=40 , w=40, x=780, y=500, vai=self.anda_baixo) #cria um elemento posicionado 'abaixo' no joystick
        self.baixo.entra(nome_do_fundo)
        
        self.direita = Elemento(MARCADOR_DIREITA, h=40 , w=40, x=720, y=490,vai=self.anda_direita) #cria um elemento posicionado 'à direita' no joystick
        self.direita.entra(nome_do_fundo)
        
        self.esquerda = Elemento(MARCADOR_ESQUERDA, h=40 , w=40, x=840, y=490, vai=self.anda_esquerda) #cria um elemento posicionado 'à esquerda' no joystick
        self.esquerda.entra(nome_do_fundo)
        
        self.persona = Elemento(PERSONAGEM, h=170 , w=190, x=self.x, y=self.y) # cria Elemento 
        self.persona.entra(nome_do_fundo) # utiliza o método entra() da classe Elemento para não ter que criar um atributo cena para a classe persona_control 
        
        



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
    Eventos()