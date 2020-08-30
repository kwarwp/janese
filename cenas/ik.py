# janese.cenas.ik.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Vittolino na UNESP.

.. codeauthor:: Equipe Supygirls <supygirls@gmail.com>

Changelog
---------
.. versionadded::    20.08
      - Criação de múltipla cenas
      - Concatenação das múltiplas cenas (Sala)
      - Uso de botões para acessar segundo andar

"""
from _spy.vitollino.main import Sala, Cena, STYLE

SALA_UM={NORTE="https://i.imgur.com/hqK4K6C.png",
         LESTE="https://i.imgur.com/IY0ZWKp.png",
         SUL="https://i.imgur.com/YDEzStv.png",
         OESTE="https://i.imgur.com/8HC6cMG.png"}
         
SALA_DOIS={NORTE="https://i.imgur.com/sH2GD9s.png",
           LESTE="https://i.imgur.com/R7JE7pM.png",
           SUL="https://i.imgur.com/BSov4HG.png",
           OESTE="https://i.imgur.com/yBuIbjQ.png"}


INVISI = "https://i.imgur.com/JuvyDuW.png"

STYLE["width"] = 900
STYLE["heigth"] = 900

        
class Passeio():

    def __init__(self):
        self.colecao = Sala(n=self.comodo_sala, l=self.comodo_cozinha)
        self.colecao.norte.vai()
        
    def comodo_cozinha(self):
        return self.cozinha = Cena(COZINHA, esquerda = self.sala)
        
    def comodo_sala(self):
        return self.sala = Cena(SALA, direita = self.cozinha)
    
if __name__ == "__main__":
    Passeio()