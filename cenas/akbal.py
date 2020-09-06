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
    def bota(self, *_): 
        inv.bota(self, True)
        #x,y,w,h=self.memento
        #self.vai=lambda*_:self.resgata(x=x,y=y,w=w,h=h)
        self.vai=lambda*_:self.resgata(*self.memento)
    
    def resgata(self,x,y,w,h):
        self.x,self.y,self.w,self.h= x,y,w,h
        inv.tira(self.tit)
        self.entra(inv.cena)
        self.vai=self.bota
        
    def mementor(self,memento):
        self.memento=memento
        
    

class Ambiente():

    def __init__(self):
        inv.inicia()
        self.fundo=Cena(ITEM["FLORESTA"])
        
        self.maca=Elemento(ITEM["MACA"], tit="maçã",style=dict(height=60,widht=60, left=600, top=20),cena=self.fundo, vai=self.guarda_item)
        
        self.laranja=Item(ITEM["LARANJA"], tit="laranja",style=dict(height=60,widht=60, left=100, top=100),cena=self.fundo)
        self.laranja.mementor((110,150,200,"200px"))
        self.laranja.vai=self.laranja.bota
        

        self.fundo.vai()
        
    def guarda_item(self, *_):    
        # sem o "*_" nos parâmetros: TypeError: guarda_item() takes 1 positional argument but more were given 
        inv.bota(self.maca, True)
        
if __name__ == "__main__":
    Ambiente()