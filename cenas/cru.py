# janese.cenas.cru.py
# SPDX-License-Identifier: GPL-3.0-or-later
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
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
        self.fundo