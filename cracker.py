"""

Etapa 4 - Quebrar uma lista de hashes e gerar um relatorio.

Um atacandte raramente tem um hash só. Ele rouba o banco de dados inteiro
de senhas de um site e ataca todos de uma vez. Esta etapa faz isso:
recebe vários hash, ataca cada um, e mede a taxa de sucesso, quantas
por cento das senhas daquele "vazamento" foram quebradas

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

def atacar_lista(hashes, palavras):
    """Ataca varios hashes. Devolve uma lista de resultado."""
    resultados = []

    for hash_alvo in hashes:
        senha = atacar(hash_alvo, palavras)
        resultados.append({
            "hash": hash_alvo,
            "senha": senha,
            "quebrado": senha is not None,
        })
    return resultados

def imprimir_relatorio(resultados, duracao):
    """Mostra o que foi quebrado e a taxa de sucesso."""
    total = len(resultados)
    quebrados = [r for r in resultados if r["quebrado"]]

    print("")
    print("=" * 56)
    print(" RELATORIO DO ATAQUE")
    print("=" * 56)

    for r in resultados:
        if r["quebrados"]:
            print(" [QUEBRADO]  {:<20} {}...".format(r["senha"], r["hash"][:12]))
        else:
            print(" [resistiu]  {:<20}  {}...".format("-", r["hash"][:12]))

    print("-" * 56)

    taxa = (len(quebrados) / total * 100) if total else 0
    print("  {} de {} senhas quebradas ({:.0f}%) em {:.4f}s".format(
        len(quebrados), total, taxa, duracao
    ))
    print("=" * 56)
    print("")

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