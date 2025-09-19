# -*- coding: utf-8 -*-

"""
Guia Completo de Tuplas em Python: Do Básico ao Avançado

Este arquivo é um guia de estudo completo sobre tuplas em Python,
estruturado como uma aula progressiva.

--------------------------------------------------------------------------------------
Conteúdo:
1.  O que são Tuplas?
2.  Criando Tuplas
3.  Acessando Elementos (Indexação e Fatiamento)
4.  Desempacotamento de Tuplas (Unpacking)
5.  Métodos e Operações com Tuplas
6.  Tópicos Avançados e Casos de Uso
--------------------------------------------------------------------------------------
"""

# 1. O que são Tuplas?
# --------------------
# Uma tupla é uma coleção de elementos **ordenada** e **imutável**.
#
# - Ordenada: Os itens mantêm uma ordem definida que não muda.
# - Imutável: Uma vez criada, você não pode alterar, adicionar ou remover itens.
# - Permite Duplicatas: Uma tupla pode conter elementos com o mesmo valor.
# - Heterogênea: Pode conter diferentes tipos de dados (int, str, list, etc.).

print("--- 1. O que são Tuplas? (10 Exemplos de uso) ---")

# Exemplo 1: Coordenadas geográficas (latitude, longitude)
coordenadas = (-23.5505, -46.6333)
print(f"1. Coordenadas de São Paulo: {coordenadas}")

# Exemplo 2: Cores no padrão RGB
cor_vermelha = (255, 0, 0)
print(f"2. Cor vermelha em RGB: {cor_vermelha}")

# Exemplo 3: Representando um registro de banco de dados
registro_usuario = (101, "Ana Silva", "ana.silva@example.com", True)
print(f"3. Registro de usuário: {registro_usuario}")

# Exemplo 4: Tupla com um único elemento (a vírgula é essencial)
tupla_um_elemento = ("único",)
print(f"4. Tupla de um elemento: {tupla_um_elemento}, tipo: {type(tupla_um_elemento)}")

# Exemplo 5: Tupla vazia
tupla_vazia = ()
print(f"5. Tupla vazia: {tupla_vazia}")

# Exemplo 6: Tupla com tipos de dados mistos
dados_mistos = (1, "texto", 3.14, [1, 2], {"chave": "valor"})
print(f"6. Tupla com dados mistos: {dados_mistos}")

# Exemplo 7: Tupla de tuplas (matriz ou tabela)
matriz_2x2 = ((1, 2), (3, 4))
print(f"7. Matriz 2x2: {matriz_2x2}")

# Exemplo 8: Retorno de uma função com múltiplos valores
def obter_min_max(lista):
    return min(lista), max(lista)
minimo, maximo = obter_min_max([1, 5, 2, 8])
print(f"8. Retorno de função (min, max): ({minimo}, {maximo})")

# Exemplo 9: Itens de um dicionário (pares chave-valor)
itens_dict = {"a": 1, "b": 2}.items() # Retorna uma view, que pode ser convertida
print(f"9. Itens de um dicionário: {tuple(itens_dict)}")

# Exemplo 10: Tupla com valores duplicados
duplicatas = (1, 2, 2, 3, 3, 3, 4)
print(f"10. Tupla com duplicatas: {duplicatas}\n")


# 2. Criando Tuplas
# -----------------
# Tuplas podem ser criadas com ou sem parênteses, ou usando o construtor `tuple()`.

print("--- 2. Criando Tuplas (10 Exemplos) ---")

# Exemplo 1: Usando parênteses (forma mais comum)
t1 = (1, 2, 3)
print(f"1. Com parênteses: {t1}")

# Exemplo 2: Sem parênteses (empacotamento de tupla ou "tuple packing")
t2 = 4, 5, 6
print(f"2. Sem parênteses (packing): {t2}, tipo: {type(t2)}")

# Exemplo 3: Criando uma tupla vazia
t3 = ()
print(f"3. Tupla vazia: {t3}")

# Exemplo 4: Criando uma tupla com um único item (requer vírgula)
t4 = (7,)
print(f"4. Tupla de um item: {t4}")

# Exemplo 5: Usando o construtor `tuple()` com uma lista
t5 = tuple([8, 9, 10])
print(f"5. Construtor com lista: {t5}")

# Exemplo 6: Usando `tuple()` com uma string (cria uma tupla de caracteres)
t6 = tuple("Python")
print(f"6. Construtor com string: {t6}")

# Exemplo 7: Usando `tuple()` com um `range`
t7 = tuple(range(5))
print(f"7. Construtor com range: {t7}")

# Exemplo 8: Usando `tuple()` com as chaves de um dicionário
d = {"a": 1, "b": 2}
t8 = tuple(d.keys())
print(f"8. Construtor com chaves de dict: {t8}")

# Exemplo 9: Usando `tuple()` com os valores de um dicionário
t9 = tuple(d.values())
print(f"9. Construtor com valores de dict: {t9}")

# Exemplo 10: Usando `tuple()` com um gerador (generator expression)
t10 = tuple(x*x for x in range(5))
print(f"10. Construtor com gerador: {t10}\n")


# 3. Acessando Elementos (Indexação e Fatiamento)
# -----------------------------------------------
# O acesso é feito por índices (começando em 0) e fatiamento (slicing).

print("--- 3. Acessando Elementos (10 Exemplos) ---")
dados = ("a", "b", "c", "d", "e", "f", "g")

print(f"1. Primeiro elemento (índice 0): {dados[0]}")
print(f"2. Último elemento (índice -1): {dados[-1]}")
print(f"3. Terceiro elemento (índice 2): {dados[2]}")
print(f"4. Fatiamento do 2º ao 4º elemento (índices 1 a 3): {dados[1:4]}")
print(f"5. Fatiamento do início ao 3º elemento: {dados[:3]}")
print(f"6. Fatiamento do 4º elemento até o final: {dados[3:]}")
print(f"7. Fatiamento com passo 2 (pega um, pula um): {dados[::2]}")
print(f"8. Invertendo a tupla com fatiamento: {dados[::-1]}")

tupla_aninhada = (1, (2, 3), (4, (5, 6)))
print(f"9. Acessando elemento aninhado: {tupla_aninhada[2][1][0]}") # Acessa o 5

try:
    dados[10]
except IndexError as e:
    print(f"10. Tentativa de acesso a índice inválido: {e}\n")


# 4. Desempacotamento de Tuplas (Unpacking)
# -----------------------------------------
# Atribuir os valores de uma tupla a múltiplas variáveis de uma só vez.

print("--- 4. Desempacotamento de Tuplas (10 Exemplos) ---")

# Exemplo 1: Desempacotamento básico
ponto = (10, 20, 5)
x, y, z = ponto
print(f"1. Desempacotamento básico: x={x}, y={y}, z={z}")

# Exemplo 2: Troca de valores de variáveis (swap)
a, b = 10, 20
a, b = b, a # Cria uma tupla (20, 10) e a desempacota em a, b
print(f"2. Troca de variáveis: a={a}, b={b}")

# Exemplo 3: Usando `*` para capturar múltiplos itens (extended unpacking)
numeros = (1, 2, 3, 4, 5)
primeiro, *meio, ultimo = numeros
print(f"3. Usando `*` no meio: primeiro={primeiro}, meio={meio}, ultimo={ultimo}")

# Exemplo 4: Usando `*` no início
*iniciais, penultimo, ultimo_val = numeros
print(f"4. Usando `*` no início: iniciais={iniciais}, penultimo={penultimo}, ultimo_val={ultimo_val}")

# Exemplo 5: Ignorando valores com `_`
data = (2023, 10, 26)
ano, _, dia = data
print(f"5. Ignorando valores com `_`: ano={ano}, dia={dia}")

# Exemplo 6: Desempacotamento em loops `for`
lista_de_pontos = [(1, 2), (3, 4), (5, 6)]
print("6. Desempacotamento em loop `for`:")
for px, py in lista_de_pontos:
    print(f"   Ponto: ({px}, {py})")

# Exemplo 7: Desempacotamento do retorno de `enumerate`
print("7. Desempacotamento com `enumerate`:")
for indice, valor in enumerate(["a", "b", "c"]):
    print(f"   Índice {indice}: {valor}")

# Exemplo 8: Desempacotamento aninhado
dados_complexos = ("Ana", 30, ("Rua A", 123))
nome, idade, (rua, numero) = dados_complexos
print(f"8. Desempacotamento aninhado: {nome} mora na {rua}, nº {numero}")

# Exemplo 9: Desempacotamento de chaves e valores de um dicionário
print("9. Desempacotamento de itens de dict:")
for chave, valor in {"x": 1, "y": 2}.items():
    print(f"   {chave} -> {valor}")

# Exemplo 10: Erro ao desempacotar (número de variáveis incorreto)
try:
    val1, val2 = (10, 20, 30)
except ValueError as e:
    print(f"10. Erro de desempacotamento: {e}\n")


# 5. Métodos e Operações com Tuplas
# ---------------------------------
# Tuplas têm apenas dois métodos, `.count()` e `.index()`, por serem imutáveis.

print("--- 5. Métodos e Operações (10 Exemplos) ---")
t = (1, 2, 3, 2, 4, 2, 5)

print(f"1. `.count(2)`: O número 2 aparece {t.count(2)} vezes.")
print(f"2. `.count(99)`: O número 99 aparece {t.count(99)} vezes.")
print(f"3. `.index(4)`: O número 4 está no índice {t.index(4)}.")

try:
    t.index(99)
except ValueError as e:
    print(f"4. `.index(99)`: {e}")

# Operações
t1 = (1, 2)
t2 = (3, 4)
print(f"5. Concatenação (+): {t1 + t2}")
print(f"6. Repetição (*): {t1 * 3}")
print(f"7. Verificação de existência (`in`): {3 in t2}")
print(f"8. Verificação de não existência (`not in`): {5 not in t2}")
print(f"9. Tamanho da tupla (`len`): {len(t)}")
print(f"10. Funções `min`, `max`, `sum`: min={min(t)}, max={max(t)}, sum={sum(t)}\n")


# 6. Tópicos Avançados e Casos de Uso
# -----------------------------------

print("--- 6. Tópicos Avançados e Casos de Uso (10 Exemplos) ---")

# Exemplo 1: Tuplas como chaves de dicionário (listas não podem)
localizacoes = {
    (34.0522, -118.2437): "Los Angeles",
    (40.7128, -74.0060): "Nova York"
}
print(f"1. Tupla como chave de dicionário: {localizacoes[(40.7128, -74.0060)]}")

# Exemplo 2: `namedtuple` para tuplas mais legíveis
from collections import namedtuple
Ponto = namedtuple('Ponto', ['x', 'y', 'z'])
p1 = Ponto(10, 20, 30)
print(f"2. Usando namedtuple: p1.x = {p1.x}, p1[1] = {p1[1]}")

# Exemplo 3: Imutabilidade de tuplas com itens mutáveis
tupla_mutavel = (1, 2, [3, 4])
print(f"3. Tupla original com item mutável: {tupla_mutavel}")
tupla_mutavel[2].append(5) # A lista dentro da tupla PODE ser alterada
print(f"   Tupla após modificar a lista interna: {tupla_mutavel}")

# Exemplo 4: Eficiência de memória e performance
# Tuplas geralmente usam menos memória que listas com os mesmos elementos.
import sys
lista_ex = [1, 2, 3, 4, 5]
tupla_ex = (1, 2, 3, 4, 5)
print(f"4. Memória (lista): {sys.getsizeof(lista_ex)} bytes, Memória (tupla): {sys.getsizeof(tupla_ex)} bytes")

# Exemplo 5: Garantindo a integridade dos dados
# Usar tupla para uma sequência que não deve ser alterada.
DIAS_DA_SEMANA = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
print(f"5. Constantes com tupla: {DIAS_DA_SEMANA[0]}")

# Exemplo 6: Conversão entre lista e tupla
lista_original = [10, 20, 30]
tupla_convertida = tuple(lista_original)
lista_reconvertida = list(tupla_convertida)
print(f"6. Lista -> Tupla: {tupla_convertida}, Tupla -> Lista: {lista_reconvertida}")

# Exemplo 7: Usando tuplas em `set`
# Listas não podem ser adicionadas a um set, mas tuplas sim.
conjunto_de_pontos = {(1, 2), (3, 4), (1, 2)}
print(f"7. Tuplas em um set (remove duplicatas): {conjunto_de_pontos}")

# Exemplo 8: `zip` para combinar sequências em tuplas
nomes = ["Ana", "Beto", "Caio"]
idades = [25, 30, 28]
combinado = tuple(zip(nomes, idades))
print(f"8. Combinando listas com `zip`: {combinado}")

# Exemplo 9: Argumentos de função com `*args`
# `*args` empacota múltiplos argumentos posicionais em uma tupla.
def soma_tudo(*args):
    print(f"   Argumentos recebidos como tupla: {args}")
    return sum(args)
print(f"9. Função com `*args`: {soma_tudo(1, 2, 3, 4, 5)}")

# Exemplo 10: `isinstance` para checar o tipo
obj = (1, 2)
if isinstance(obj, tuple):
    print("10. `isinstance` confirma que o objeto é uma tupla.")

print("-" * 20 + "\n")