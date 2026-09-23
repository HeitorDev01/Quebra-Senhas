"""
Etapa 5 - Força Bruta

O dicionario só acha o que na lista. A força bruta nao usa lista:
tenta TODAS as combinalçoes possiveis de caracteres uma por uma.
Sempre acha a senha, a pergunta e so quanto tempo leva. E o tempo
cresce de forma explosiva com o temanho da senha. É isso que esta
etapa mostra.
"""
import hashlib
import itertools
import string
import time

def gerar_hash(senha):
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()