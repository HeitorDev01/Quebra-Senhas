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
        if r["quebrado"]:
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
        gerar_hash("123456"),
        gerar_hash("P@ssw0rd!"),
        gerar_hash("password"),
        gerar_hash("xk9-mancha-vento-42"),
        gerar_hash("dragon"),
    ]

    palavras = carregar_wordlist("wordlist.txt")

    inicio = time.perf_counter()
    resultados = atacar_lista(HASHES_ALVO, palavras)
    duracao = time.perf_counter() - inicio

    imprimir_relatorio(resultados, duracao)