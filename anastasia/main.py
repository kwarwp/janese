# janese.joystick_falso_2607.main.py

#Profa Gi :)

'''Uma forma de fazer a passagem de cenas é criando salas - que permitem 4 cenas
e depois criando o labirinto, adicionando as salas nele.

# Cria Salas
# n = norte, s = sul, l = leste, o = oeste
# Mas serve só para se localizar, dá pra usar de outras formas
# Acho que dá pra fazer com lista também, mas to seguindo o que tava naquela documentação

s1 = Sala(n = c11, s = c12, l = c13, o = c14)
s2 = Sala(n = c21, s = c22, l = c23)

# Cria o labirinto de Salas
# c = centro, n = norte
la = Labirinto(c=s1,n=s2)


Essa é a forma descrita na documentação da biblioteca que usamos para criar o jogo, ela funciona, 
porém como cada sala espera 4 cenas, e o labirinto várias salas, quando alguma delas fica vazia, 
pode acontecer de um clique na tela direcionar para uma sala nula = que não existe. 
Para arrumar isso seria necessário criar uma ação que não faz nada, e 
na posição da sala que não existe adicionar uma sala que 'não faz nada'
'''

'''
Pelo o que entendi da ideia de jogo de vocês, as cenas seriam todas sequenciais, então esse esquema de 
salas e labirinto seria um pouco confuso de implementar.
Por isso, outra maneira seria criando uma lista de cenas.
Essa lista tem que ser criada aqui em cima no código, pq ela vai ser uma variável global, ou seja,
essa lista existe, e vai ser possível acessar ela em qualquer função abaixo.
'''

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto, Sala, Labirinto


from browser import document


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
BATERIA = "https://imgur.com/0kcOVwk.png"
CARGA = "https://imgur.com/dipQTCT.png"




STYLE["width"]=1150
STYLE["height"]=500

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
        self.bonequinha = 0
        self.itens = []
        self.score = 0
        self.ind_cenas= 0
        self.pos_carga = 0

#Função para pegar o item
    def pega_acao(self, event = None):
        
        for i in self.itens:
        
            i.h = 0
            i.w = 0
            self.score = self.score + 1
            carga = Elemento(CARGA, w = 50, h = 50, x=1050+self.pos_carga, y=20)
            self.cenas[self.ind_cenas].bota(carga)
            break
        self.pos_carga = self.pos_carga + 10
        del self.itens[0]
        print(self.itens)
        
            
    


    

#Função para ir para a cena 3    
    def cena3(self, event = None):
    #la.centro.leste.vai()
        self.cenas[2].vai()
        texto_ = Texto(self.c13, txt = "Terceira Cena")
        texto_.vai()
        self.bonequinha = Persona_control(self.c13)
        botao = Elemento(MARCADOR_ESQUERDA, tit="Próxima Cena",
                           h=30 , w=30, x=1100, y=220, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = self.c13,
                           vai = self.cena4)
                           
#Função para ir para a cena 2
    def cena2(self, event = None):
    #la.centro.sul.vai()
        self.cenas[1].vai()
        texto_ = Texto(self.c12, txt = "Segunda Cena")
        texto_.vai()
        self.bonequinha = Persona_control(self.c12)
        botao = Elemento(MARCADOR_ESQUERDA, tit="Próxima Cena",
                           h=30 , w=30, x=1100, y=220, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = self.c12,
                           vai = self.cena3)
    
#Função que cria a cena 1
    def cena1(self):
    #Código se fosse usar o sistema de labirinto
    #la.centro.norte.vai()
    
    
    #Código usando lista
    #Lembrando que lista em python começa sempre da posição 0
        self.cenas[0].vai()
    
        item1 = Elemento(ITEM, tit="Item", h=30 , w=30, x=300, y=500, cena = self.c11)
        item2 = Elemento(ITEM, tit="Item", h=30 , w=30, x=400, y=480, cena = self.c11)
        item3 = Elemento(ITEM, tit="Item", h=30 , w=30, x=550, y=490, cena = self.c11)
        self.itens.append(item1)
        self.itens.append(item2)
        self.itens.append(item3)
        self.score = 0

    
    #Para inserir pop up
        texto_ = Texto(self.c11, txt = "Primeira Cena")
        texto_.vai()
    #Inserindo a boneca
        self.bonequinha = Persona_control(self.c11)
    
    
        pega = Elemento(MARCADOR_MEIO, tit = "Pegar", h=40 , w=40, x=1005, y=470, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = self.c11)
                           
if x==300:                   
        pega.elt.bind("click", self.pega_acao)
    #Inserindo o botão que muda de cena
        bateria = Elemento(BATERIA, tit="Bateria",
                           h=50 , w=50, x=1050, y=20, cena= self.c11)
        proxima = Elemento(MARCADOR_ESQUERDA, tit="Próxima Cena",
                           h=30 , w=30, x=1100, y=220, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = self.c11,
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