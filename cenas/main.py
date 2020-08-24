"""   Tutorial Vitollino para Equipe UNESP 

.. codeauthor:: Equipe Suoygirls <supygirls@gmail.com>

.. version:: 20.01
     - Adiciona Cena;
     - Texto inicial 
     - Texto ao clicar em Elemento;
     - Import de Salas;

"""
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
from samantha.main import turmaDireita
from kristen.main import inicialesquerda
from danae.main import Lago

FUNDO = "https://img.elo7.com.br/product/original/1D27E33/painel-cenario-mundo-encantado-frete-gratis-cenario.jpg"
LIVRO = "https://comunicamack.files.wordpress.com/2016/12/livro.png"

STYLE["width"] = 900
STYLE["heigth"] = 900


class inicial():

    def __init__(self):
        """ Criação do fundo. Importação de módulos , do primeiro elemento (livro) e um texto inicial"""
        self.fundo = Cena(FUNDO, direita =turmaDireita(), esquerda =inicialesquerda(), meio=Lago()) 
        self.livro = Elemento(LIVRO, texto = "Abra este livro!", h=150 , w=150, x=350, y=250)
        self.mais = Texto(self.fundo, txt = "Teste!", foi = self.mostra_livro) 
        
    def mostra_livro(self, *_ ):
        """Subordina o aparecimento do livro ao fechamento do texto inicial"""
        self.livro.entra(self.fundo)
        
    def chama(self):
        """ Chama a Cana e o texto inicial"""
        self.fundo.vai()
        self.mais.vai()
        
        
if __name__ == "__main__":        
    inicial().chama()