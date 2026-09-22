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

def atacar(hahs_alvo, palavras):
    """Testar cada palavra contra o hash. Devolve a senha, ou None."""
    for palavra in palavras:
        if gerar_hash(palavra) == hahs_alvo:
            return palavra

    return None

if __name__ == "__main__":
    HASHES_ALVO = [
        "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",
        "0e44ce7308af2b3de5232e4616403ce7d49ba2aec83f79c196409556422a4927",
        "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
    ]

    palavras = carregar_wordlist("wordlist.txt")
    print("Wordlist carregada: {} senhas.".format(len(palavras)))
    print("")

    for hash_alvo in HASHES_ALVO:
        inicio = time.perf_counter()
        senha = atacar(hash_alvo, palavras)
        duracao = time.perf_counter() - inicio

        if senha is not None:
            print("QUEBRADO em {:.4f}s -> {}".format(duracao, senha))
        else:
            print("nao quebrado ({:.4f}s) -> {}...".format(duracao, hash_alvo[:16]))