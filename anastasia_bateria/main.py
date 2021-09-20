# janese.joystick_falso_2607.main.py

#Profa Gi :)

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto, Sala, Labirinto


from browser import document


#MINHA_MUSICA = "string_correspondente_a_url_e_extensao_da_musica" # Extensões aceitas: mp3, mp4

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
PERSONAGEM1 = "https://i.imgur.com/ab8mN5s.png"
ITEM = "https://i.imgur.com/ZWKf0Dr.png"
ITEM_FALSO = "https://i.imgur.com/D4hzi7R.png"

BATERIA = "https://imgur.com/0kcOVwk.png"
CARGA = "https://imgur.com/dipQTCT.png"




STYLE["width"]=1150
STYLE["height"]=500

#Classe para implementar jogo
class Jogo:

    
    def __init__(self):
        #Cria Cenas
        self.c11 = Cena(FUNDO_CENA1)
        self.c12 = Cena(FUNDO_CENA2)
        self.c13 = Cena(FUNDO_CENA3)
        self.c14 = Cena(FUNDO_CENA4)

        self.c21 = Cena(FUNDO_CENA5)
        self.c22 = Cena(FUNDO_CENA6)
        self.c23 = Cena(FUNDO_CENA7)
        
        self.cenas = [self.c11, self.c12, self.c13, self.c14, self.c21, self.c22, self.c23]
        #Criação das variáveis globais
        self.bonequinha = 0
        #Lista de itens para cada cena
        self.itens = []
        #Indíce para indicar a cena em que a personagem está no momento
        self.ind_cenas= 0
        #Variável para auxiliar o 'aumento' da bateria
        self.pos_carga = 0

#Função para pegar o item
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
                    
                    #Remove o item encontrado da lista
                    self.itens.remove(i)
                    #Atualiza a variável
                    aux = False
                    if (len(self.itens) == 0):
                        #Se eu peguei o último item - adiciona a barrinha da bateria
                        carga = Elemento(CARGA, w = 50, h = 50, x=1050+self.pos_carga, y=20)
                        self.cenas[self.ind_cenas].bota(carga)
                                           
                    break
                    
            if (aux):
                #Se nenhum item estiver próximo
                texto_ = Texto(self.cenas[self.ind_cenas], txt = "Você não está próxima de nenhum item!")
                texto_.vai()
            

        else:
            
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

    

#Função para ir para a cena 3    
    def cena3(self, event = None):
    #la.centro.leste.vai()
        if(len(self.itens) == 0):
            self.cenas[2].vai()
            self.ind_cenas = 2
            #self.pos_carga = 0
        
            item1 = Elemento(ITEM, tit="Item", h=30 , w=30, x=330, y=500, cena = self.c13)
            #item2 = Elemento(ITEM, tit="Item", h=30 , w=30, x=400, y=480, cena = self.c11)
            item3 = Elemento(ITEM, tit="Item", h=30 , w=30, x=700, y=450, cena = self.c13)
            self.itens.append(item1)
            #self.itens.append(item2)
            self.itens.append(item3)
        
        
            texto_ = Texto(self.c13, txt = "Terceira Cena")
            texto_.vai()
            self.bonequinha = Persona_control(self.c13)
        
            pega = Elemento(MARCADOR_MEIO, tit = "Pegar", h=40 , w=40, x=1005, y=470, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = self.c13)                          
            pega.elt.bind("click", self.pega_acao)
        
            #Inserindo o botão que muda de cena
            bateria = Elemento(BATERIA, tit="Bateria",
                           h=50 , w=50, x=1050, y=20, cena= self.c13)
            #Posição Inicial               
            carga = Elemento(CARGA, w = 50, h = 50, x=1050, y=20)
            self.cenas[self.ind_cenas].bota(carga)
            #Inicial + 10
            carga1 = Elemento(CARGA, w = 50, h = 50, x=1050+self.pos_carga, y=20)
            self.cenas[self.ind_cenas].bota(carga1)
            #Aumenta a posição para o próximo item
            self.pos_carga = self.pos_carga + 10
                           
            proxima = Elemento(MARCADOR_ESQUERDA, tit="Próxima Cena",
                           h=30 , w=30, x=1100, y=220, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = self.cenas[self.ind_cenas],
                           vai = self.cena4)
        else:
            texto_ = Texto(self.c12, txt = "Você ainda não terminou de explorar essa cena!")
            texto_.vai()
            
            
                           
#Função para ir para a cena 2
    def cena2(self, event = None):
    #la.centro.sul.vai()
        if(len(self.itens) == 0):
            
            self.cenas[1].vai()
            #Atualiza o indíce da cena e a posição da carga da bateria
            self.ind_cenas = 1
            #self.pos_carga = 0
        
            item1 = Elemento(ITEM, tit="Item", h=30 , w=30, x=330, y=500, cena = self.c12)
            #item2 = Elemento(ITEM, tit="Item", h=30 , w=30, x=400, y=480, cena = self.c11)
            item3 = Elemento(ITEM, tit="Item", h=30 , w=30, x=550, y=490, cena = self.c12)
            self.itens.append(item1)
            #self.itens.append(item2)
            self.itens.append(item3)
        
        
            texto_ = Texto(self.c12, txt = "Segunda Cena")
            texto_.vai()
            self.bonequinha = Persona_control(self.c12)
        
            pega = Elemento(MARCADOR_MEIO, tit = "Pegar", h=40 , w=40, x=1005, y=470, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = self.c12)                          
            pega.elt.bind("click", self.pega_acao)
        
            #Inserindo o botão que muda de cena
            bateria = Elemento(BATERIA, tit="Bateria",
                           h=50 , w=50, x=1050, y=20, cena= self.c12)
            carga = Elemento(CARGA, w = 50, h = 50, x=1050, y=20)
            self.cenas[self.ind_cenas].bota(carga)
            #Aumenta a posição para o próximo item
            self.pos_carga = self.pos_carga + 10
                        
            proxima = Elemento(MARCADOR_ESQUERDA, tit="Próxima Cena",
                           h=30 , w=30, x=1100, y=220, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = self.cenas[self.ind_cenas],
                           vai = self.cena3)
        else:
            texto_ = Texto(self.c11, txt = "Você ainda não terminou de explorar essa cena!")
            texto_.vai()
                           
    
#Função que cria a cena 1 - tem que adicionar o self pois agora estamos dentro de uma classe
    def cena1(self):
    #Código se fosse usar o sistema de labirinto
    #la.centro.norte.vai()
    
    
    #Código usando lista
    #Lembrando que lista em python começa sempre da posição 0
        self.cenas[0].vai()
        self.ind_cenas = 0
        
        #Cria itens e os adiciona na lista de itens    
        item1 = Elemento(ITEM, tit="Item", h=30 , w=30, x=300, y=500, cena = self.c11)
        item2 = Elemento(ITEM, tit="Item", h=30 , w=30, x=400, y=480, cena = self.c11)
        item3 = Elemento(ITEM, tit="Item", h=30 , w=30, x=550, y=490, cena = self.c11)
        self.itens.append(item1)
        self.itens.append(item2)
        self.itens.append(item3)
        
        #Pra dificultar :)
        item_falso1 = Elemento(ITEM_FALSO, tit="Item", h=40 , w=40, x=200, y=500, cena = self.c11)
        item_falso1 = Elemento(ITEM_FALSO, tit="Item", h=40 , w=40, x=600, y=500, cena = self.c11)
        
        #bateria vazia
        bateria = Elemento(BATERIA, tit="Bateria",
                           h=50 , w=50, x=1050, y=20, cena= self.c11)

    
    #Para inserir pop up
        texto_ = Texto(self.c11, txt = "Primeira Cena - Descubra quais são as estrelas verdadeiras e colete-as")
        texto_.vai()
    #Inserindo a boneca
        self.bonequinha = Persona_control(self.c11)
        
        #nome_da_musica = Musica(MINHA_MUSICA, loop = True, autoplay = True)
    
#Botão de pegar elemento
        pega = Elemento(MARCADOR_MEIO, tit = "Pegar", h=40 , w=40, x=1005, y=470, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = self.c11)                          
        pega.elt.bind("click", self.pega_acao)
        
    #Inserindo o botão que muda de cena
        
        proxima = Elemento(MARCADOR_ESQUERDA, tit="Próxima Cena",
                           h=30 , w=30, x=1100, y=220, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = self.cenas[self.ind_cenas],
                           vai = self.cena2)
        


    
        
class Persona_control:
    """ Cria um elemento que anda a partir do clique no joystick
    
        self.nome_do_elemento = Persona_control( nome_do_fundo)
        
        :param nome_do_fundo: Insere o personagem em um fundo pré-criado
        
    """
    def __init__(self, nome_do_fundo):
        self.x = 10 # valor pré-estabelecido do x
        self.y = 430 # valor pré-estabelecido do y
        
        '''Para criar um persogem que muda de direita para esquerda: Crie dois personagens e um deles tem tamanho zerado,
        ou seja, h=0 e w=0.
        Para mudar de personagem veja as funções de andar'''
        self.persona = Elemento(PERSONAGEM, tit = "Menina", h=100 , w=100, x=self.x, y=self.y) # cria Elemento 
        self.persona.entra(nome_do_fundo) # utiliza o método entra() da classe Elemento para não ter que criar um atributo cena para a classe persona_control 
               
        self.persona1 = Elemento(PERSONAGEM1, tit = "Menina", h=0 , w=0, x=self.x, y=self.y) # cria Elemento 
        self.persona1.entra(nome_do_fundo) # utiliza o método entra() da classe Elemento para não ter que cria
               
        
               
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
        '''Quando necessário os personagens devem ser trocados - Um será zerado e o outro volta ao tamanho normal
        porém ambos devem ser atualizados nas posições para andarem sincronizados, isto para todas as funções 
        que alterem a posição do personagem'''
        
        self.persona1.h = 100
        self.persona1.w = 100
        
        self.persona.h = 0
        self.persona.w = 0
        
        if (self.persona.x - 20 > 0):
            self.persona.x = self.x = self.x - 20
            self.persona1.x = self.x = self.x - 20
        #self.persona.x = self.x - 10 > Deixar para averiguações posteriores
        #self.persona.x = self.x -= 10 > Deixar para averiguações posteriores
        
    def anda_esquerda(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'esquerda' é clicado.
        """
        self.persona1.h = 0
        self.persona1.w = 0
        
        self.persona.h = 100
        self.persona.w = 100
        
        if (self.persona.x + 20 < 1100):
            self.persona.x = self.x = self.x + 20
            self.persona1.x = self.x = self.x + 20
        
    def anda_cima(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'em cima' é clicado.
        """
        if (self.persona.y - 20 > 400):
            self.persona.y = self.y = self.y - 20
            self.persona1.y = self.y = self.y - 20
        
    def anda_baixo(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'embaixo' é clicado.
        """
        if (self.persona.y + 20 < 500):
            self.persona.y = self.y = self.y + 20
            self.persona1.y = self.y = self.y + 20

if __name__ == "__main__":  
    jogo = Jogo()
    jogo.cena1()