"""

Etapa 1 - transformar uma senha em hash

Um hash é uma "impressao digital" de mao unica: da pra gerar a partir
da senha, mas nao da para voltar do hash para a senha. É assim que sistemas guardam senhas
sem guardar a senha em si.

"""
import hashlib

SENHA_DE_TESTE = [
    "123456",
    "senha123",
    "P@ssw0rd!",
]
