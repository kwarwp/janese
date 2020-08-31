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


class ambiente():

    def __init__(self):
        inv.inicia()
        self.fundo=Cena(ITEM["FLORESTA"])
        self.maca=Elemento(ITEM["MACA"], tit="maçã", txt="Opa, você encontrou uma maçã!", h=100,w=100, x=100, y=20, cena=self.fundo, vai=inv.bota())
        self.laranja=Elemento(ITEM["LARANJA"], tit="laranja", txt="Opa, você encontrou uma laranja!",h=100,w=100, x=100, y=120, cena=self.fundo)
        #inv.bota(self.maca, drag=True)
        inv.bota(self.laranja, drag=True)
        self.fundo.vai()
        
if __name__ == "__main__":
    ambiente()