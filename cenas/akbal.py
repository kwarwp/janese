# janese.cenas.akbal.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Vittolino na UNESP.

.. codeauthor:: Equipe Supygirls <supygirls@gmail.com>

Changelog
---------
.. versionadded::    20.08
      - Criação de Elementos
      - Implementação do inventário

"""
from _spy.vitollino.main import Cena, Elemento, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE["width"] = 900
STYLE["heigth"]= "900px"

ITEM={"LARANJA":"https://i.imgur.com/XXi1abd.png",
      "MACA":"https://i.imgur.com/8aCEBLc.png",
      "FLORESTA":"https://i.imgur.com/xUzMidi.jpeg"}

class Item(Elemento):
    
    #self.elemento = None
    def bota(self,elemento=None, *_):
        self.elemento= Elemento 
        inv.bota(self.elemento, True)
        
    def resgata(self,elemento=None, *_):
        self.elemento=Elemento 
        inv.tira(self.elemento)
        self.vai(self.fundo)

class Ambiente():

    def __init__(self):
        inv.inicia()
        self.fundo=Cena(ITEM["FLORESTA"])
        
        self.maca=Elemento(ITEM["MACA"], tit="maçã",style=dict(height=60,widht=60, left=600, top=20),drag=True,drop={},cena=self.fundo, vai=Item.bota)
        
        self.laranja=Elemento(ITEM["LARANJA"], tit="laranja",style=dict(height=60,widht=60, left=100, top=100),drag=True,cena=self.fundo, vai=Item.bota)

        self.fundo.vai()
        
    def guarda_item(self):    
        inv.bota(self.maca, True)
        
if __name__ == "__main__":
    Ambiente()