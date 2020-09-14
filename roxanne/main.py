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
#from samantha.main import turmaDireita
#from kristen.main import inicialesquerda
#from danae.main import Lago

FUNDO = "https://img.elo7.com.br/product/original/1D27E33/painel-cenario-mundo-encantado-frete-gratis-cenario.jpg"
LIVRO = "https://comunicamack.files.wordpress.com/2016/12/livro.png"
TESTE = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmancilha.files.wordpress.com%2F2008%2F09%2Fteste2.png"

STYLE["width"] = 900
STYLE["heigth"] = 900


#fundo = Cena(FUNDO) 
#fundo.vai()

def cria_fundo():
    teste = Cena(TESTE)
    #fundo = Cena(FUNDO, esquerda=teste, meio=teste) #sem o direita não funciona
    fundo = Cena(FUNDO, esquerda=teste, meio=teste, direita=teste) # com o direita funciona
    fundo.vai()
    
cria_fundo()