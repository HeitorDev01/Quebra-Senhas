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


def forca_bruta(hash_alvo, alfabeto, tamanho_maximo):
    """Testar todas as combincoes do alfabeto, de 1 ate tamanho_maimo.
    
    Devolve(senha, tentativas) se achar, ou (None, tentativa).
    """
    tentativas = 0

    for tamanho in range(1, tamanho_maximo + 1):
        for combinacao in itertools.product(alfabeto, repeat=tamanho):
            senha = "".join(combinacao)
            tentativas += 1

            if gerar_hash(senha) == hash_alvo:
                return senha, tentativas

    return None, tentativas

if __name__ == "__main__":
    ALFABETO = string.ascii_lowercase + string.digits
    print("Alfabeto: {} caracteres possiveis.".format(len(ALFABETO)))
    print("")

    ALVOS = ["ab", "cor", "gato", "sol42" "4225@!"]

    for alvo in ALVOS:
        hash_alvo = gerar_hash(alvo)

        inicio = time.perf_counter()
        senha, tentativas = forca_bruta(hash_alvo, ALFABETO, tamanho_maximo=6)
        duracao = time.perf_counter() - inicio

        print("senha '{}' ({} caracteres):".format(alvo, len(alvo)))
        print("     quebra em {:.3f}s apos  {:,} tentativas".format(duracao, tentativas))
        print("")