# janese.adda.main.py
#Bianca
#Ada Lovelace

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document
#objetos
FOLHA = "https://i.imgur.com/upAN1GX.png"
PENA = "https://i.imgur.com/916QFLA.png"

SOMA = "https://img.icons8.com/dusk/50/000000/plus-math.png"
MENOS = "https://img.icons8.com/dusk/50/000000/minus-math.png"
MULTIPLICA = "https://img.icons8.com/dusk/50/000000/multiply.png"
DIVISAO = "https://img.icons8.com/dusk/50/000000/divide.png"

INFINITOum = "https://img.icons8.com/dusk/50/000000/infinity.png"
INFINITOdois = "https://img.icons8.com/doodle/50/000000/repeat.png"
INFINITOtres = "https://img.icons8.com/carbon-copy/50/000000/repeat.png"
INFINITOquatro = "https://img.icons8.com/plasticine/50/000000/repeat.png"


FUNDO = "https://i.imgur.com/KYKStgT.png"
PERSONAGEM = "https://imgur.com/E6lSl7l.gif"
PERSONAGEM1= "https://imgur.com/A6wdCYS.gif"

MARCADOR_X = "https://imgur.com/4RZPRRz.png"
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


BATERIA = "https://imgur.com/0PGuq9q.png"
CARGA = "https://imgur.com/mw9hsBq.png"


STYLE["width"]=1350
STYLE["height"]=700
class cenas:
    def __init__(self):
        self.c11 = Cena(FUNDO_CENA1)
        self.c12 = Cena(FUNDO_CENA2)

        self.c21 = Cena(FUNDO_CENA5)
        self.c22 = Cena(FUNDO_CENA6)

        
        self.c31 = Cena(FUNDO_CENA11)
        self.c32 = Cena(FUNDO_CENA12)
        
        self.cenas = [self.c11, self.c12, self.c21, self.c22, self.c31, self.c32]
        self.bonequinha = 0
        self.itens = []
        self.ind_cenas= 0
        self.pos_carga = 0  

    def pega_acao(self, event = None):
         
        #Verifica se ainda existe algum item na cena - se a lista de itens está vazia        
        if (len(self.itens) > 0):
            aux = True #Variável auxiliar para exibir a mensagem de erro de proximidade
            #Percorre a lista de itens para encontrar se tem algum próximo
            for i in self.itens:
                if(self.verifica_proximidade(i.x, i.y)):
                    #Se exisitir um item próximo a personagem ele será 'apagado' da cena
                    i.h = 0
                    i.w = 0
                    #E a bateria irá encher
                    carga = Elemento(CARGA, w = 80, h = 50, x=50+self.pos_carga, y=20)
                    self.cenas[self.ind_cenas].bota(carga)
                    #Aumenta a posição para o próximo item
                    self.pos_carga = self.pos_carga + 10
                    #Remove o item encontrado da lista
                    self.itens.remove(i)
                    #Atualiza a variável
                    aux = False
                    break
                    
            if (aux):
                #Se nenhum item estiver próximo
                texto_ = Texto(self.cenas[self.ind_cenas], txt = "Você não está próxima de nenhum item!")
                texto_.vai()
            

        else:
            #Se a lista estiver vazia
            texto_ = Texto(self.cenas[self.ind_cenas], txt = "Você pegou todos os itens!")
            texto_.vai()
            
        
            
    #Verifica se a bonequinha está próxima de algum item
    def verifica_proximidade(self, item_x, item_y):
            #A verificação é feita atravé das posições x,y e x + largura e y + altura da bonequinha em relação 
            #as posições x, y do item

        if((item_x >= self.bonequinha.x and item_x <= self.bonequinha.x + 100) and
          (item_y >= self.bonequinha.y and item_y <= self.bonequinha.y + 100)):
             return True
        else:
             return False
             
    def cena1(self):
        self.cenas[0].vai()
        proxima = Elemento(MARCADOR_PLAY, tit="Próxima Cena",
                               h=130 , w=130, x=1190, y=50, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.cenas[self.ind_cenas],
                               vai = self.cena2) 
        

    def cena2(self, event = None):
        #Código se fosse usar o sistema de labirinto
        #la.centro.norte.vai()


        #Código usando lista
        #Lembrando que lista em python começa sempre da posição 0
            self.cenas[1].vai()
            self.ind_cenas = 1

            #Cria itens e os adiciona na lista de itens    
            item1 = Elemento(PENA, tit="Item", h=30 , w=30, x=300, y=500, cena = self.c12)
            item2 = Elemento(FOLHA, tit="Item", h=30 , w=30, x=400, y=480, cena = self.c12)
            #item3 = Elemento(PENA, tit="Item", h=30 , w=30, x=550, y=490, cena = self.c12)
            self.itens.append(item1)
            self.itens.append(item2)
            #self.itens.append(item3)

            #bateria vazia
            bateria = Elemento(BATERIA, tit="Bateria",h=50 , w=100, x= 50, y=20, cena= self.c12)

        #Inserindo a boneca
            self.bonequinha = Persona_control(self.c12)

            #nome_da_musica = Musica(MINHA_MUSICA, loop = True, autoplay = True)

    #Botão de pegar elemento  h=70 , w=70, x=1200, y=420
            pega = Elemento(MARCADOR_X, tit = "Pegar", h=70 , w=70, x=1200, y=470, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.c12)                          
            pega.elt.bind("click", self.pega_acao)

        #Inserindo o botão que muda de cena

            proxima = Elemento(MARCADOR_PLAY, tit="Próxima Cena",
                               h=70 , w=70, x=1200, y=50, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.cenas[self.ind_cenas],
                               vai = self.cena3)


        #Função para ir para a cena 2
    def cena3(self, event = None):
        if(len(self.itens) == 0):
            self.cenas[2].vai()
            self.ind_cenas = 2
            proxima = Elemento(MARCADOR_PLAY, tit="Próxima Cena",
                                h=130 , w=130, x=1190, y=50, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.cenas[self.ind_cenas],
                               vai = self.cena4) 
      #  else:
       #     texto_ = Texto(self.c11)
        #    texto_.vai()
            
    def cena4(self, event = None):
        #la.centro.sul.vai()
            

                self.cenas[3].vai()
                #Atualiza o indíce da cena e a posição da carga da bateria
                self.ind_cenas = 3
                self.pos_carga = 1

                item1 = Elemento(SOMA, tit="Item", h=70 , w=70, x=330, y=500, cena = self.c22)
                item2 = Elemento(MENOS, tit="Item", h=30 , w=30, x=400, y=480, cena = self.c22)
                item3 = Elemento(MULTIPLICA, tit="Item", h=30 , w=30, x=550, y=490, cena = self.c22)
                item4 = Elemento(DIVISAO, tit="Item", h=30 , w=30, x=550, y=490, cena = self.c22)
                self.itens.append(item1)
                self.itens.append(item2)
                self.itens.append(item3)
                self.itens.append(item4)



                self.bonequinha = Persona_control(self.c22)
                self.x = 410 # valor pré-estabelecido do x
                self.y = 430
                
                pega = Elemento(MARCADOR_X, tit = "Pegar", h=70 , w=70, x=1200, y=470, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.c22)                              
                pega.elt.bind("click", self.pega_acao)

                #Inserindo o botão que muda de cena
                batteria = Elemento(BATERIA, tit="Bateria",h=50 , w=100, x= 50, y=20, cena= self.c22)
                proxima = Elemento(MARCADOR_PLAY, tit="Próxima Cena",
                                h=70 , w=70, x=1200, y=50, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.cenas[self.ind_cenas],
                               vai = self.cena5)
                               
                               
                               
    def cena5(self, event = None):
        if(len(self.itens) == 0):
            self.cenas[4].vai()
            self.ind_cenas = 4
            
            proxima = Elemento(MARCADOR_PLAY, tit="Próxima Cena",
                                h=130 , w=130, x=1190, y=50, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.cenas[self.ind_cenas],
                               vai = self.cena6) 
            
    def cena6(self, event = None):
        #la.centro.sul.vai()
            

                self.cenas[5].vai()
                #Atualiza o indíce da cena e a posição da carga da bateria
                self.ind_cenas = 5
                self.pos_carga = 4

                item1 = Elemento(INFINITOum, tit="Item", h=70 , w=70, x=330, y=500, cena = self.c32)
                item2 = Elemento(INFINITOdois, tit="Item", h=30 , w=30, x=400, y=480, cena = self.c32)
                item3 = Elemento(INFINITOtres, tit="Item", h=30 , w=30, x=550, y=490, cena = self.c32)
                item4 = Elemento(INFINITOquatro, tit="Item", h=30 , w=30, x=550, y=490, cena = self.c32)
                self.itens.append(item1)
                self.itens.append(item2)
                self.itens.append(item3)
                self.itens.append(item4)



                self.bonequinha = Persona_control(self.c32)
                self.x = 410 # valor pré-estabelecido do x
                self.y = 430
                
                pega = Elemento(MARCADOR_X, tit = "Pegar", h=70 , w=70, x=1200, y=470, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.c32)                              
                pega.elt.bind("click", self.pega_acao)

                #Inserindo o botão que muda de cena
                batteria = Elemento(BATERIA, tit="Bateria",h=50 , w=100, x= 50, y=20, cena= self.c32)
                proxima = Elemento(MARCADOR_PLAY, tit="Próxima Cena",
                                h=70 , w=70, x=1200, y=50, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.cenas[self.ind_cenas],
                              vai = self.cena7)


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
        
        """self.joystickfalso = Elemento(JOYSTICK_FALSO, h=100 , w=100, x=750, y=440) #cria um elemento posicionado 'acima' no joystick
        self.joystickfalso.entra(nome_do_fundo)"""
        
       # self.marcadorx = Elemento(MARCADOR_X, h=70 , w=70, x=80, y=450) #cria um elemento posicionado 'acima' no joystick
        #self.marcadorx.entra(nome_do_fundo)
        
                       
        self.cima = Elemento(MARCADOR_CIMA, h=70 , w=70, x=1200, y=390, vai=self.anda_cima) #cria um elemento posicionado 'acima' no joystick
        self.cima.entra(nome_do_fundo)
        
        self.baixo = Elemento(MARCADOR_BAIXO, h=70 , w=70, x=1200, y=530, vai=self.anda_baixo) #cria um elemento posicionado 'abaixo' no joystick
        self.baixo.entra(nome_do_fundo)
        
        self.direita = Elemento(MARCADOR_DIREITA, h=70 , w=70, x=1140, y=460,vai=self.anda_direita) #cria um elemento posicionado 'à direita' no joystick
        self.direita.entra(nome_do_fundo)
        
        self.esquerda = Elemento(MARCADOR_ESQUERDA, h=70 , w=70, x=1260, y=460, vai=self.anda_esquerda) #cria um elemento posicionado 'à esquerda' no joystick
        self.esquerda.entra(nome_do_fundo)
        
       # self.play = Elemento(MARCADOR_PLAY, h=70 , w=70, x=1250, y=860, vai=self.anda_esquerda) #cria um elemento posicionado 'à esquerda' no joystick
        #self.play.entra(nome_do_fundo)
        
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
    jogo = cenas()
    jogo.cena1()


