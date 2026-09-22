"""

Etapa 1 - transformar uma senha em hash

Um hash é uma "impressao digital" de mao unica: da pra gerar a partir
da senha, mas nao da para voltar do hash para a senha. É assim que sistemas guardam senhas
sem guardar a senha em si.

"""
import hashlib

SENHAS_DE_TESTE = [
    "123456",
    "senha123",
    "P@ssw0rd!",
]

def gerar_hash(senha):
    """Devolve o hash SHA-256 da senha, em texto hexadecimal."""
    senha_em_bytes = senha.encode("utf-8")
    resultado = hashlib.sha256(senha_em_bytes)
    return resultado.hexdigest()

if __name__ == "__main__":
    for senha in SENHAS_DE_TESTE:
        print("{}  ->  {}".format(senha, gerar_hash(senha)))