# janese.roxanne.main.py
from _spy.vitollino.main import Cena, Style

STYLE["width"] = 900 # width = 300 (default)
STYLE["heigth"] = "900px" # min-height = "300px"

IMAGEM_QUALQUER = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2F1.bp.blogspot.com%2F-lGK-NZbMSBE%2FUUtrchW3_-I%2FAAAAAAAAIs4%2FhsWa_5_A-1g%2Fs1600%2Ffloresta-amazonica.jpg" # Extensões aceitas: png, jpg, jpeg e gif
IMAGEM_ESQUERDA = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fthumbs.dreamstime.com%2Fb%2Foutono-na-floresta-2905639.jpg" # Extensões aceitas: png, jpg, jpeg e gif
IMAGEM_DIREITA = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.elo7.com.br%2Fproduct%2Fzoom%2F232BA7F%2Fpainel-sublimado-floresta-inverno-3-8x2-6m-paineis-sublimados.jpg" # Extensões aceitas: png, jpg, jpeg e gif
IMAGEM_MEIO = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fs1.1zoom.me%2Fbig0%2F731%2FForests_Spring_Bells_485191.jpg" # Extensões aceitas: png, jpg, jpeg e gif

#nome_da_cena_meio = Cena(IMAGEM_MEIO)
#nome_da_cena_direita = Cena(IMAGEM_DIREITA)
#nome_da_cena_esquerda = Cena(IMAGEM_ESQUERDA)
#nome_da_cena = Cena(IMAGEM_QUALQUER, esquerda=nome_da_cena_esquerda, direita=nome_da_cena_direita, meio=nome_da_cena_meio) 

#nome_da_cena = Cena(IMAGEM_QUALQUER)
#nome_da_cena.vai()


def cria_cena(self):
    self.nome_da_cena = Cena(IMAGEM_QUALQUER)
    self.nome_da_cena.vai()
    
cria_cena()