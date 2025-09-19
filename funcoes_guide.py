# -*- coding: utf-8 -*-

"""
Guia Definitivo de Funções em Python: Do Básico ao Avançado

Este arquivo é um guia de estudo completo sobre funções em Python,
estruturado como uma aula progressiva com múltiplos exemplos para cada conceito.

--------------------------------------------------------------------------------------
Conteúdo:

-- Parte 1: Fundamentos (Básico ao Intermediário) --
1. Definição e Chamada de Funções
2. A Palavra-chave `return`
3. Argumentos Posicionais e Nomeados (Keyword Arguments)
4. Parâmetros com Valores Padrão (Default Arguments)
5. Docstrings e Anotações de Tipo (Type Hinting)

-- Parte 2: Tópicos Avançados --
6. Escopo de Variáveis (Regra LEGB)
7. Argumentos Arbitrários e Forçados (`*args`, `**kwargs`, `/`, `*`)
8. Funções de Ordem Superior e o Módulo `functools`
9. Funções Geradoras e Expressões (`yield`)
10. Closures e Decorators
--------------------------------------------------------------------------------------
"""

from typing import List, Dict, Any, Callable, Tuple, Union
from functools import partial, reduce, wraps
import time

# ====================================================================================
# Parte 1: Fundamentos
# ====================================================================================

# 1. Definição e Chamada de Funções
# ----------------------------------
# Funções são blocos de código nomeados e reutilizáveis. São definidas com `def`.

print("--- 1. Definição e Chamada de Funções (10 Exemplos) ---")

# 1. Função mais simples: sem parâmetros
def saudacao():
    """Imprime uma saudação simples."""
    print("1. Olá, Python!")
saudacao()

# 2. Função com um parâmetro
def saudacao_personalizada(nome):
    """Imprime uma saudação para um nome específico."""
    print(f"2. Olá, {nome}!")
saudacao_personalizada("Ana")

# 3. Função com múltiplos parâmetros
def exibir_info(nome, idade, cidade):
    """Exibe informações formatadas."""
    print(f"3. {nome} tem {idade} anos e mora em {cidade}.")
exibir_info("Beto", 35, "Recife")

# 4. Função que realiza um cálculo
def calcular_media(n1, n2, n3):
    """Calcula e imprime a média de três números."""
    media = (n1 + n2 + n3) / 3
    print(f"4. A média é: {media}")
calcular_media(10, 8, 9)

# 5. Função que chama outra função
def preparar_relatorio():
    """Função principal que usa uma função auxiliar."""
    print("5. Preparando relatório...")
    saudacao_personalizada("Equipe")
    print("   Relatório concluído.")
preparar_relatorio()

# 6. Função para exibir uma linha de separação
def linha(tamanho=40):
    """Imprime uma linha de traços."""
    print('6. ' + '-' * tamanho)
linha()

# 7. Função para verificar se um número é par
def eh_par(numero):
    """Verifica se um número é par."""
    if numero % 2 == 0:
        print(f"7. O número {numero} é par.")
    else:
        print(f"7. O número {numero} é ímpar.")
eh_par(10)

# 8. Função com múltiplos parâmetros de tipos diferentes
def registrar_produto(id_produto, nome, preco, em_estoque):
    """Simula o registro de um produto."""
    print(f"8. Produto '{nome}' (ID: {id_produto}) registrado com preço R${preco:.2f}. Em estoque: {em_estoque}")
registrar_produto(101, "Mouse", 89.90, True)

# 9. Função que executa uma tarefa sem argumentos
def exibir_data_hora_atual():
    """Mostra a data e hora atuais."""
    from datetime import datetime
    print(f"9. Data e hora: {datetime.now()}")
exibir_data_hora_atual()

# 10. Chamando a mesma função com dados diferentes
print("10. Chamando a mesma função múltiplas vezes:")
saudacao_personalizada("Carlos")
saudacao_personalizada("Diana")
print("-" * 20 + "\n")


# 2. A Palavra-chave `return`
# ---------------------------
# `return` é usada para enviar um valor de volta de uma função.
# Uma função sem `return` explicitamente retorna `None`.

print("--- 2. A Palavra-chave `return` (10 Exemplos) ---")

# 1. Retornando um valor simples (número)
def somar(a, b):
    return a + b
resultado_soma = somar(10, 5)
print(f"1. Resultado da soma: {resultado_soma}")

# 2. Retornando uma string
def formatar_nome_completo(primeiro, ultimo):
    return f"{primeiro.title()} {ultimo.title()}"
nome_formatado = formatar_nome_completo("ana", "souza")
print(f"2. Nome formatado: {nome_formatado}")

# 3. Retornando um booleano
def eh_maior_de_idade(idade):
    return idade >= 18
status_idade = eh_maior_de_idade(20)
print(f"3. É maior de idade? {status_idade}")

# 4. Retornando uma lista
def gerar_numeros_pares(limite):
    pares = []
    for i in range(limite + 1):
        if i % 2 == 0:
            pares.append(i)
    return pares
lista_pares = gerar_numeros_pares(10)
print(f"4. Lista de pares: {lista_pares}")

# 5. Retornando um dicionário
def criar_dicionario_usuario(id_usuario, nome):
    return {"id": id_usuario, "nome": nome, "ativo": True}
usuario_dict = criar_dicionario_usuario(205, "Fábio")
print(f"5. Dicionário de usuário: {usuario_dict}")

# 6. Retornando múltiplos valores (como uma tupla)
def obter_min_max(lista):
    return min(lista), max(lista)
minimo, maximo = obter_min_max([1, 10, -5, 100, 42])
print(f"6. Mínimo: {minimo}, Máximo: {maximo}")

# 7. Função com `return` condicional
def encontrar_valor(lista, valor):
    for item in lista:
        if item == valor:
            return f"Valor {valor} encontrado!"
    return f"Valor {valor} não encontrado."
print(f"7. {encontrar_valor([1, 2, 3], 3)}")
print(f"   {encontrar_valor([1, 2, 3], 99)}")

# 8. Função sem `return` explícito (retorna `None`)
def apenas_imprime(texto):
    print(f"8. Imprimindo: {texto}")
retorno_implicito = apenas_imprime("Teste")
print(f"   Retorno implícito: {retorno_implicito}")

# 9. Usando `return` para sair da função antecipadamente
def processar_dados(lista_dados):
    if not lista_dados:
        return "Nenhum dado para processar." # Sai da função aqui
    # ... lógica de processamento
    return "Dados processados com sucesso."
print(f"9. {processar_dados([])}")

# 10. Retornando o resultado de uma expressão diretamente
def area_circulo(raio):
    return 3.14159 * (raio ** 2)
print(f"10. Área do círculo: {area_circulo(10):.2f}")
print("-" * 20 + "\n")


# 3. Argumentos Posicionais e Nomeados (Keyword Arguments)
# --------------------------------------------------------
# Argumentos são os valores passados para uma função.
# - Posicionais: dependem da ordem em que são passados.
# - Nomeados: são passados com `nome=valor`, e a ordem não importa.

print("--- 3. Argumentos Posicionais e Nomeados (10 Exemplos) ---")

def criar_relatorio(titulo, autor, versao):
    print(f"Relatório: '{titulo}' | Autor: {autor} | Versão: {versao}")

# 1. Usando apenas argumentos posicionais (a ordem importa)
print("1. Argumentos posicionais:")
criar_relatorio("Vendas 2023", "Equipe de Vendas", "1.0")

# 2. Usando apenas argumentos nomeados (a ordem não importa)
print("2. Argumentos nomeados:")
criar_relatorio(autor="Equipe de Marketing", versao="2.1", titulo="Análise de Mercado")

# 3. Misturando posicionais e nomeados (posicionais devem vir primeiro)
print("3. Misturando argumentos:")
criar_relatorio("Feedback de Clientes", autor="Suporte", versao="1.3")

# 4. Usando argumentos nomeados para clareza
def enviar_email(destinatario, remetente, assunto, corpo):
    print(f"4. Enviando email para {destinatario} sobre '{assunto}'")
enviar_email(
    destinatario="cliente@example.com",
    remetente="suporte@empresa.com",
    assunto="Sua fatura chegou",
    corpo="Prezado cliente..."
)

# 5. Passando variáveis como argumentos
print("5. Passando variáveis:")
titulo_rel = "Relatório de Bug"
autor_rel = "QA Team"
versao_rel = "0.9-beta"
criar_relatorio(titulo_rel, autor_rel, versao_rel)

# 6. Erro: argumento posicional após argumento nomeado
try:
    # criar_relatorio(titulo="Teste", "Autor Teste", "1.0") # Descomente para ver o erro
    print("6. (Comentado) `SyntaxError` ao usar posicional após nomeado.")
except SyntaxError as e:
    print(f"   Erro capturado: {e}")

# 7. Erro: faltando um argumento posicional
try:
    # criar_relatorio("Título Apenas") # Descomente para ver o erro
    print("7. (Comentado) `TypeError` ao faltar argumentos.")
except TypeError as e:
    print(f"   Erro capturado: {e}")

# 8. Erro: passando o mesmo argumento de duas formas
try:
    # criar_relatorio("Título", "Autor", titulo="Outro Título") # Descomente para ver o erro
    print("8. (Comentado) `TypeError` ao passar argumento duas vezes.")
except TypeError as e:
    print(f"   Erro capturado: {e}")

# 9. Função com muitos parâmetros onde nomeados são úteis
def configurar_plot(x, y, cor="blue", estilo_linha="-", largura=1):
    print(f"9. Plotando com cor {cor} e estilo '{estilo_linha}'")
configurar_plot([1,2], [3,4], estilo_linha="--") # Fácil de pular os do meio

# 10. Usando nomeados para inverter a ordem lógica da chamada
print("10. Invertendo a ordem com nomeados:")
criar_relatorio(versao="final", autor="Diretoria", titulo="Plano Estratégico")
print("-" * 20 + "\n")


# 4. Parâmetros com Valores Padrão (Default Arguments)
# ----------------------------------------------------
# Permitem que você defina um valor padrão para um parâmetro, tornando-o opcional.

print("--- 4. Parâmetros com Valores Padrão (10 Exemplos) ---")

# 1. Função com um parâmetro padrão
def conectar_banco(host="localhost", porta=5432):
    print(f"1. Conectando a {host}:{porta}")
conectar_banco()

# 2. Sobrescrevendo um valor padrão
print("2. Sobrescrevendo a porta:")
conectar_banco(porta=3306)

# 3. Sobrescrevendo todos os valores padrão
print("3. Sobrescrevendo host e porta:")
conectar_banco("db.example.com", 1433)

# 4. Misturando parâmetros obrigatórios e opcionais
def criar_usuario(nome, email, admin=False):
    print(f"4. Usuário '{nome}' criado. Admin: {admin}")
criar_usuario("Eva", "eva@example.com")
criar_usuario("Frank", "frank@example.com", admin=True)

# 5. Função de log com nível de severidade padrão
def log(mensagem, nivel="INFO"):
    print(f"5. [{nivel}] - {mensagem}")
log("Serviço iniciado.")
log("Falha na conexão!", nivel="ERROR")

# 6. Função para aplicar desconto com taxa padrão
def calcular_preco_final(preco, desconto=0.10):
    return preco * (1 - desconto)
print(f"6. Preço com desconto padrão: R${calcular_preco_final(100):.2f}")
print(f"   Preço com desconto de 50%: R${calcular_preco_final(100, 0.5):.2f}")

# 7. Parâmetros padrão devem vir após os não-padrão
# def funcao_errada(a=1, b): # SyntaxError: non-default argument follows default argument
print("7. (Comentado) Parâmetros padrão devem vir por último na definição.")

# 8. O perigo de usar objetos mutáveis (lista, dict) como padrão
def adiciona_a_lista_ruim(item, lista=[]): # NÃO FAÇA ISSO!
    lista.append(item)
    return lista
print(f"8. Chamada 1 (ruim): {adiciona_a_lista_ruim(1)}")
print(f"   Chamada 2 (ruim): {adiciona_a_lista_ruim(2)}") # A lista é compartilhada!

# 9. A forma correta de usar objetos mutáveis como padrão
def adiciona_a_lista_bom(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista
print(f"9. Chamada 1 (bom): {adiciona_a_lista_bom(1)}")
print(f"   Chamada 2 (bom): {adiciona_a_lista_bom(2)}")

# 10. Usando `None` como padrão para indicar "não fornecido"
def buscar_usuario(id_usuario=None, email=None):
    if id_usuario:
        print(f"10. Buscando por ID: {id_usuario}")
    elif email:
        print(f"10. Buscando por Email: {email}")
    else:
        print("10. Nenhum critério de busca fornecido.")
buscar_usuario(id_usuario=123)
buscar_usuario(email="user@example.com")
print("-" * 20 + "\n")


# 5. Docstrings e Anotações de Tipo (Type Hinting)
# ------------------------------------------------
# Docstrings (PEP 257) documentam o que sua função faz.
# Type Hints (PEP 484) anotam os tipos esperados de argumentos e do valor de retorno.

print("--- 5. Docstrings e Anotações de Tipo (10 Exemplos) ---")

# 1. Função com docstring simples
def dizer_ola(nome):
    """Imprime uma saudação para a pessoa."""
    print(f"Olá, {nome}!")
print(f"1. Docstring de `dizer_ola`: {dizer_ola.__doc__}")

# 2. Função com type hints básicos
def calcular_idade(ano_nascimento: int, ano_atual: int) -> int:
    """Calcula a idade com base nos anos fornecidos."""
    return ano_atual - ano_nascimento
print(f"2. Anotações de `calcular_idade`: {calcular_idade.__annotations__}")

# 3. Docstring no formato Google
def dividir(dividendo: float, divisor: float) -> float:
    """Divide um número pelo outro.

    Args:
        dividendo (float): O número a ser dividido.
        divisor (float): O número pelo qual dividir (não pode ser zero).

    Returns:
        float: O resultado da divisão.

    Raises:
        ValueError: Se o divisor for zero.
    """
    if divisor == 0:
        raise ValueError("O divisor não pode ser zero.")
    return dividendo / divisor
print("3. Função `dividir` com docstring completa e type hints.")

# 4. Type hints para tipos complexos (listas, dicionários)
def processar_nomes(nomes: List[str]) -> int:
    """Conta o número de nomes em uma lista."""
    print(f"4. Processando a lista: {nomes}")
    return len(nomes)
processar_nomes(["Ana", "Beto"])

# 5. Type hint para valor de retorno opcional (pode retornar `None`)
from typing import Optional
def encontrar_usuario(usuarios: Dict[int, str], id_usuario: int) -> Optional[str]:
    """Encontra um usuário pelo ID ou retorna None."""
    return usuarios.get(id_usuario)
print(f"5. Encontrando usuário 1: {encontrar_usuario({1: 'Ana'}, 1)}")

# 6. Type hint para múltiplos tipos possíveis (`Union`)
def formatar_id(id_valor: Union[int, str]) -> str:
    """Formata um ID que pode ser int ou str."""
    return f"ID-{str(id_valor).zfill(5)}"
print(f"6. Formatando ID (int): {formatar_id(123)}")
print(f"   Formatando ID (str): {formatar_id('abc')}")

# 7. Type hint para funções que não retornam nada (`None`)
def log_erro(mensagem: str) -> None:
    """Apenas registra uma mensagem de erro."""
    print(f"7. [ERRO] {mensagem}")
log_erro("Falha no sistema.")

# 8. Type hint para argumentos de função (`Callable`)
def executar_operacao(op: Callable[[int, int], int], a: int, b: int) -> None:
    """Executa uma operação (função) com dois números."""
    resultado = op(a, b)
    print(f"8. Resultado da operação: {resultado}")
executar_operacao(lambda x, y: x * y, 5, 4)

# 9. Type hint para `*args` e `**kwargs`
def log_eventos(*args: Any, **kwargs: Any) -> None:
    """Registra eventos com argumentos arbitrários."""
    print(f"9. Args: {args}, Kwargs: {kwargs}")
log_eventos(1, "evento", sucesso=True)

# 10. Acessando a docstring com `help()`
print("10. Use `help(dividir)` no console para ver a docstring formatada.")
print("-" * 20 + "\n")


# ====================================================================================
# Parte 2: Tópicos Avançados
# ====================================================================================

# 6. Escopo de Variáveis (Regra LEGB)
# ------------------------------------
# A Regra LEGB define a ordem de busca por variáveis:
# Local -> Enclosing (funções aninhadas) -> Global -> Built-in

print("--- 6. Escopo de Variáveis (10 Exemplos) ---")

variavel_global = "Sou Global" # Escopo Global

# 1. Escopo Local vs. Global
def escopo_local_teste():
    variavel_local = "Sou Local"
    print(f"1. Dentro da função: {variavel_local}, {variavel_global}")
escopo_local_teste()
# print(variavel_local) # NameError: `variavel_local` não existe aqui

# 2. Modificando uma variável global com a palavra-chave `global`
def modificar_global():
    global variavel_global
    variavel_global = "Fui modificada!"
print(f"2. Antes: {variavel_global}")
modificar_global()
print(f"   Depois: {variavel_global}")

# 3. Escopo Enclosing (funções aninhadas)
def funcao_externa():
    var_enclosing = "Sou Enclosing"
    def funcao_interna():
        # A função interna pode ler a variável da função externa
        print(f"3. Acesso ao escopo enclosing: {var_enclosing}")
    funcao_interna()
funcao_externa()

# 4. Modificando uma variável do escopo enclosing com `nonlocal`
def funcao_externa_nonlocal():
    contador = 0
    def incrementa():
        nonlocal contador
        contador += 1
        return contador
    print(f"4. Contador (nonlocal): {incrementa()}, {incrementa()}")
funcao_externa_nonlocal()

# 5. Shadowing (Sombreamento) de variáveis
x = 100 # Global
def funcao_shadow():
    x = 10 # Local (sombreia a global)
    print(f"5. Dentro da função, x é {x}")
funcao_shadow()
print(f"   Fora da função, x ainda é {x}")

# 6. Escopo Built-in
print(f"6. Acessando uma função built-in: {len([1, 2, 3])}")
# sum = lambda a, b: a + b # NÃO FAÇA ISSO! Sombreia a função `sum()` built-in.

# 7. LEGB em ação
a = "Global"
def enclosing_func():
    a = "Enclosing"
    def local_func():
        a = "Local"
        print(f"7. LEGB: Nível mais próximo (Local): {a}")
    local_func()
    print(f"   LEGB: Próximo nível (Enclosing): {a}")
enclosing_func()
print(f"   LEGB: Nível mais externo (Global): {a}")

# 8. `global` em loops (não recomendado, mas possível)
total_global = 0
def adiciona_ao_total(valor):
    global total_global
    total_global += valor
adiciona_ao_total(10)
adiciona_ao_total(20)
print(f"8. Total global acumulado: {total_global}")

# 9. `nonlocal` com múltiplos níveis de aninhamento
def nivel1():
    var1 = "Nível 1"
    def nivel2():
        nonlocal var1
        var1 = "Modificado no Nível 2"
    nivel2()
    print(f"9. `nonlocal` em múltiplos níveis: {var1}")
nivel1()

# 10. Interação de escopos
g = 1
def func_escopo(a):
    b = 2
    def interna(c):
        d = 3
        print(f"10. Acesso a todos os escopos: g={g}, a={a}, b={b}, c={c}, d={d}")
    interna(99)
func_escopo(100)
print("-" * 20 + "\n")


# 7. Argumentos Arbitrários (*args e **kwargs)
# --------------------------------------------------------------------
# Permitem que uma função aceite um número indefinido de argumentos.
# `*args`: agrupa argumentos posicionais extras em uma tupla.
# `**kwargs`: agrupa argumentos nomeados extras em um dicionário.

print("--- 7. Argumentos Arbitrários e Forçados (10 Exemplos) ---")

# 1. Uso básico de `*args` para somar números
def somar_tudo(*args: float) -> float:
    print(f"1. Recebido em args: {args}")
    return sum(args)
print(f"   Soma: {somar_tudo(1, 2, 3, 4.5)}")

# 2. Uso básico de `**kwargs` para exibir configurações
def exibir_config(**kwargs: Any) -> None:
    print("2. Configurações recebidas em kwargs:")
    for chave, valor in kwargs.items():
        print(f"   - {chave}: {valor}")
exibir_config(user="admin", theme="dark", notifications=True)

# 3. Combinando `*args` e `**kwargs` com parâmetros normais
def relatorio_completo(reporter: str, *scores: int, **details: Any) -> None:
    print(f"3. Relatório por: {reporter}")
    print(f"   Scores: {scores}")
    print(f"   Detalhes: {details}")
relatorio_completo("Ana", 10, 20, 30, data="2023-10-27", status="Concluído")

# 4. Desempacotando uma lista/tupla com `*` na chamada da função
def calcular_volume(comprimento: float, largura: float, altura: float) -> float:
    return comprimento * largura * altura
dimensoes = [10, 5, 2]
print(f"4. Volume (desempacotando lista): {calcular_volume(*dimensoes)}")

# 5. Desempacotando um dicionário com `**` na chamada da função
params = {"largura": 3, "altura": 4, "comprimento": 5}
print(f"5. Volume (desempacotando dict): {calcular_volume(**params)}")

# 6. `*args` para uma função de "log" genérica
def log_evento(evento: str, *participantes: str) -> None:
    print(f"6. Evento '{evento}' com participantes: {', '.join(participantes)}")
log_evento("Reunião", "Ana", "Beto", "Carlos")

# 7. `**kwargs` para criar objetos flexíveis
def criar_personagem(**atributos: Any) -> Dict[str, Any]:
    personagem = {"nome": "Desconhecido", "hp": 100}
    personagem.update(atributos)
    return personagem
guerreiro = criar_personagem(nome="Aragorn", classe="Guerreiro", hp=150)
print(f"7. Personagem criado com kwargs: {guerreiro}")

# 8. Passando `*args` e `**kwargs` para outra função (proxy/wrapper)
def funcao_wrapper(*args, **kwargs):
    print("8. Wrapper: passando argumentos para `criar_relatorio`...")
    criar_relatorio(*args, **kwargs)
funcao_wrapper("Análise de Risco", "Financeiro", versao="3.0")

# 9. Argumentos somente-posicionais com `/` (Python 3.8+)
def dividir_posicional(dividendo, divisor, /):
    print(f"9. Divisão posicional: {dividendo / divisor}")
dividir_posicional(10, 2)
# dividir_posicional(dividendo=10, divisor=2) # TypeError

# 10. Combinando todos os tipos de argumentos
def super_funcao(pos_only, /, std, *, kw_only):
    print(f"10. pos_only: {pos_only}, std: {std}, kw_only: {kw_only}")
super_funcao(1, 2, kw_only=3)
super_funcao(1, std=2, kw_only=3)

# Exemplo extra: Usando `*` para forçar argumentos nomeados sem precisar de `*args`
def forcar_nomeados(*, nome: str, email: str) -> None:
    print(f"10. Usuário: {nome}, Email: {email}")
forcar_nomeados(nome="Diana", email="diana@example.com")
# forcar_nomeados("Diana", "diana@example.com") # TypeError
print("-" * 20 + "\n")


# 8. Funções de Ordem Superior e o Módulo `functools`
# ---------------------------------------------------
# Funções que recebem outras funções como argumentos ou retornam funções.

print("--- 8. Funções de Ordem Superior e `functools` (10 Exemplos) ---")

# 1. `map()`: aplica uma função a cada item de um iterável
numeros = [1, 2, 3, 4]
quadrados = list(map(lambda x: x**2, numeros))
print(f"1. `map` para quadrados: {quadrados}")

# 2. `filter()`: filtra itens de um iterável com base em uma função
numeros_ate_10 = range(11)
pares = list(filter(lambda x: x % 2 == 0, numeros_ate_10))
print(f"2. `filter` para pares: {pares}")

# 3. `sorted()`: ordena um iterável com uma chave de ordenação customizada
pessoas = [("Ana", 25), ("Beto", 30), ("Caio", 20)]
ordenado_por_idade = sorted(pessoas, key=lambda pessoa: pessoa[1])
print(f"3. `sorted` por idade: {ordenado_por_idade}")

# 4. Função que recebe outra função como argumento
def aplicar_operacao(a, b, operacao: Callable):
    return operacao(a, b)
print(f"4. Aplicando soma: {aplicar_operacao(10, 5, lambda x, y: x + y)}")
print(f"   Aplicando multiplicação: {aplicar_operacao(10, 5, lambda x, y: x * y)}")

# 5. Função que retorna outra função (Factory Function / Closure)
def criar_saudacao(prefixo: str) -> Callable[[str], str]:
    def saudar(nome: str) -> str:
        return f"{prefixo}, {nome}!"
    return saudar
bom_dia = criar_saudacao("Bom dia")
print(f"5. Closure: {bom_dia('Maria')}")

# 6. `reduce()` do `functools` para acumular valores
produto_total = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(f"6. `reduce` para produto: {produto_total}")

# 7. Usando `map` com uma função definida (não-lambda)
def para_maiuscula(s: str) -> str:
    return s.upper()
nomes = ["ana", "beto", "caio"]
nomes_maiusculos = list(map(para_maiuscula, nomes))
print(f"7. `map` com função nomeada: {nomes_maiusculos}")

# 8. Usando `filter` para remover valores `None` ou vazios
dados_brutos = [1, 0, "texto", "", None, [], {"a": 1}]
dados_validos = list(filter(None, dados_brutos)) # `None` como função testa se o valor é "truthy"
print(f"8. `filter` para remover falsos: {dados_validos}")

# 9. `sorted` com chave complexa
dicionarios = [{"nome": "C", "valor": 10}, {"nome": "A", "valor": 30}, {"nome": "B", "valor": 20}]
ordenado_por_nome = sorted(dicionarios, key=lambda d: d["nome"])
print(f"9. `sorted` de dicts por nome: {ordenado_por_nome}")

# 10. `functools.partial` para pré-configurar argumentos de uma função
def potencia(base, expoente):
    return base ** expoente

quadrado = partial(potencia, expoente=2)
cubo = partial(potencia, expoente=3)
print(f"10. `partial` para quadrado de 5: {quadrado(5)}")
print(f"    `partial` para cubo de 5: {cubo(5)}")
print("-" * 20 + "\n")


# 9. Funções Lambda (Anônimas)
# -----------------------------
# Funções pequenas, de uma única expressão, sem nome.
# Sintaxe: `lambda argumentos: expressao`

print("--- 9. Funções Lambda (10 Exemplos) ---")

print(f"1. Lambda simples para adicionar 10: {(lambda x: x + 10)(5)}")
print(f"2. Lambda com múltiplos argumentos: {(lambda x, y: x * y)(4, 5)}")
print(f"3. Lambda sem argumentos: {(lambda: 'Olá, Lambda!')()}")

# 4. Usando lambda para ordenar uma lista de strings pelo comprimento
palavras = ["python", "é", "fantástico"]
print(f"4. Ordenando por comprimento: {sorted(palavras, key=lambda p: len(p))}")

# 5. Usando lambda para encontrar o item com maior valor em um dicionário
estoque = {"maçã": 50, "banana": 20, "laranja": 80}
item_mais_estoque = max(estoque, key=lambda k: estoque[k])
print(f"5. Item com mais estoque: {item_mais_estoque}")

# 6. Lambda com expressão condicional (if/else)
classificar = lambda nota: "Aprovado" if nota >= 7 else "Reprovado"
print(f"6. Classificando nota 8: {classificar(8)}")

# 7. Usando lambda em uma list comprehension
quadrados_lambda = [(lambda x: x**2)(i) for i in range(5)]
print(f"7. Lambda em list comprehension: {quadrados_lambda}")

# 8. Armazenando lambdas em um dicionário (estilo "switch")
operacoes = {
    'soma': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
}
print(f"8. Lambda de dicionário: {operacoes['soma']}")

# 9. Lambda para extrair um elemento de uma tupla
pontos_2d = [(1, 9), (4, 3), (2, 7)]
print(f"9. Ordenando pelo segundo elemento da tupla: {sorted(pontos_2d, key=lambda p: p[1])}")

# 10. Lambda como valor padrão de argumento (uso raro, mas possível)
def processar(dados, func=lambda x: x):
    return [func(d) for d in dados]
print(f"10. Lambda como valor padrão: {processar([1, 2, 3], func=lambda x: x * 10)}")
print("-" * 20 + "\n")

# 9. Funções Geradoras e Expressões (`yield`)
# -------------------------------------------
# Funções que produzem uma sequência de valores sob demanda, pausando e
# retomando sua execução. Usam a palavra-chave `yield`.

print("--- 9. Funções Geradoras (10 Exemplos) ---")

# 1. Gerador simples de números
def gerador_simples(n):
    for i in range(n):
        yield i

print("1. Gerador simples:")
for num in gerador_simples(3):
    print(f"   - {num}")

# 2. Gerador para ler linhas de um arquivo (eficiente em memória)
def ler_linhas(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        for linha in f:
            yield linha.strip()
# with open("temp.txt", "w") as f: f.write("linha1\nlinha2")
# print("2. Lendo arquivo com gerador...")
# for linha in ler_linhas("temp.txt"): print(f"   - {linha}")
print("2. (Exemplo de leitura de arquivo com gerador)")

# 3. Gerador da sequência de Fibonacci
def fibonacci_gen(limite):
    a, b = 0, 1
    while a < limite:
        yield a
        a, b = b, a + b
print(f"3. Fibonacci até 30: {list(fibonacci_gen(30))}")

# 4. Expressão Geradora (sintaxe similar a list comprehension)
quadrados_gen = (x*x for x in range(5))
print(f"4. Expressão geradora: {quadrados_gen}")
print(f"   Valores: {list(quadrados_gen)}")

# 5. `yield from` para delegar a outro gerador (Python 3.3+)
def gerador_combinado():
    yield from gerador_simples(3)
    yield from ('a', 'b')
print(f"5. `yield from`: {list(gerador_combinado())}")

# 6. Enviando valores para um gerador com `.send()`
def co_rotina():
    print("6. Co-rotina esperando valor...")
    valor_recebido = yield
    print(f"   Valor recebido: {valor_recebido}")

cr = co_rotina()
next(cr) # Inicia o gerador até o primeiro `yield`
try:
    cr.send("Olá, gerador!")
except StopIteration:
    print("   Co-rotina finalizada.")

# 7. Gerador infinito
def contador_infinito():
    num = 0
    while True:
        yield num
        num += 1
print("7. Pegando os 3 primeiros de um gerador infinito:")
gen_inf = contador_infinito()
print(f"   {next(gen_inf)}, {next(gen_inf)}, {next(gen_inf)}")

# 8. Usando geradores para pipelines de dados
numeros = range(10)
quadrados = (n*n for n in numeros)
pares = (q for q in quadrados if q % 2 == 0)
print(f"8. Pipeline de geradores (pares dos quadrados): {list(pares)}")

# 9. Fechando um gerador com `.close()`
def gerador_com_finally():
    try:
        yield 1
        yield 2
    finally:
        print("9. Gerador fechado!")

g = gerador_com_finally()
next(g)
g.close()

# 10. Gerador para percorrer uma árvore (ex: nós de uma estrutura)
def percorrer_arvore(no):
    yield no['valor']
    for filho in no.get('filhos', []):
        yield from percorrer_arvore(filho)

arvore = {'valor': 'A', 'filhos': [{'valor': 'B'}, {'valor': 'C', 'filhos': [{'valor': 'D'}]}]}
print(f"10. Percorrendo árvore: {list(percorrer_arvore(arvore))}")
print("-" * 20 + "\n")


# 10. Closures e Decorators
# -------------------------
# Closure: Uma função interna que "lembra" do ambiente (variáveis) onde foi criada.
# Decorator: Uma função que modifica ou envolve outra função, usando o conceito de closure.

print("--- 10. Closures e Decorators (10 Exemplos) ---")

# 1. Exemplo básico de Closure
def pai(msg):
    def filho():
        print(f"1. Mensagem da closure: {msg}")
    return filho
minha_closure = pai("Segredo")
minha_closure()

# 2. Decorator simples para log
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"\n2. Chamando {func.__name__}...")
        resultado = func(*args, **kwargs)
        print(f"   {func.__name__} retornou {resultado}")
        return resultado
    return wrapper

@log_decorator
def somar_decorado(a, b):
    return a + b
somar_decorado(5, 3)

# 3. Decorator para medir tempo de execução
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"3. {func.__name__} levou {fim - inicio:.6f} segundos.")
        return resultado
    return wrapper

@timer_decorator
def processamento_lento():
    time.sleep(0.1)
processamento_lento()

# 4. Decorator com argumentos
def repetir(num_vezes):
    def decorator_repetir(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_vezes):
                func(*args, **kwargs)
        return wrapper
    return decorator_repetir

@repetir(num_vezes=3)
def saudar_repetido(nome):
    print(f"   4. Olá, {nome}!")
saudar_repetido("Mundo")

# 5. Preservando metadados da função com `functools.wraps`
def decorator_com_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Docstring do wrapper."""
        return func(*args, **kwargs)
    return wrapper

@decorator_com_wraps
def funcao_com_doc():
    """Docstring original da função."""
    pass
print(f"5. Nome da função decorada: {funcao_com_doc.__name__}")
print(f"   Docstring: {funcao_com_doc.__doc__}")

# 6. Decorator de classe (menos comum)
class ContadorDeChamadas:
    def __init__(self, func):
        self.func = func
        self.num_chamadas = 0
    def __call__(self, *args, **kwargs):
        self.num_chamadas += 1
        print(f"\n6. Chamada nº {self.num_chamadas} para {self.func.__name__}")
        return self.func(*args, **kwargs)

@ContadorDeChamadas
def alguma_funcao():
    pass
alguma_funcao()
alguma_funcao()

# 7. Decorator para cache simples (memoization)
def cache_decorator(func):
    cache = {}
    @wraps(func)
    def wrapper(n):
        if n not in cache:
            print(f"7. Calculando para {n}...")
            cache[n] = func(n)
        return cache[n]
    return wrapper

@cache_decorator
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(5)
fibonacci(5) # Não vai imprimir "Calculando..."

# 8. Empilhando decorators
@timer_decorator
@log_decorator # Este é executado primeiro (de dentro para fora)
def funcao_empilhada(a, b):
    print("   8. Executando a função empilhada...")
    return a + b

funcao_empilhada(10, 20)

# 9. Closure para criar contadores independentes
def criar_contador():
    count = 0
    def contador():
        nonlocal count
        count += 1
        return count
    return contador

contador1 = criar_contador()
contador2 = criar_contador()
print(f"9. Contador 1: {contador1()}, {contador1()}")
print(f"   Contador 2: {contador2()}")

# 10. Decorator para validar tipos de entrada
def validar_tipos(*tipos):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            for val, tipo in zip(args, tipos):
                if not isinstance(val, tipo):
                    raise TypeError(f"Argumento {val} deve ser do tipo {tipo}")
            return func(*args)
        return wrapper
    return decorator

@validar_tipos(int, int)
def multiplicar(a, b):
    return a * b

print(f"\n10. Validação de tipo (sucesso): {multiplicar(5, 4)}")
try:
    multiplicar(5, "4")
except TypeError as e:
    print(f"    Validação de tipo (falha): {e}")
print("-" * 20 + "\n")