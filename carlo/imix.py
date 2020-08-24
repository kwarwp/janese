# janese.carlo.imix.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Nome Sobrenome <mail@local.tipo>

Changelog
---------
.. versionadded::    20.08
        Descreva o que você adicionou no código.

"""
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
from cenas.imix import Inicial
FUNDO = "https://img.freepik.com/vetores-gratis/fundo-branco-textura-elegante_23-2148415643.jpg?size=626&ext=jpg"
CALEND={"IMIX":"https://i.imgur.com/XmmzDHZ.png", 
        "IK":"https://i.imgur.com/9nieFUZ.png",
        "AKBAL":"XX",
        "KAN":"XX",
        "CHICCHAN":"XX",
        "CIMI":"XX",
        "MANIK":"XX",
        "LAMAT":"XX",
        "MALUC":"XX",
        "OC":"XX",
        "CHUEN":"XX",
        "EB":"XX",
        "AKBAL":"XX"
       }
       
STYLE["width"] = 900
STYLE["heigth"] = 900


class Estrutura():

    def __init__(self):
    
        self.fundo=Cena(FUNDO)
        self.imix = Elemento(CALEND["IMIX"], x=100, y=100, cena=self.fundo, vai=self.botao)
        self.ik = Elemento(CALEND["IK"], x=200, y=100, cena=self.fundo, vai=self.botao)
        self.ik.elt.onmouseenter = self.esconde
        self.ik.elt.onmouseleave = self.mostra
        
    def esconde(self, ev=None):
        self.imix.o = 0
        
    def mostra(self, ev=None):
        self.imix.o = 1
        
    def outro_botao(self, ev=None):
        Inicial().chama()
        
    def botao(self, ev=None):
        Inicial().chama()
        
    def vai(self):
        self.fundo.vai()
        
if __name__ == "__main__":
    Estrutura().vai()