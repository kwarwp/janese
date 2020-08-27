# janese.cenas.cru.py
# SPDX-License-Identifier: GPL-3.0-or-later
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

SALA="https://p2.trrsf.com/image/fget/cf/460/0/images.terra.com/2018/03/23/modelos-de-escadas-linear-sem-corrimao.jpg"
ESCRITORIO="https://www.viveremcasa.com/wp-content/uploads/2018/02/cadeira-home-office-preta-couro-comprar.jpg"
CORREDOR="https://i.pinimg.com/originals/b0/de/8a/b0de8ab7aa396b97d7f43d8289727146.jpg"
QUARTO="https://i.pinimg.com/originals/61/af/f4/61aff4dcbf8fdfe0ec7faa77bf310f64.jpg"
BANHEIRO="https://www.iquilibrio.com/blog/wp-content/uploads/2017/03/71245-feng-shui-no-banheiro-veja-como-aplicar-em-sua-casa-1.jpg"
COZINHA="https://i.pinimg.com/originals/18/bf/1b/18bf1b40b41a7d86b5913c38f6492799.jpg"


STYLE["width"] = 900
STYLE["heigth"] = 900

class botao():

    def __init__(self,Elemento, acao, caminho, event=None):
        self.Elemento = _Elemento
        self.acao = clica
        self.caminho = caminho
        
    def _Elemento(self, olho="https://i.imgur.com/JuvyDuW.png"):
        from _spy.vitollino.main import Elemento
        self._Elemento = Elemento(self.olho, h, w, x, y, cena=cena)
        
    def clica(self):
        return _Elemento.elt.bind("click", caminho)
    
    def caminho(self):
    
class Passeio():

    def __init__(self):
        self.escrit = Cena(SALA)
        self.cozinha = Cena(COZINHA, direita = self.escrit)
        
        self.botaoteste = botao(
        
        self.colecao = Sala(n=self.escrit, l= self.cozinha, o= self.cozinha)
        self.colecao.norte.vai()
    
if __name__ == "__main__":
    Passeio()