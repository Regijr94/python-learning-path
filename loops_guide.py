# -*- coding: utf-8 -*-

"""
Guia Completo de Loops em Python: Do Básico ao Avançado

Este arquivo é um guia de estudo completo sobre as estruturas de repetição (loops)
em Python, cobrindo `for` e `while`, além de conceitos associados.

--------------------------------------------------------------------------------------
Conteúdo:

-- Parte 1: Fundamentos --
1.  O Loop `for`: Iterando sobre Sequências
2.  A Função `range()`: Repetindo um Número Fixo de Vezes
3.  O Loop `while`: Repetindo com Base em uma Condição
4.  A Declaração `break`: Saindo de um Loop
5.  A Declaração `continue`: Pulando uma Iteração

-- Parte 2: Tópicos Intermediários e Avançados --
6.  A Cláusula `else` em Loops
7.  Loops Aninhados (Nested Loops)
8.  Iterando sobre Dicionários
9.  A Função `enumerate()`: Obtendo Índice e Valor
10. A Função `zip()`: Iterando sobre Múltiplas Sequências
--------------------------------------------------------------------------------------
"""

# ====================================================================================
# Parte 1: Fundamentos
# ====================================================================================

# 1. O Loop `for`: Iterando sobre Sequências
# -------------------------------------------
# O loop `for` é usado para iterar sobre os itens de qualquer sequência (uma lista,
# uma tupla, um dicionário, um conjunto ou uma string), na ordem em que aparecem.

print("--- 1. O Loop `for` (6 Exemplos) ---")

# Exemplo 1: Iterando sobre uma lista de strings
frutas = ["maçã", "banana", "cereja"]
print("1. Iterando sobre uma lista de frutas:")
for fruta in frutas:
    print(f"   - Gosto de {fruta}")

# Exemplo 2: Iterando sobre uma string
palavra = "Python"
print("\n2. Iterando sobre os caracteres de uma string:")
for letra in palavra:
    print(f"   Letra: {letra}")

# Exemplo 3: Iterando sobre uma tupla de números para calcular a soma
numeros = (10, 20, 30, 40, 50)
soma = 0
for num in numeros:
    soma += num
print(f"\n3. A soma dos números na tupla é: {soma}")

# Exemplo 4: Modificando a saída durante a iteração
nomes = ["ana", "beto", "caio"]
print("\n4. Imprimindo nomes capitalizados:")
for nome in nomes:
    print(f"   - {nome.title()}")

# Exemplo 5: Iterando sobre uma lista de tipos mistos
dados_mistos = [1, "texto", 3.14, True]
print("\n5. Iterando sobre dados de tipos mistos:")
for item in dados_mistos:
    print(f"   - Item: {item} (Tipo: {type(item).__name__})")

# Exemplo 6: Usando o loop `for` para criar uma nova lista
quadrados = []
for i in [1, 2, 3, 4, 5]:
    quadrados.append(i ** 2)
print(f"\n6. Nova lista de quadrados criada com loop: {quadrados}")
print("-" * 20 + "\n")


# 2. A Função `range()`: Repetindo um Número Fixo de Vezes
# --------------------------------------------------------
# A função `range()` gera uma sequência de números, sendo muito útil em loops `for`.

print("--- 2. A Função `range()` (6 Exemplos) ---")

# Exemplo 1: `range(stop)` - Gera números de 0 até `stop-1`
print("1. Loop de 0 a 4:")
for i in range(5):
    print(f"   - Número {i}")

# Exemplo 2: `range(start, stop)` - Gera números de `start` até `stop-1`
print("\n2. Loop de 2 a 6:")
for i in range(2, 7):
    print(f"   - Número {i}")

# Exemplo 3: `range(start, stop, step)` - Gera números com um passo
print("\n3. Números pares de 0 a 10:")
for i in range(0, 11, 2):
    print(f"   - {i}")

# Exemplo 4: Usando `range` para contagem regressiva
print("\n4. Contagem regressiva de 5 a 1:")
for i in range(5, 0, -1):
    print(f"   - {i}...")
print("   Lançar!")

# Exemplo 5: Usando `range` para acessar elementos de uma lista pelo índice
animais = ["gato", "cão", "pássaro"]
print("\n5. Acessando lista por índice com `range`:")
for i in range(len(animais)):
    print(f"   - No índice {i} está o animal: {animais[i]}")

# Exemplo 6: Usando `_` como variável quando o valor não é necessário
print("\n6. Repetindo uma ação 3 vezes sem usar a variável de loop:")
for _ in range(3):
    print("   - Ação repetida")
print("-" * 20 + "\n")


# 3. O Loop `while`: Repetindo com Base em uma Condição
# -----------------------------------------------------
# O loop `while` executa um bloco de código enquanto uma condição for verdadeira.

print("--- 3. O Loop `while` (6 Exemplos) ---")

# Exemplo 1: Contador simples de 1 a 5
contador = 1
print("1. Contando de 1 a 5 com `while`:")
while contador <= 5:
    print(f"   - {contador}")
    contador += 1

# Exemplo 2: Loop que depende de uma entrada do usuário
print("\n2. Digite 'sair' para terminar.")
entrada = ""
while entrada.lower() != "sair":
    entrada = input("   > ")
    print(f"   Você digitou: {entrada}")

# Exemplo 3: Consumindo uma lista até que ela esteja vazia
tarefas = ["Lavar pratos", "Limpar o quarto"]
print("\n3. Realizando tarefas da lista:")
while tarefas:  # A lista vazia é avaliada como False
    tarefa_atual = tarefas.pop(0)
    print(f"   - Realizando: {tarefa_atual}")
print("   Todas as tarefas foram concluídas!")

# Exemplo 4: Encontrando a primeira potência de 2 maior que 100
potencia = 1
while potencia <= 100:
    potencia *= 2
print(f"\n4. A primeira potência de 2 > 100 é: {potencia}")

# Exemplo 5: Usando uma flag (bandeira) booleana para controlar o loop
jogo_ativo = True
vidas = 3
print("\n5. Simulação de um jogo simples:")
while jogo_ativo:
    print(f"   - Você tem {vidas} vidas.")
    vidas -= 1
    if vidas == 0:
        print("   - Game Over!")
        jogo_ativo = False

# Exemplo 6: Loop infinito com condição de parada interna (veremos `break` a seguir)
# while True:
#     print("Este loop nunca terminaria sem um `break`.")
print("\n6. `while True` é usado para loops infinitos controlados por `break`.")
print("-" * 20 + "\n")


# 4. A Declaração `break`: Saindo de um Loop
# -------------------------------------------
# `break` termina o loop imediatamente, independentemente da condição do loop.

print("--- 4. A Declaração `break` (6 Exemplos) ---")

# Exemplo 1: Parando um `for` quando um item é encontrado
print("1. Procurando pelo número 5 na lista:")
for num in [1, 2, 3, 4, 5, 6, 7]:
    if num == 5:
        print("   - Encontrei o 5! Saindo do loop.")
        break
    print(f"   - Verificando {num}...")

# Exemplo 2: Usando `break` em um loop `while True`
print("\n2. Loop `while True` com `break`:")
while True:
    resposta = input("   - Você quer sair? (s/n): ")
    if resposta.lower() == 's':
        break
print("   - Loop encerrado.")

# Exemplo 3: Parando a busca em uma lista de dicionários
usuarios = [{"nome": "Ana", "id": 1}, {"nome": "Beto", "id": 2}, {"nome": "Caio", "id": 3}]
print("\n3. Buscando usuário com id 2:")
for usuario in usuarios:
    if usuario["id"] == 2:
        print(f"   - Usuário encontrado: {usuario['nome']}")
        break

# Exemplo 4: Validando entrada do usuário
print("\n4. Peça um número positivo:")
while True:
    num_str = input("   - Digite um número: ")
    if num_str.isdigit():
        print("   - Obrigado!")
        break
    else:
        print("   - Entrada inválida. Tente novamente.")

# Exemplo 5: Jogo de adivinhação simples
numero_secreto = 7
print("\n5. Adivinhe o número secreto entre 1 e 10:")
while True:
    palpite = int(input("   - Seu palpite: "))
    if palpite == numero_secreto:
        print("   - Você acertou!")
        break

# Exemplo 6: Saindo de um loop `for` sobre uma string
print("\n6. Procurando por um espaço em uma frase:")
for char in "frase de exemplo":
    if char == ' ':
        print("   - Espaço encontrado. Parando.")
        break
    print(f"   - Caractere: {char}")
print("-" * 20 + "\n")


# 5. A Declaração `continue`: Pulando uma Iteração
# -------------------------------------------------
# `continue` pula o resto do código dentro do loop para a iteração atual
# e passa para a próxima iteração.

print("--- 5. A Declaração `continue` (6 Exemplos) ---")

# Exemplo 1: Pulando números negativos ao somar
soma_positivos = 0
print("1. Somando apenas números positivos em [-1, 10, -5, 3]:")
for num in [-1, 10, -5, 3]:
    if num < 0:
        continue
    soma_positivos += num
print(f"   - Soma: {soma_positivos}")

# Exemplo 2: Imprimindo apenas números ímpares
print("\n2. Imprimindo ímpares de 0 a 9:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"   - {i}")

# Exemplo 3: Ignorando um item específico em uma lista
print("\n3. Processando todos os nomes, exceto 'Beto':")
for nome in ["Ana", "Beto", "Caio"]:
    if nome == "Beto":
        continue
    print(f"   - Olá, {nome}!")

# Exemplo 4: Pulando linhas de comentário
linhas_codigo = ["x = 1", "# Isso é um comentário", "print(x)"]
print("\n4. Ignorando comentários:")
for linha in linhas_codigo:
    if linha.strip().startswith("#"):
        continue
    print(f"   - Executando: {linha}")

# Exemplo 5: Em um loop `while`, `continue` também pula para a próxima verificação
i = 0
print("\n5. `continue` em um loop `while`:")
while i < 5:
    i += 1
    if i == 3:
        print("   - Pulando o 3")
        continue
    print(f"   - i = {i}")

# Exemplo 6: Coletando apenas vogais de uma string
vogais = ""
for letra in "programacao":
    if letra not in "aeiou":
        continue
    vogais += letra
print(f"\n6. Vogais encontradas em 'programacao': {vogais}")
print("-" * 20 + "\n")


# ====================================================================================
# Parte 2: Tópicos Intermediários e Avançados
# ====================================================================================

# 6. A Cláusula `else` em Loops
# -----------------------------
# O bloco `else` de um loop é executado somente se o loop terminar
# naturalmente (sem ser interrompido por um `break`).

print("--- 6. A Cláusula `else` em Loops (6 Exemplos) ---")

# Exemplo 1: `for/else` - busca bem-sucedida (com `break`)
print("1. Procurando por 3 em [1, 2, 3, 4]:")
for num in [1, 2, 3, 4]:
    if num == 3:
        print("   - Número 3 encontrado!")
        break
else:
    print("   - O loop terminou e o número não foi encontrado.") # Não será executado

# Exemplo 2: `for/else` - busca mal-sucedida (sem `break`)
print("\n2. Procurando por 5 em [1, 2, 3, 4]:")
for num in [1, 2, 3, 4]:
    if num == 5:
        print("   - Número 5 encontrado!")
        break
else:
    print("   - O loop terminou e o número 5 não foi encontrado.") # Será executado

# Exemplo 3: `while/else` - loop termina normalmente
contador = 0
print("\n3. Loop `while` que completa:")
while contador < 3:
    print(f"   - Contagem: {contador}")
    contador += 1
else:
    print("   - O loop `while` terminou sem `break`.")

# Exemplo 4: `while/else` - loop é interrompido por `break`
contador = 0
print("\n4. Loop `while` que é interrompido:")
while contador < 5:
    if contador == 3:
        print("   - Interrompendo no 3.")
        break
    contador += 1
else:
    print("   - O `else` não será executado.")

# Exemplo 5: Validando se todos os números são positivos
numeros = [10, 20, 30, 5]
print("\n5. Verificando se todos os números são positivos:")
for num in numeros:
    if num < 0:
        print("   - Encontrado um número negativo. Validação falhou.")
        break
else:
    print("   - Todos os números são positivos. Validação bem-sucedida.")

# Exemplo 6: Verificando se um número é primo
num_para_verificar = 7
print(f"\n6. Verificando se {num_para_verificar} é primo:")
for i in range(2, num_para_verificar):
    if num_para_verificar % i == 0:
        print(f"   - Não é primo, divisível por {i}.")
        break
else:
    print(f"   - É primo!")
print("-" * 20 + "\n")


# 7. Loops Aninhados (Nested Loops)
# ----------------------------------
# Um loop dentro de outro. O loop interno é executado completamente
# para cada iteração do loop externo.

print("--- 7. Loops Aninhados (6 Exemplos) ---")

# Exemplo 1: Imprimindo uma matriz (lista de listas)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("1. Imprimindo uma matriz 3x3:")
for linha in matriz:
    for elemento in linha:
        print(f"   {elemento}", end=" ")
    print() # Pula para a próxima linha

# Exemplo 2: Criando uma tabuada
print("\n2. Tabuada do 1 ao 3:")
for i in range(1, 4):
    for j in range(1, 11):
        print(f"   {i} x {j} = {i*j}")
    print("   " + "-"*10)

# Exemplo 3: Encontrando pares de números que somam 10
lista_nums = [2, 4, 6, 8, 5]
print("\n3. Pares que somam 10:")
for i in lista_nums:
    for j in lista_nums:
        if i + j == 10:
            print(f"   - ({i}, {j})")

# Exemplo 4: Criando uma lista de coordenadas
coordenadas = []
for x in range(3):
    for y in range(2):
        coordenadas.append((x, y))
print(f"\n4. Lista de coordenadas (x,y): {coordenadas}")

# Exemplo 5: `break` em um loop aninhado (só sai do loop interno)
print("\n5. `break` em loop aninhado:")
for i in range(3):
    print(f" - Loop externo i={i}")
    for j in range(5):
        if j == 2:
            print("   - Saindo do loop interno (j)")
            break
        print(f"   - Loop interno j={j}")

# Exemplo 6: Processando estrutura de dados aninhada
dados_vendas = {"2022": [100, 120], "2023": [150, 130, 180]}
print("\n6. Processando vendas aninhadas:")
for ano, vendas in dados_vendas.items():
    total_ano = 0
    for venda in vendas:
        total_ano += venda
    print(f"   - Total de vendas em {ano}: {total_ano}")
print("-" * 20 + "\n")


# 8. Iterando sobre Dicionários
# -------------------------------
# Você pode iterar sobre as chaves, valores ou ambos (pares chave-valor).

print("--- 8. Iterando sobre Dicionários (6 Exemplos) ---")

contatos = {"Ana": "ana@email.com", "Beto": "beto@email.com", "Caio": "caio@email.com"}

# Exemplo 1: Iterando sobre as chaves (comportamento padrão)
print("1. Iterando sobre as chaves:")
for nome in contatos:
    print(f"   - Chave: {nome}")

# Exemplo 2: Iterando sobre as chaves explicitamente com `.keys()`
print("\n2. Iterando com `.keys()`:")
for nome in contatos.keys():
    print(f"   - Chave: {nome}")

# Exemplo 3: Iterando sobre os valores com `.values()`
print("\n3. Iterando sobre os valores com `.values()`:")
for email in contatos.values():
    print(f"   - Valor: {email}")

# Exemplo 4: Iterando sobre os pares chave-valor com `.items()`
print("\n4. Iterando sobre os itens com `.items()`:")
for nome, email in contatos.items():
    print(f"   - {nome} -> {email}")

# Exemplo 5: Acessando o valor a partir da chave durante a iteração
print("\n5. Acessando valor a partir da chave:")
for nome in contatos:
    print(f"   - O email de {nome} é {contatos[nome]}")

# Exemplo 6: Criando um novo dicionário a partir de outro
precos = {"maçã": 2.50, "banana": 1.80}
precos_com_imposto = {}
for fruta, preco in precos.items():
    precos_com_imposto[fruta] = preco * 1.10
print(f"\n6. Dicionário de preços com imposto: {precos_com_imposto}")
print("-" * 20 + "\n")


# 9. A Função `enumerate()`: Obtendo Índice e Valor
# --------------------------------------------------
# `enumerate()` adiciona um contador a um iterável e o retorna em forma de
# um objeto enumerado. Útil para obter o índice e o valor ao mesmo tempo.

print("--- 9. A Função `enumerate()` (6 Exemplos) ---")

# Exemplo 1: Uso básico com uma lista
print("1. Enumerando uma lista de cores:")
for indice, cor in enumerate(["vermelho", "verde", "azul"]):
    print(f"   - Índice {indice}: {cor}")

# Exemplo 2: `enumerate` com um `start` diferente de 0
print("\n2. Enumerando a partir do índice 1:")
for i, nome in enumerate(["Ana", "Beto", "Caio"], start=1):
    print(f"   - Posição {i}: {nome}")

# Exemplo 3: Usando `enumerate` para criar um dicionário
letras = ['a', 'b', 'c']
mapa_indices = {}
for indice, letra in enumerate(letras):
    mapa_indices[letra] = indice
print(f"\n3. Dicionário de letra para índice: {mapa_indices}")

# Exemplo 4: Encontrando o índice de um item específico
print("\n4. Encontrando o índice de 'banana':")
for i, fruta in enumerate(frutas):
    if fruta == "banana":
        print(f"   - 'banana' está no índice {i}.")
        break

# Exemplo 5: Processando apenas itens em índices pares
print("\n5. Itens em índices pares:")
for i, valor in enumerate([10, 20, 30, 40, 50]):
    if i % 2 == 0:
        print(f"   - Índice {i}: {valor}")

# Exemplo 6: `enumerate` em uma string
print("\n6. Enumerando uma string:")
for i, char in enumerate("loop"):
    print(f"   - Índice {i}: '{char}'")
print("-" * 20 + "\n")


# 10. A Função `zip()`: Iterando sobre Múltiplas Sequências
# ---------------------------------------------------------
# `zip()` cria um iterador que agrega elementos de dois ou mais iteráveis.
# O loop para quando a menor das sequências chega ao fim.

print("--- 10. A Função `zip()` (6 Exemplos) ---")

# Exemplo 1: Combinando duas listas
nomes = ["Ana", "Beto", "Caio"]
idades = [28, 34, 29]
print("1. Combinando nomes e idades:")
for nome, idade in zip(nomes, idades):
    print(f"   - {nome} tem {idade} anos.")

# Exemplo 2: `zip` para quando as listas têm tamanhos diferentes
produtos = ["Produto A", "Produto B"]
estoques = [100, 50, 200] # `zip` vai parar no segundo item
print("\n2. `zip` com listas de tamanhos diferentes:")
for produto, estoque in zip(produtos, estoques):
    print(f"   - {produto}: {estoque} em estoque")

# Exemplo 3: Combinando três sequências
letras = ('a', 'b', 'c')
numeros = [1, 2, 3]
simbolos = "!@#"
print("\n3. Combinando três sequências:")
for letra, num, simb in zip(letras, numeros, simbolos):
    print(f"   - {letra}, {num}, {simb}")

# Exemplo 4: Usando `zip` para criar um dicionário
chaves = ["nome", "idade"]
valores = ["Carlos", 40]
dicionario_usuario = dict(zip(chaves, valores))
print(f"\n4. Dicionário criado com `zip`: {dicionario_usuario}")

# Exemplo 5: Desempacotando com `zip` e `*`
pares = [('a', 1), ('b', 2), ('c', 3)]
letras_unzipped, numeros_unzipped = zip(*pares)
print(f"\n5. Desempacotando com `zip`: {letras_unzipped} e {numeros_unzipped}")

# Exemplo 6: Iterando sobre um dicionário e uma lista
precos = {"maçã": 2.5, "banana": 1.8}
quantidades = [10, 5]
print("\n6. Calculando custo total:")
for (fruta, preco), quantidade in zip(precos.items(), quantidades):
    print(f"   - Custo de {fruta}: R${preco * quantidade:.2f}")
print("-" * 20 + "\n")