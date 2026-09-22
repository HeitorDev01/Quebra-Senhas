"""

Etapa 3 - ataque de dicionario.

A lista de tentativas sai do codigo e vira um arquivo: uma "wordlist".
O ataque de dicionario é o mais comum do mundo real - nao tenta todas as
comninaçoes possiveis, so as senhas que as pessoas de fato usam.
Um arquivo desses, com milhoes de senhas vazadas, cabe num pen drive.
"""
import hashlib
import time

def gerar_hash(senha):
    """Devolve o hash SHA-256 da senha, em texto hexadecimal."""
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()

def carregar_wordlist(caminho):
    """Le o arquivo de senhas e devolve uma lista, sem quebras de linha"""
    palavras =[]

    with open(caminho, "r", encoding="utf-8", errors="ignore") as arquivo:
        for linha in arquivo:
            palavra = linha.strip()
            if palavra:
                palavras.append(palavra)
    return palavras


def senha_confere(senha, hash_alvo):
    """Devolve True se a senha, uma vez hasheada, bate com o hash-alvo."""
    return gerar_hash(senha) == hash_alvo


if __name__ == "__main__":
    tentativas = ["adimin", "123456", "P@ssw0rd!", "qwerty"]

    for hash_alvo in HASHES_ALVO:
        print("Alvo:", hash_alvo)

        for tentativa in tentativas:
            if senha_confere(tentativa, hash_alvo):
                print(" QUEBRADO -> a senha era: {}".format(tentativa))
                break
        else:
            print("   nao quebrado com esta lista")
        print("")