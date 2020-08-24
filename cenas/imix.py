# janese.cenas.imix.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""     Vitollino na UNESP 2020

.. codeauthor:: Equipe Supygirls <supygirls@gmail.com>

Changelog
---------
.. versionadded::    20.08
       - Cenas;
       - Texto de abertura;
       - Elemento;
       - Texto ao clicar no elemento;
       - Importação de classes de MESMO MÓDULO

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
    """ Adiciona fundo, elemento e textos. 
    """

    def __init__(self):
        """ Criação do fundo e preparação da cena para cliques à direita, esquerda e meios."""
        self.fundo = Cena(FUNDO, direita =turmaDireita(), esquerda =inicialesquerda(), meio=Lago()) 
        """ Cria elemento da Cena. Adiciona nome ao elemento e texto."""
        self.livro = Elemento(LIVRO, tit = "LIVRO" texto = "Era uma vez...", h=150 , w=150, x=350, y=250)
        """ Cria texto que é carregado junto da abertura da cena."""
        self.mais = Texto(self.fundo, txt = "Teste!", foi = self.mostra_livro) 
        
    def mostra_livro(self, *_ ):
        """Subordina o aparecimento do livro ao fechamento do texto de abertura"""
        self.livro.entra(self.fundo)
        
    def chama(self):
        """ Chama a Cena e o texto inicial"""
        self.fundo.vai()
        self.mais.vai()
        
        
if __name__ == "__main__":        
    inicial().chama()