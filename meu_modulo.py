# -*- coding: utf-8 -*-

"""
Este é um módulo de exemplo para o arquivo modulos_guide.py.
"""

print("Módulo 'meu_modulo' foi importado e executado.")

PI = 3.14159

def saudar(nome):
    """Retorna uma saudação."""
    return f"Olá do meu módulo, {nome}!"

class Ferramenta:
    """Uma classe de exemplo."""
    def __init__(self, nome="genérica"):
        self.nome = nome