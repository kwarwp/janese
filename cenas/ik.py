# janese.cenas.ik.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Vittolino na UNESP.

.. codeauthor:: Equipe Supygirls <supygirls@gmail.com>

Changelog
---------
.. versionadded::    20.08
      - Criação de múltipla cenas
      - Concatenação das múltiplas cenas (Sala)
      - Implementação do labirinto

"""
from _spy.vitollino.main import Sala, Cena, Labirinto,STYLE

SALA_UM={"NORTE": "https://i.imgur.com/hqK4K6C.png",
         "LESTE":"https://i.imgur.com/IY0ZWKp.png",
         "SUL":"https://i.imgur.com/YDEzStv.png",
         "OESTE":"https://i.imgur.com/8HC6cMG.png"}
         
SALA_DOIS={"NORTE":"https://i.imgur.com/sH2GD9s.png",
           "LESTE":"https://i.imgur.com/R7JE7pM.png",
           "SUL":"https://i.imgur.com/BSov4HG.png",
           "OESTE":"https://i.imgur.com/yBuIbjQ.png"}


INVISI = "https://i.imgur.com/JuvyDuW.png"

STYLE["width"] = 900
STYLE["heigth"] = "900px"
"""Adequação da área de clique"""
STYLE["min-height"] = "900px"

        
class Passeio():
    """Gera um labirinto com duas salas
    """
    def __init__(self):
        """Start com coleção de Salas"""
        self.colecao_total=Labirinto(n=self.sala_um(),c=self.sala_dois())
        """Referencia a sala e a cena do labirinto"""
        self.colecao_total.centro.norte.vai()
    
    def sala_um(self):
        """Coleção de cenas 1"""
        self.norte_um = Cena(SALA_UM["NORTE"])
        self.leste_um = Cena(SALA_UM["LESTE"])
        self.oeste_um = Cena(SALA_UM["OESTE"])
        self.sul_um = Cena(SALA_UM["SUL"])
        self.colecao_um = Sala(n=self.norte_um,l=self.leste_um,s=self.sul_um,o=self.oeste_um) 
        return self.colecao_um
                
    def sala_dois(self):
        """Coleção de cenas 2"""
        self.norte_dois = Cena(SALA_DOIS["NORTE"])
        self.leste_dois = Cena(SALA_DOIS["LESTE"])
        self.oeste_dois = Cena(SALA_DOIS["OESTE"])
        self.sul_dois = Cena(SALA_DOIS["SUL"])
        self.colecao_dois = Sala(n=self.norte_dois,l=self.leste_dois,s=self.sul_dois,o=self.oeste_dois)
        return self.colecao_dois
    
if __name__ == "__main__":
     Passeio()