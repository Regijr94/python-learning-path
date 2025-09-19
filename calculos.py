# -*- coding: utf-8 -*-

"""Módulo de cálculos dentro de meu_pacote."""

# Exemplo de importação relativa (Tópico 8 do guia)
from . import utils

def somar(a, b):
    utils.log("Somando...")
    return a + b