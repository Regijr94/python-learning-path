# -*- coding: utf-8 -*- 

"""
Aula Completa sobre Listas em Python

Este arquivo serve como um guia completo para entender e trabalhar com listas em Python.
As listas são uma das estruturas de dados mais versáteis e fundamentais da linguagem.

--------------------------------------------------------------------------------------
Conteúdo:
1.  O que são Listas?
2.  Criando Listas
3.  Acessando Elementos (Índices e Slicing)
4.  Métodos de Lista (Modificação e Acesso)
5.  Funções Úteis para Listas
6.  Iteração em Listas
7.  List Comprehensions (Compreensão de Listas)
8.  Copiando Listas (Shallow vs. Deep Copy)
9.  Observações do Básico ao Avançado
--------------------------------------------------------------------------------------
"""

# 1. O que são Listas?
# --------------------
# Uma lista é uma coleção ordenada e mutável de elementos.
# - Ordenada: Os itens mantêm uma ordem definida e não mudam.
# - Mutável: Você pode adicionar, remover ou alterar itens em uma lista após sua criação.
# - Permite Duplicatas: Uma lista pode conter elementos com o mesmo valor.
# - Tipos de Dados: Pode conter diferentes tipos de dados (int, float, str, bool, etc.).

print("--- 1. O que são Listas? ---")
lista_mista = [1, "Python", 3.14, True, [1, 2, 3]]
print(f"Exemplo de lista com tipos de dados mistos: {lista_mista}\n")


# 2. Criando Listas
# -----------------
# Você pode criar listas usando colchetes `[]` ou o construtor `list()`.

print("--- 2. Criando Listas ---")
# Usando colchetes (forma mais comum)
lista_frutas = ["maçã", "banana", "cereja"]
print(f"Lista criada com colchetes: {lista_frutas}")

# Usando o construtor list()
lista_numeros = list((1, 2, 3, 4, 5)) # Note que `list()` recebe um iterável (como uma tupla)
print(f"Lista criada com o construtor list(): {lista_numeros}\n")


# 3. Acessando Elementos (Índices e Slicing)
# ------------------------------------------
# O acesso é feito por meio de índices, começando em 0.

print("--- 3. Acessando Elementos ---")
linguagens = ["Python", "Java", "C#", "JavaScript", "Ruby"]

# Acesso por índice positivo (começa do 0)
print(f"Primeiro elemento (índice 0): {linguagens[0]}")
print(f"Terceiro elemento (índice 2): {linguagens[2]}")

# Acesso por índice negativo (começa do -1 para o último elemento)
print(f"Último elemento (índice -1): {linguagens[-1]}")
print(f"Penúltimo elemento (índice -2): {linguagens[-2]}")

# Slicing (Fatiamento): Acessando um subconjunto da lista
# sintaxe: lista[start:stop:step]
print(f"Do segundo ao quarto elemento (índices 1 a 3): {linguagens[1:4]}")
print(f"Do início ao terceiro elemento (índices 0 a 2): {linguagens[:3]}")
print(f"Do terceiro elemento até o final: {linguagens[2:]}")
print(f"Toda a lista com passo 2 (pega um, pula um): {linguagens[::2]}\n")


# 4. Métodos de Lista
# -------------------
# Métodos são funções que pertencem ao objeto lista e permitem manipulá-la.

print("--- 4. Métodos de Lista ---")
numeros = [1, 2, 3, 4]
print(f"Lista original: {numeros}")

# append(): Adiciona um item ao final da lista
numeros.append(5)
print(f"Após append(5): {numeros}")

# insert(): Adiciona um item em uma posição específica
numeros.insert(0, 0) # Adiciona 0 na posição 0
print(f"Após insert(0, 0): {numeros}")

# extend(): Adiciona todos os itens de um iterável (outra lista, tupla, etc.)
numeros.extend([6, 7, 8])
print(f"Após extend([6, 7, 8]): {numeros}")

# remove(): Remove a primeira ocorrência de um valor
numeros.remove(8)
print(f"Após remove(8): {numeros}")

# pop(): Remove e retorna o item de uma posição. Se o índice não for especificado, remove o último.
item_removido = numeros.pop(0)
print(f"Após pop(0), item removido foi {item_removido}: {numeros}")
ultimo_item = numeros.pop()
print(f"Após pop(), último item removido foi {ultimo_item}: {numeros}")

# index(): Retorna o índice da primeira ocorrência de um valor
indice_do_tres = numeros.index(3)
print(f"O valor 3 está no índice: {indice_do_tres}")

# count(): Conta o número de vezes que um valor aparece
numeros.append(3) # Adicionando outro 3 para o exemplo
print(f"A lista agora é: {numeros}")
print(f"O número 3 aparece {numeros.count(3)} vezes")

# sort(): Ordena a lista in-place (modifica a lista original)
numeros_desordenados = [3, 1, 4, 1, 5, 9, 2, 6]
numeros_desordenados.sort()
print(f"Lista ordenada (crescente): {numeros_desordenados}")
numeros_desordenados.sort(reverse=True)
print(f"Lista ordenada (decrescente): {numeros_desordenados}")

# reverse(): Inverte a ordem dos elementos in-place
numeros.reverse()
print(f"Lista invertida: {numeros}")

# clear(): Remove todos os elementos da lista
numeros.clear()
print(f"Após clear(): {numeros}\n")


# 5. Funções Úteis para Listas
# ----------------------------
# Funções built-in do Python que podem ser usadas com listas.

print("--- 5. Funções Úteis para Listas ---")
valores = [8, 2, 10, 4, 6]
print(f"Lista de valores: {valores}")

# len(): Retorna o número de elementos
print(f"Tamanho da lista (len()): {len(valores)}")

# sum(): Retorna a soma de todos os elementos (funciona apenas com números)
print(f"Soma dos elementos (sum()): {sum(valores)}")

# min(): Retorna o menor elemento
print(f"Menor elemento (min()): {min(valores)}")

# max(): Retorna o maior elemento
print(f"Maior elemento (max()): {max(valores)}")

# sorted(): Retorna uma NOVA lista ordenada (não modifica a original)
lista_original = [3, 1, 4, 2]
lista_ordenada_nova = sorted(lista_original)
print(f"A lista original {lista_original} não foi modificada.")
print(f"A nova lista ordenada é: {lista_ordenada_nova}\n")


# 6. Iteração em Listas
# ---------------------
# Percorrendo os elementos de uma lista usando loops.

print("--- 6. Iteração em Listas ---")
cores = ["vermelho", "verde", "azul"]

# Exemplo 1: Usando um loop 'for' (forma mais comum)
print("Iterando com 'for':")
for cor in cores:
    print(f"- {cor}")

# Exemplo 2: Usando 'for' com 'enumerate' para obter o índice e o valor
print("\nIterando com 'enumerate':")
for indice, cor in enumerate(cores):
    print(f"- Índice {indice}: {cor}")

# Exemplo 3: Usando um loop 'while'
print("\nIterando com 'while':")
i = 0
while i < len(cores):
    print(f"- {cores[i]}")
    i += 1

# Exemplo 4 (Avançado): Loop 'while' para consumir uma lista
print("\nConsumindo uma lista com 'while' e '.pop()':")
tarefas = ["Lavar louça", "Passear com o cachorro", "Fazer compras"]
while tarefas: # O loop continua enquanto a lista não estiver vazia
    tarefa_atual = tarefas.pop(0) # Remove e obtém o primeiro item
    print(f"Realizando: {tarefa_atual}")
print(f"Tarefas restantes: {tarefas}\n")


# 7. List Comprehensions (Compreensão de Listas)
# ----------------------------------------------
# Uma forma concisa e elegante de criar listas.

print("--- 7. List Comprehensions ---")
# Exemplo 1: Criar uma lista com os quadrados dos números de 0 a 9
quadrados_comprehension = [x**2 for x in range(10)]
print(f"Quadrados (comprehension): {quadrados_comprehension}")

# Exemplo 2: Criar uma lista de números pares de 0 a 19 com uma condição
pares = [x for x in range(20) if x % 2 == 0]
print(f"Números pares de 0 a 19: {pares}")

# Exemplo 3: Usando if/else (expressão condicional)
# A sintaxe é `[valor_se_verdadeiro if condicao else valor_se_falso for item in iteravel]`
par_ou_impar = ["par" if num % 2 == 0 else "ímpar" for num in range(10)]
print(f"Classificação par/ímpar: {par_ou_impar}")

# Exemplo 4 (Avançado): List comprehension aninhada para criar uma matriz
matriz = [[linha * 3 + col + 1 for col in range(3)] for linha in range(3)]
print(f"Matriz 3x3 criada com list comprehension aninhada: {matriz}\n")


# 8. Copiando Listas
# ------------------
# A forma como você copia uma lista é importante para evitar modificações indesejadas.

print("--- 8. Copiando Listas ---")
lista_a = [1, 2, 3]

# Atribuição simples (NÃO é uma cópia, ambas as variáveis apontam para a mesma lista)
lista_b = lista_a
lista_b.append(4)
print(f"Lista A após modificar B (atribuição simples): {lista_a}")
print(f"Lista B: {lista_b}")
print("-> Ambas foram modificadas!\n")

# Shallow Copy (Cópia Rasa) - Usando copy() ou slicing [:]
# Cria um novo objeto lista, mas se a lista contiver outras listas (aninhadas),
# essas listas internas não são copiadas, apenas suas referências.
lista_c = [10, 20, 30]
lista_d = lista_c.copy() # ou lista_d = lista_c[:]
lista_d.append(40)

print(f"Lista C (original): {lista_c}")
print(f"Lista D (cópia): {lista_d}")
print("-> Apenas a cópia foi modificada, pois a lista não tem elementos aninhados.\n")

# Exemplo de problema com shallow copy em listas aninhadas
lista_aninhada_1 = [1, [10, 20]]
lista_aninhada_2 = lista_aninhada_1.copy()
lista_aninhada_2[1].append(30) # Modificando a lista interna

print(f"Lista aninhada 1: {lista_aninhada_1}")
print(f"Lista aninhada 2: {lista_aninhada_2}")
print("-> Ambas foram modificadas na parte interna!\n")

# Deep Copy (Cópia Profunda) - Usando o módulo 'copy'
# Cria uma cópia recursiva de todos os objetos, incluindo os aninhados.
import copy

lista_e = [1, [10, 20]]
lista_f = copy.deepcopy(lista_e)
lista_f[1].append(30)

print(f"Lista E (original com deepcopy): {lista_e}")
print(f"Lista F (cópia profunda): {lista_f}")
print("-> Apenas a cópia profunda foi modificada, incluindo a parte interna.\n")


# 9. Observações do Básico ao Avançado
# -------------------------------------
print("--- 9. Observações do Básico ao Avançado ---")

# --- Nível Básico ---
# Mutabilidade: Listas são mutáveis, o que significa que seu conteúdo pode ser alterado
# após a criação. Isso é poderoso, mas pode levar a efeitos colaterais se não for gerenciado.
l_mutavel = [1, 2, 3]
l_referencia = l_mutavel
l_referencia.append(4)
print(f"A lista original foi alterada por uma referência: {l_mutavel}")

# Heterogeneidade: Listas podem conter tipos de dados diferentes, mas para clareza e 
# manutenibilidade do código, é geralmente uma boa prática manter listas homogêneas.

# Performance de Operações Comuns:
# - Acesso por índice (ex: `minha_lista[5]`): É muito rápido, tempo constante O(1).
# - `append()`: Geralmente muito rápido, tempo constante O(1).
# - `insert()` e `pop(i)`: Lento, pois pode precisar deslocar muitos elementos, tempo linear O(n).
# - `in` (verificar se um item existe): Lento, precisa varrer a lista, tempo linear O(n).

# --- Nível Intermediário ---
# Usando Listas como Pilhas (Stack - LIFO: Last-In, First-Out)
# É muito eficiente usar `append()` para adicionar (push) e `pop()` para remover (pop).
pilha = [1, 2, 3]
pilha.append(4) # Push
pilha.append(5) # Push
print(f"Pilha: {pilha}")
print(f"Item removido da pilha (pop): {pilha.pop()}")
print(f"Pilha após pop: {pilha}")

# Usando Listas como Filas (Queue - FIFO: First-In, First-Out)
# Usar `append()` para adicionar e `pop(0)` para remover da frente é INEFICIENTE (O(n)).
# Para filas eficientes, use `collections.deque`.
from collections import deque
fila_eficiente = deque([1, 2, 3])
fila_eficiente.append(4) # Adiciona no final
print(f"Fila eficiente: {fila_eficiente}")
print(f"Item removido da fila (popleft): {fila_eficiente.popleft()}") # popleft() é O(1)
print(f"Fila eficiente após popleft: {fila_eficiente}")

# Diferença entre .sort() e sorted():
# - `minha_lista.sort()`: Ordena a lista *in-place* (modifica a original) e retorna `None`.
# - `nova_lista = sorted(minha_lista)`: Cria e retorna uma *nova* lista ordenada, não altera a original.
lista_para_ordenar = [5, 1, 4, 3]
print(f"\nLista original para ordenação: {lista_para_ordenar}")
retorno_sort = lista_para_ordenar.sort()
print(f"Após .sort(), a lista original mudou: {lista_para_ordenar}")
print(f"O método .sort() retorna: {retorno_sort}")

lista_para_sorted = [5, 1, 4, 3]
nova_lista_ordenada = sorted(lista_para_sorted)
print(f"A função sorted() não muda a lista original: {lista_para_sorted}")
print(f"A função sorted() retorna uma nova lista: {nova_lista_ordenada}")

# --- Nível Avançado ---
# Cuidado com Argumentos de Função Mutáveis
# Usar uma lista (ou outro tipo mutável) como valor padrão de um argumento de função é perigoso.
# O objeto da lista é criado UMA VEZ e reutilizado em todas as chamadas subsequentes.

def adiciona_item(item, lista=[]): # Prática perigosa!
    lista.append(item)
    return lista

print("\nDemonstração do perigo de argumentos mutáveis:")
print(adiciona_item(1)) # Retorna [1]
print(adiciona_item(2)) # Retorna [1, 2] - Efeito colateral indesejado!

# A forma correta é usar `None` como padrão e criar a lista dentro da função.
def adiciona_item_correto(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista

print("\nForma correta de usar listas em argumentos:")
print(adiciona_item_correto(1)) # Retorna [1]
print(adiciona_item_correto(2)) # Retorna [2] - Comportamento esperado

# Listas vs. Tuplas
# - Use Listas quando precisar de uma coleção de itens que pode mudar (adicionar, remover, reordenar).
# - Use Tuplas quando tiver uma coleção de itens que não deve mudar (imutável).
# Tuplas são geralmente mais eficientes em termos de memória e um pouco mais rápidas para acessar.
# Elas também podem ser usadas como chaves de dicionário, ao contrário das listas.

coordenadas_lista = [34.0522, -118.2437] # Poderia ser alterado
coordenadas_tupla = (34.0522, -118.2437) # Constante, mais seguro para dados que não mudam

dic_exemplo = {coordenadas_tupla: "Los Angeles"}
# dic_exemplo = {coordenadas_lista: "Los Angeles"} # Isso geraria um TypeError: unhashable type: 'list'

print(f"\nTupla como chave de dicionário: {dic_exemplo}")
