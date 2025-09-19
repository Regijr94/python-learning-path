# -*- coding: utf-8 -*-

"""
Guia Completo de Dicionários em Python: Do Básico ao Avançado

Este arquivo é um guia de estudo completo sobre dicionários em Python,
estruturado como uma aula progressiva.
--------------------------------------------------------------------------------------
Conteúdo:
1.  O que são Dicionários?
2.  Criando Dicionários
3.  Acessando e Modificando Dados
4.  Removendo Elementos
5.  Iteração e Views (keys, values, items)
6.  Métodos Úteis e Comuns
7.  Dictionary Comprehensions (Compreensão de Dicionários)
8.  Empacotamento e Desempacotamento (Packing & Unpacking)
9.  Tópicos Avançados
--------------------------------------------------------------------------------------
"""

# 1. O que são Dicionários?
# --------------------------
# Um dicionário é uma coleção mutável que armazena pares de chave-valor.
# A partir do Python 3.7, a ordem de inserção dos itens é preservada.
#
# - Mutável: Seu conteúdo pode ser alterado após a criação.
# - Chaves Únicas: As chaves devem ser únicas dentro de um dicionário.
# - Chaves Imutáveis: As chaves devem ser de um tipo de dado imutável (como strings, números ou tuplas).
# - Indexado por Chaves: Em vez de índices numéricos como as listas, usamos chaves para acessar valores.

print("--- 1. O que são Dicionários? ---")
# Exemplo 1: Representando um objeto do mundo real (um carro)
usuario = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2023,
    "motor": 2.0
}
print(f"1. Objeto Carro: {usuario}")

# Exemplo 2: Configurações de um aplicativo
configuracoes_app = {
    "idioma": "pt-br",
    "tema": "escuro",
    "notificacoes_ativas": True,
    "volume": 80
}
print(f"2. Configurações: {configuracoes_app}")

# Exemplo 3: Dados de uma API (simulação de JSON)
dados_api_clima = {
    "cidade": "Rio de Janeiro",
    "temperatura": 28,
    "unidade": "celsius",
    "condicao": "ensolarado"
}
print(f"3. Dados de API: {dados_api_clima}")

# Exemplo 4: Usando tuplas como chaves para coordenadas
mapa_tesouro = {
    (10, 20): "Baú de Ouro",
    (35, -15): "Armadilha",
    (0, 0): "Início"
}
print(f"4. Mapa com chaves-tupla: {mapa_tesouro}")

# Exemplo 5: Contagem de frequência de itens
contagem_letras = {'a': 5, 'b': 3, 'c': 8}
print(f"5. Contagem de Frequência: {contagem_letras}\n")


# 2. Criando Dicionários
# ----------------------
# Dicionários podem ser criados de várias formas, principalmente com `{}` ou `dict()`.

print("--- 2. Criando Dicionários (5 Exemplos) ---")
# Exemplo 1: Dicionário vazio e adição posterior
d1 = {}
d1['nome'] = "Ana"
d1['idade'] = 25
print(f"1. Dicionário vazio preenchido: {d1}")

# Exemplo 2: Usando a sintaxe literal com chaves `{}`
d2 = {"curso": "Python", "nivel": "Avançado", "duracao_horas": 40}
print(f"2. Dicionário com sintaxe literal: {d2}")

# Exemplo 3: Usando o construtor `dict()` com argumentos nomeados
produto = dict(nome="Laptop", preco=4500.00, em_estoque=True)
print(f"3. Dicionário com construtor dict(): {produto}")

# Exemplo 4: Usando `dict()` com uma lista de tuplas (chave, valor)
d4 = dict([('id', 101), ('departamento', 'Vendas'), ('salario', 5000)])
print(f"4. Dicionário de lista de tuplas: {d4}")

# Exemplo 5: Usando `dict()` e `zip()` para combinar duas listas
chaves = ["a", "b", "c"]
valores = [1, 2, 3]
d5 = dict(zip(chaves, valores))
print(f"5. Dicionário criado com zip(): {d5}\n")


# 3. Acessando e Modificando Dados
# --------------------
# Acessar e modificar dados é uma operação central em dicionários.

print("--- 3. Acessando e Modificando Dados (5 Exemplos) ---")
filme = {
    "titulo": "Inception",
    "ano": 2010,
    "diretor": "Christopher Nolan"
}

# Exemplo 1: Acessando um valor com colchetes `[]`
print(f"1. Acessando 'titulo': {filme['titulo']}")

# Exemplo 2: Modificando um valor existente e adicionando um novo
filme['ano'] = 2011  # Modifica
filme['genero'] = "Ficção Científica"  # Adiciona
print(f"2. Dicionário modificado: {filme}")

# Exemplo 3: Usando `.get()` para acesso seguro (evita KeyError)
ator_principal = filme.get("ator_principal")
print(f"3. Usando .get() para chave inexistente: {ator_principal}")

# Exemplo 4: Usando `.get()` com um valor padrão
bilheteria = filme.get("bilheteria", "Não informada")
print(f"4. Usando .get() com valor padrão: {bilheteria}")

# Exemplo 5: Usando `.setdefault()` para adicionar se não existir
# Se a chave 'bilheteria' não existir, adiciona com o valor padrão e retorna o valor.
bilheteria_definida = filme.setdefault("bilheteria", 0)
print(f"5. Dicionário após .setdefault(): {filme}")
print(f"   Valor retornado por .setdefault(): {bilheteria_definida}\n")


# 4. Removendo Elementos
# ----------------------
print("--- 4. Removendo Elementos (5 Exemplos) ---")
estoque = {"lapis": 100, "caneta": 75, "borracha": 200, "apontador": 50}
print(f"Estoque original: {estoque}")

# Exemplo 1: Usando `del` para remover um item específico
del estoque["apontador"]
print(f"1. Após `del estoque['apontador']`: {estoque}")

# Exemplo 2: Usando `.pop()` para remover e obter o valor
valor_removido = estoque.pop("borracha")
print(f"2. Após `.pop('borracha')`: {estoque}, valor removido: {valor_removido}")

# Exemplo 3: Usando `.pop()` com valor padrão para evitar KeyError
item_inexistente = estoque.pop("régua", 0)
print(f"3. Usando .pop() em chave inexistente com padrão: {item_inexistente}")

# Exemplo 4: Usando `.popitem()` para remover o último item inserido (LIFO)
estoque['caderno'] = 30  # Adicionando um novo item
ultimo_item = estoque.popitem()
print(f"4. Após .popitem(): {estoque}, item removido: {ultimo_item}")

# Exemplo 5: Usando `.clear()` para remover todos os itens
estoque.clear()
print(f"5. Após .clear(): {estoque}\n")


# 5. Iteração e Views (keys, values, items)
# -----------------------------------------
# Dicionários oferecem "views" dinâmicas para suas chaves, valores e pares.

print("--- 5. Iteração e Views (5 Exemplos) ---")
contatos = {"Ana": "ana@email.com", "Beto": "beto@email.com", "Carlos": "carlos@email.com"}

# Exemplo 1: Iterando sobre as chaves (comportamento padrão do `for`)
print("1. Iterando sobre as chaves:")
for nome in contatos: # ou `for nome in contatos.keys():`
    print(f"   - {nome}")

# Exemplo 2: Iterando sobre os valores com `.values()`
print("2. Iterando sobre os valores:")
for email in contatos.values():
    print(f"   - {email}")

# Exemplo 3: Iterando sobre os pares (chave, valor) com `.items()`
print("3. Iterando sobre os itens (chave, valor):")
for nome, email in contatos.items():
    print(f"   - {nome}: {email}")

# Exemplo 4: Verificando a existência de uma chave com `in`
if "Ana" in contatos:
    print("4. 'Ana' está na lista de contatos.")

# Exemplo 5: Usando uma view para criar uma lista de chaves
lista_chaves = list(contatos.keys())
print(f"5. Lista criada a partir da view .keys(): {lista_chaves}\n")


# 6. Métodos Úteis e Comuns
# -------------------------
print("--- 6. Métodos Úteis e Comuns (5 Exemplos) ---")
perfil = {"nome": "Diana", "idade": 28}

# Exemplo 1: `.update()` para mesclar dicionários
info_adicional = {"idade": 29, "profissao": "Engenheira"}
perfil.update(info_adicional)
print(f"1. Após .update(): {perfil}")

# Exemplo 2: `.copy()` para criar uma cópia rasa (shallow copy)
perfil_copia = perfil.copy()
perfil_copia["cidade"] = "São Paulo"
print(f"2. Cópia modificada: {perfil_copia}, Original: {perfil}")

# Exemplo 3: `len()` para obter o número de pares chave-valor
print(f"3. O dicionário 'perfil' tem {len(perfil)} itens.")

# Exemplo 4: `fromkeys()` para criar um dicionário com chaves de um iterável e um valor padrão
novos_campos = ["status", "ultimo_login"]
perfil_base = dict.fromkeys(novos_campos, "Não definido")
print(f"4. Dicionário criado com .fromkeys(): {perfil_base}")

# Exemplo 5: Mesclando com o operador `|` (Python 3.9+)
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d3 = d1 | d2
print(f"5. Mesclado com operador pipe '|': {d3}\n")


# 7. Dictionary Comprehensions
# ----------------------------
# Uma maneira concisa e poderosa de criar dicionários a partir de iteráveis.

print("--- 7. Dictionary Comprehensions (5 Exemplos) ---")
# Exemplo 1: Números e seus quadrados
quadrados = {x: x**2 for x in range(1, 6)}
print(f"1. Dicionário de quadrados: {quadrados}")

# Exemplo 2: A partir de uma lista, com condição
frutas = ["maçã", "banana", "cereja", "abacaxi"]
comprimento_frutas = {fruta: len(fruta) for fruta in frutas if len(fruta) > 5}
print(f"2. Frutas com nome > 5 letras: {comprimento_frutas}")

# Exemplo 3: Invertendo chaves e valores
original = {'a': 1, 'b': 2, 'c': 3}
invertido = {valor: chave for chave, valor in original.items()}
print(f"3. Dicionário invertido: {invertido}")

# Exemplo 4: Criando um dicionário com valores condicionais (if/else)
numeros = range(1, 6)
par_impar = {n: 'par' if n % 2 == 0 else 'ímpar' for n in numeros}
print(f"4. Classificação par/ímpar: {par_impar}")

# Exemplo 5: Processando valores de outro dicionário
precos_dolar = {'produtoA': 10, 'produtoB': 20, 'produtoC': 5}
cotacao_real = 5.0
precos_real = {produto: preco * cotacao_real for produto, preco in precos_dolar.items()}
print(f"5. Preços convertidos para Real: {precos_real}\n")


# 8. Empacotamento e Desempacotamento (Packing & Unpacking)
# ---------------------------------------------------------
# O operador `**` é extremamente poderoso para manipular dicionários.

print("--- 8. Empacotamento e Desempacotamento (5 Exemplos) ---")

# Exemplo 1: Desempacotamento (`**`) para mesclar dicionários
# Semelhante ao operador `|`, mas compatível com Python 3.5+.
# Chaves do dicionário mais à direita têm precedência.
d1 = {'a': 1, 'b': 20}
d2 = {'b': 3, 'c': 4}
d_mesclado = {**d1, **d2, 'd': 5}
print(f"1. Mesclando dicionários com `**`: {d_mesclado}")

# Exemplo 2: Desempacotamento (`**`) em chamadas de função
# Passa os pares chave-valor de um dicionário como argumentos nomeados.
def criar_relatorio(titulo, autor, ano):
    return f"Relatório '{titulo}' por {autor}, em {ano}."

dados_relatorio = {"titulo": "Vendas Anuais", "autor": "Equipe de Vendas", "ano": 2023}
relatorio_final = criar_relatorio(**dados_relatorio)
print(f"2. Desempacotamento em chamada de função: {relatorio_final}")

# Exemplo 3: Empacotamento (`**kwargs`) em definições de função
# Coleta todos os argumentos de palavra-chave extras em um dicionário.
def processar_dados(**kwargs):
    print(f"3. Dados recebidos via **kwargs: {kwargs}")
    id_usuario = kwargs.get('id')
    if id_usuario:
        print(f"   Processando usuário com ID: {id_usuario}")

processar_dados(id=101, nome="Carlos", status="ativo")

# Exemplo 4: Desempacotamento de chaves com `*` (Python 3.5+)
# O operador `*` em um dicionário desempacota apenas as chaves.
chaves_dict = {*'abcde', *'123'} # Cria um set de caracteres únicos
print(f"4. Desempacotando chaves com `*` em um set: {chaves_dict}")

# Exemplo 5: Combinando desempacotamento e argumentos posicionais
def configuracao_completa(host, port, **opcoes_avancadas):
    print(f"5. Conectando a {host}:{port}")
    if opcoes_avancadas.get('timeout'):
        print(f"   Timeout definido para: {opcoes_avancadas['timeout']}s")
    if opcoes_avancadas.get('retry'):
        print(f"   Tentativas: {opcoes_avancadas['retry']}")

config_db = {'host': 'localhost', 'port': 5432, 'timeout': 30, 'retry': 3}
configuracao_completa(**config_db)
print("")

# 8. Tópicos Avançados
# -------------------
# Esta seção explora estruturas de dados especializadas do módulo `collections`
# e padrões de uso avançado com dicionários.
print("--- 8. Tópicos Avançados (5 Exemplos) ---")

# Exemplo 1: Dicionários Aninhados (Nested Dictionaries)
# Dicionários podem conter outros dicionários, permitindo criar estruturas de dados complexas.
usuarios_db = {
    "user1": {"nome": "Gabriel", "email": "gabriel@email.com"},
    "user2": {"nome": "Helena", "email": "helena@email.com"}
}
# Modificando um valor aninhado
usuarios_db['user1']['email'] = 'gabriel.novo@email.com'
print(f"1. Acessando e modificando valor aninhado: {usuarios_db['user1']}")

# Exemplo 2: `collections.defaultdict` para agrupar dados
# `defaultdict` é como um dicionário normal, mas fornece um valor padrão para
# chaves que ainda não existem, evitando um `KeyError`.
from collections import defaultdict
cidades_por_estado = [('SP', 'São Paulo'), ('RJ', 'Rio de Janeiro'), ('SP', 'Campinas')]
d_list = defaultdict(list)  # A fábrica `list` cria uma lista vazia para novas chaves
for estado, cidade in cidades_por_estado:
    d_list[estado].append(cidade)
print(f"2. defaultdict(list) para agrupar: {dict(d_list)}")

# Exemplo 3: `collections.Counter` para contagem de frequência
# `Counter` é uma subclasse de `dict` especializada em contar objetos "hasheáveis".
from collections import Counter
cores_votos = ['azul', 'vermelho', 'azul', 'verde', 'azul', 'vermelho']
contagem_votos = Counter(cores_votos)
print(f"3. Counter para contagem de votos: {contagem_votos}")
print(f"   - Votos para 'azul': {contagem_votos['azul']}")
print(f"   - Cor mais votada: {contagem_votos.most_common(1)}")

# Exemplo 4: `collections.OrderedDict` (legado, pois dicts normais já são ordenados)
# Ainda é útil por métodos como `move_to_end()` e `popitem(last=False)`.
from collections import OrderedDict
cache_fifo = OrderedDict()
cache_fifo['chave1'] = 'valor1'
cache_fifo['chave2'] = 'valor2'
cache_fifo['chave3'] = 'valor3'
# Simulando uma fila (FIFO - First-In, First-Out)
primeiro_item_removido = cache_fifo.popitem(last=False)
print(f"4. OrderedDict como cache FIFO: {cache_fifo}")
print(f"   - Item removido (o mais antigo): {primeiro_item_removido}")

# Exemplo Bônus: `collections.ChainMap` para combinar dicionários
# `ChainMap` agrupa múltiplos dicionários em uma única visão atualizável.
# A busca por chaves é feita em cada dicionário sequencialmente.
from collections import ChainMap
config_padrao = {'tema': 'claro', 'fonte': 'Arial', 'idioma': 'en'}
config_usuario = {'tema': 'escuro', 'fonte_tamanho': 12}

configs_combinadas = ChainMap(config_usuario, config_padrao)

print("\n--- Tópico Avançado Bônus: ChainMap ---")
print(f"Visão combinada: {configs_combinadas}")
print(f"Tema (vem de config_usuario): {configs_combinadas['tema']}")
print(f"Idioma (vem de config_padrao): {configs_combinadas['idioma']}")

# Modificações em ChainMap afetam apenas o primeiro dicionário da cadeia
configs_combinadas['idioma'] = 'pt-br'
print(f"config_usuario após modificação: {config_usuario}")
print(f"config_padrao (não foi alterado): {config_padrao}\n")

# Exemplo 5 foi movido para a seção de Empacotamento/Desempacotamento.
# Adicionando um novo exemplo avançado:
# Exemplo 5: Visões de Dicionário (Dictionary Views)
# As views (de .keys(), .values(), .items()) são dinâmicas e refletem alterações no dicionário.
numeros = {'a': 1, 'b': 2}
items_view = numeros.items()
print(f"5. View inicial: {items_view}")
numeros['c'] = 3
print(f"   View após adição no dicionário: {items_view}\n")
