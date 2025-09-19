# -*- coding: utf-8 -*-

"""
Guia Definitivo de Decorators em Python: Do Básico ao Avançado

Este arquivo é um guia de estudo completo sobre decorators, um dos recursos
mais poderosos e elegantes de Python.

--------------------------------------------------------------------------------------
Conteúdo:

-- Parte 1: Os Pilares dos Decorators --
1.  Funções como Cidadãos de Primeira Classe
2.  Funções de Ordem Superior (Higher-Order Functions)
3.  Closures: O Coração dos Decorators
4.  Sintaxe Básica de um Decorator

-- Parte 2: Construindo Decorators Robustos --
5.  Decorators para Funções com Argumentos (*args, **kwargs)
6.  Retornando Valores da Função Decorada
7.  Preservando Metadados com `functools.wraps`
8.  Decorators com Argumentos Próprios

-- Parte 3: Tópicos Avançados e Casos de Uso --
9.  Decorators de Classe (Stateful Decorators)
10. Casos de Uso Práticos e Avançados
--------------------------------------------------------------------------------------
"""

import time
from functools import wraps

# ====================================================================================
# Parte 1: Os Pilares dos Decorators
# ====================================================================================

# 1. Funções como Cidadãos de Primeira Classe
# -------------------------------------------
# Em Python, funções são objetos como qualquer outro. Elas podem ser:
# - Atribuídas a variáveis.
# - Passadas como argumentos para outras funções.
# - Retornadas de outras funções.
# - Armazenadas em estruturas de dados (listas, dicionários).

print("--- 1. Funções como Cidadãos de Primeira Classe (5 Exemplos) ---")

def saudacao():
    return "Olá, mundo!"

# 1. Atribuindo uma função a uma variável
minha_saudacao = saudacao
print(f"1. Chamando a função através da variável: {minha_saudacao()}")

# 2. Passando uma função como argumento
def executar_funcao(func):
    print("2. Executando a função recebida como argumento:")
    print(f"   - {func()}")
executar_funcao(saudacao)

# 3. Retornando uma função de outra função
def criar_saudador():
    def saudador_interno():
        return "Olá novamente!"
    return saudador_interno

nova_saudacao = criar_saudador()
print(f"3. Chamando a função retornada: {nova_saudacao()}")

# 4. Armazenando funções em uma lista
def somar(a, b): return a + b
def subtrair(a, b): return a - b

operacoes = [somar, subtrair]
print(f"4. Executando função de uma lista: 5 + 3 = {operacoes}")

# 5. Armazenando funções em um dicionário
calculadora = {"soma": somar, "sub": subtrair}
print(f"5. Executando função de um dicionário: 10 - 7 = {calculadora['sub']}")
print("-" * 20 + "\n")


# 2. Funções de Ordem Superior (Higher-Order Functions)
# ----------------------------------------------------
# Uma função de ordem superior é aquela que recebe uma função como argumento,
# retorna uma função, ou ambos.

print("--- 2. Funções de Ordem Superior (5 Exemplos) ---")

# 1. Função que recebe outra função (ex: `map`)
numeros = [1, 2, 3, 4]
quadrados = list(map(lambda x: x**2, numeros))
print(f"1. `map` como função de ordem superior: {quadrados}")

# 2. Função que recebe outra função (ex: `filter`)
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"2. `filter` como função de ordem superior: {pares}")

# 3. Criando nossa própria função de ordem superior
def aplicar_operacao(lista, operacao):
    return [operacao(item) for item in lista]

dobrados = aplicar_operacao([1, 2, 3], lambda x: x * 2)
print(f"3. Nossa HOF para dobrar números: {dobrados}")

# 4. Função que retorna uma função (Factory Function)
def criar_verificador_de_limite(limite):
    def verificador(valor):
        return valor < limite
    return verificador

abaixo_de_10 = criar_verificador_de_limite(10)
print(f"4. Verificando se 5 < 10: {abaixo_de_10(5)}")
print(f"   Verificando se 15 < 10: {abaixo_de_10(15)}")

# 5. Combinando os dois: recebe e retorna uma função
def criar_logger(prefixo):
    def logger(funcao):
        def wrapper():
            print(f"{prefixo}: Chamando a função...")
            funcao()
        return wrapper
    return logger

log_info = criar_logger("[INFO]")
saudacao_logada = log_info(saudacao)
print("5. Usando uma HOF que cria outra HOF:")
saudacao_logada()
print("-" * 20 + "\n")


# 3. Closures: O Coração dos Decorators
# ------------------------------------
# Uma closure ocorre quando uma função aninhada (interna) "lembra" e tem acesso
# às variáveis do escopo da função que a continha (externa), mesmo depois que a
# função externa já terminou sua execução.

print("--- 3. Closures (5 Exemplos) ---")

# 1. Closure básica para multiplicar
def criar_multiplicador(n):
    # `n` é uma "free variable" para a função `multiplicador`
    def multiplicador(x):
        return x * n
    return multiplicador

multiplicar_por_5 = criar_multiplicador(5)
print(f"1. Closure para multiplicar 10 por 5: {multiplicar_por_5(10)}")

# 2. Closure para criar um contador
def criar_contador():
    count = 0
    def contador():
        nonlocal count # Necessário para modificar a variável do escopo externo
        count += 1
        return count
    return contador

contador1 = criar_contador()
print(f"2. Contador 1: {contador1()}, {contador1()}, {contador1()}")

# 3. Closure para armazenar uma mensagem
def guardar_mensagem(msg):
    def mostrar_mensagem():
        print(f"3. Mensagem guardada: {msg}")
    return mostrar_mensagem

minha_msg = guardar_mensagem("Python é incrível!")
minha_msg()

# 4. Closure para criar uma função de potência
def criar_potenciador(expoente):
    return lambda base: base ** expoente

ao_cubo = criar_potenciador(3)
print(f"4. 4 ao cubo: {ao_cubo(4)}")

# 5. Verificando as "free variables" de uma closure
print(f"5. Variáveis livres da closure `multiplicar_por_5`: {multiplicar_por_5.__code__.co_freevars}")
print("-" * 20 + "\n")


# 4. Sintaxe Básica de um Decorator
# ---------------------------------
# Um decorator é, essencialmente, uma função que recebe outra função, adiciona
# alguma funcionalidade e retorna a função modificada (ou uma nova função).

print("--- 4. Sintaxe Básica de um Decorator (5 Exemplos) ---")

# 1. Definição de um decorator simples
def meu_primeiro_decorator(func):
    def wrapper():
        print("1. Algo acontece ANTES da função ser chamada.")
        func()
        print("   Algo acontece DEPOIS da função ser chamada.")
    return wrapper

# 2. Aplicando o decorator manualmente (a forma "longa")
def diz_ola():
    print("   Olá!")

diz_ola_decorado = meu_primeiro_decorator(diz_ola)
diz_ola_decorado()

# 3. Aplicando o decorator com a sintaxe de "açúcar sintático" `@`
@meu_primeiro_decorator
def diz_tchau():
    print("   Tchau!")

print("\n3. Usando a sintaxe `@`:")
diz_tchau()

# 4. Decorator que imprime o nome da função
def informa_nome_funcao(func):
    def wrapper():
        print(f"\n4. Executando a função: '{func.__name__}'")
        func()
    return wrapper

@informa_nome_funcao
def outra_funcao():
    print("   Esta é outra função.")
outra_funcao()

# 5. Reutilizando o mesmo decorator em múltiplas funções
@informa_nome_funcao
def mais_uma_funcao():
    print("   Esta é mais uma função.")

print("\n5. Reutilizando o decorator:")
mais_uma_funcao()
print("-" * 20 + "\n")


# ====================================================================================
# Parte 2: Construindo Decorators Robustos
# ====================================================================================

# 5. Decorators para Funções com Argumentos (*args, **kwargs)
# -----------------------------------------------------------
# Para que um decorator funcione com qualquer função, a função `wrapper` interna
# precisa aceitar quaisquer argumentos posicionais e nomeados.

print("--- 5. Decorators para Funções com Argumentos (5 Exemplos) ---")

def decorator_flexivel(func):
    def wrapper(*args, **kwargs):
        print("1. Decorator flexível: ANTES da chamada.")
        func(*args, **kwargs)
        print("   Decorator flexível: DEPOIS da chamada.")
    return wrapper

# 1. Decorando uma função sem argumentos
@decorator_flexivel
def funcao_simples():
    print("   - Função simples executada.")
funcao_simples()

# 2. Decorando uma função com argumentos posicionais
@decorator_flexivel
def somar_flex(a, b):
    print(f"\n2. Soma: {a + b}")
somar_flex(10, 20)

# 3. Decorando uma função com argumentos nomeados
@decorator_flexivel
def exibir_info_flex(nome, idade):
    print(f"\n3. Info: {nome}, {idade} anos.")
exibir_info_flex(nome="Carlos", idade=40)

# 4. Decorando uma função com argumentos mistos
@decorator_flexivel
def relatorio_flex(titulo, autor="Desconhecido"):
    print(f"\n4. Relatório '{titulo}' por {autor}.")
relatorio_flex("Vendas", autor="Equipe")

# 5. Decorator que inspeciona os argumentos
def inspeciona_args(func):
    def wrapper(*args, **kwargs):
        print(f"\n5. Inspecionando argumentos para '{func.__name__}':")
        print(f"   - Argumentos posicionais: {args}")
        print(f"   - Argumentos nomeados: {kwargs}")
        func(*args, **kwargs)
    return wrapper

@inspeciona_args
def funcao_teste(a, b, c="padrão"):
    pass
funcao_teste(1, "dois", c="três")
print("-" * 20 + "\n")


# 6. Retornando Valores da Função Decorada
# ----------------------------------------
# O `wrapper` deve capturar e retornar o valor da função original.

print("--- 6. Retornando Valores (5 Exemplos) ---")

def decorator_com_retorno(func):
    def wrapper(*args, **kwargs):
        print("1. ANTES da função que retorna um valor.")
        resultado = func(*args, **kwargs)
        print(f"   DEPOIS. A função retornou: {resultado}")
        return resultado
    return wrapper

# 1. Decorando uma função que retorna um número
@decorator_com_retorno
def multiplicar(a, b):
    return a * b

res_mult = multiplicar(5, 4)
print(f"   Valor final recebido: {res_mult}")

# 2. Decorando uma função que retorna uma string
@decorator_com_retorno
def formatar_nome(primeiro, ultimo):
    return f"{primeiro.title()} {ultimo.title()}"

print("\n2. Decorando função que retorna string:")
nome_formatado = formatar_nome("joão", "silva")
print(f"   Nome final recebido: {nome_formatado}")

# 3. Decorator que modifica o valor de retorno
def para_maiusculas(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado.upper()
    return wrapper

@para_maiusculas
def saudacao_minuscula():
    return "olá, como vai?"

print(f"\n3. Decorator que modifica o retorno: '{saudacao_minuscula()}'")

# 4. Decorator que retorna um tipo diferente
def para_dicionario(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return {"resultado": resultado, "timestamp": time.time()}
    return wrapper

@para_dicionario
def obter_status():
    return "OK"

print(f"\n4. Decorator que muda o tipo do retorno: {obter_status()}")

# 5. Decorator que não retorna nada (perde o valor da função original)
def decorator_sem_retorno(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs) # Não captura nem retorna o resultado
    return wrapper

@decorator_sem_retorno
def somar_perdido(a, b):
    return a + b

resultado_perdido = somar_perdido(1, 2)
print(f"\n5. Valor perdido por decorator sem `return`: {resultado_perdido}")
print("-" * 20 + "\n")


# 7. Preservando Metadados com `functools.wraps`
# ---------------------------------------------
# Decorators substituem a função original pela função `wrapper`. Isso faz com que
# metadados como o nome (`__name__`) e a docstring (`__doc__`) sejam perdidos.
# `@wraps` do módulo `functools` resolve isso.

print("--- 7. Preservando Metadados com `functools.wraps` (5 Exemplos) ---")

def decorator_sem_wraps(func):
    def wrapper():
        """Docstring do wrapper."""
        func()
    return wrapper

@decorator_sem_wraps
def funcao_sem_wraps():
    """Docstring original da função sem wraps."""
    pass

print(f"1. Sem @wraps - Nome: {funcao_sem_wraps.__name__}")
print(f"2. Sem @wraps - Docstring: {funcao_sem_wraps.__doc__}")

def decorator_com_wraps(func):
    @wraps(func) # Copia os metadados da função original para o wrapper
    def wrapper():
        """Docstring do wrapper (não será vista)."""
        func()
    return wrapper

@decorator_com_wraps
def funcao_com_wraps():
    """Docstring original da função com wraps."""
    pass

print(f"\n3. Com @wraps - Nome: {funcao_com_wraps.__name__}")
print(f"4. Com @wraps - Docstring: {funcao_com_wraps.__doc__}")

print("\n5. Use `help(funcao_com_wraps)` para ver a ajuda correta, graças ao `@wraps`.")
print("-" * 20 + "\n")


# 8. Decorators com Argumentos Próprios
# -------------------------------------
# Para criar um decorator que aceita seus próprios argumentos (ex: `@repetir(n=3)`),
# é necessária uma camada extra de função.

print("--- 8. Decorators com Argumentos (5 Exemplos) ---")

# Estrutura: uma função que retorna um decorator.
def repetir(num_vezes):
    def decorator_repetir(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"1. Repetindo {num_vezes} vezes:")
            for _ in range(num_vezes):
                func(*args, **kwargs)
        return wrapper
    return decorator_repetir

# 1. Usando o decorator com argumento
@repetir(num_vezes=3)
def saudar_repetido(nome):
    print(f"   - Olá, {nome}!")
saudar_repetido("Equipe")

# 2. Decorator para adicionar um prefixo de log
def log_com_prefixo(prefixo):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"\n2. {prefixo}: {func.__name__} foi chamada.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_com_prefixo("[INFO]")
def operacao_importante():
    pass
operacao_importante()

# 3. Decorator para verificar tipo de retorno
def esperar_tipo(tipo_esperado):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            resultado = func(*args, **kwargs)
            assert isinstance(resultado, tipo_esperado), f"Esperava {tipo_esperado}, recebeu {type(resultado)}"
            return resultado
        return wrapper
    return decorator

@esperar_tipo(int)
def somar_inteiros(a, b):
    return a + b

print(f"\n3. Verificação de tipo (sucesso): {somar_inteiros(1, 2)}")

# 4. Decorator com argumento opcional
def meu_log(func=None, *, prefixo="[LOG]"):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print(f"\n4. {prefixo} {f.__name__}")
            return f(*args, **kwargs)
        return wrapper
    if func is None:
        return decorator # Chamado como @meu_log(prefixo="...")
    return decorator(func) # Chamado como @meu_log

@meu_log
def funcao_log_padrao(): pass
funcao_log_padrao()

# 5. Decorator para atrasar a execução
def atrasar(segundos):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"\n5. Esperando {segundos}s para executar...")
            time.sleep(segundos)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@atrasar(0.1)
def execucao_atrasada():
    print("   - Executado!")
execucao_atrasada()
print("-" * 20 + "\n")


# ====================================================================================
# Parte 3: Tópicos Avançados e Casos de Uso
# ====================================================================================

# 9. Decorators de Classe (Stateful Decorators)
# ---------------------------------------------
# É possível usar uma classe para implementar um decorator. Isso é útil quando
# o decorator precisa manter um estado (ex: contar quantas vezes uma função foi chamada).

print("--- 9. Decorators de Classe (5 Exemplos) ---")

# 1. Decorator de classe para contar chamadas
class ContadorDeChamadas:
    def __init__(self, func):
        self.func = func
        self.num_chamadas = 0
    
    def __call__(self, *args, **kwargs):
        self.num_chamadas += 1
        print(f"1. Chamada nº {self.num_chamadas} para {self.func.__name__}")
        return self.func(*args, **kwargs)

@ContadorDeChamadas
def funcao_contada():
    pass
funcao_contada()
funcao_contada()

# 2. Decorator de classe com argumentos
class LimiteDeChamadas:
    def __init__(self, limite):
        self.limite = limite
        self.chamadas = 0

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.chamadas += 1
            if self.chamadas > self.limite:
                raise Exception(f"2. Limite de {self.limite} chamadas excedido!")
            return func(*args, **kwargs)
        return wrapper

@LimiteDeChamadas(limite=2)
def funcao_limitada():
    print("   - Função limitada executada.")

print("\n2. Testando limite de chamadas:")
funcao_limitada()
funcao_limitada()
try:
    funcao_limitada()
except Exception as e:
    print(f"   {e}")

# 3. Decorator de classe para registrar o último resultado
class UltimoResultado:
    def __init__(self, func):
        self.func = func
        self.ultimo_resultado = None
    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        self.ultimo_resultado = resultado
        return resultado

@UltimoResultado
def calcula_algo(x):
    return x * 10

print("\n3. Registrando último resultado:")
calcula_algo(5)
print(f"   Último resultado: {calcula_algo.ultimo_resultado}")
calcula_algo(10)
print(f"   Último resultado agora: {calcula_algo.ultimo_resultado}")

# 4. Decorator de classe para singleton (padrão de projeto)
class Singleton:
    def __init__(self, cls):
        self._cls = cls
        self._instance = None
    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._cls(*args, **kwargs)
        return self._instance

@Singleton
class ConexaoDB:
    def __init__(self):
        print("4. (Singleton) Conexão com o DB criada.")

print("\n4. Testando padrão Singleton:")
db1 = ConexaoDB()
db2 = ConexaoDB()
print(f"   db1 é o mesmo objeto que db2? {db1 is db2}")

# 5. Decorator de classe para adicionar um atributo
class AdicionarAtributo:
    def __init__(self, nome_attr, valor_attr):
        self.nome_attr = nome_attr
        self.valor_attr = valor_attr
    def __call__(self, func):
        setattr(func, self.nome_attr, self.valor_attr)
        return func

@AdicionarAtributo("versao", "1.0")
def minha_api():
    pass

print(f"\n5. Atributo adicionado via decorator de classe: {minha_api.versao}")
print("-" * 20 + "\n")


# 10. Casos de Uso Práticos e Avançados
# -------------------------------------

print("--- 10. Casos de Uso Práticos e Avançados (5 Exemplos) ---")

# 1. Decorator de `timing` para medir performance
def cronometrar(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        print(f"1. '{func.__name__}' levou {fim - inicio:.6f}s para executar.")
        return resultado
    return wrapper

@cronometrar
def processamento_demorado():
    sum(i*i for i in range(1000000))
processamento_demorado()

# 2. Decorator de `cache` (memoization) para otimizar chamadas repetidas
def cache(func):
    cache_resultados = {}
    @wraps(func)
    def wrapper(n):
        if n not in cache_resultados:
            print(f"   - Calculando fib({n})...")
            cache_resultados[n] = func(n)
        return cache_resultados[n]
    return wrapper

@cache
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\n2. Testando cache com Fibonacci:")
fibonacci(10)
fibonacci(10) # Esta chamada será instantânea

# 3. Decorator para controle de acesso (ex: verificar se usuário está logado)
def login_necessario(func):
    @wraps(func)
    def wrapper(usuario, *args, **kwargs):
        if usuario.get("logado"):
            return func(usuario, *args, **kwargs)
        else:
            raise PermissionError("3. Acesso negado. Usuário não está logado.")
    return wrapper

@login_necessario
def painel_secreto(usuario):
    print(f"   - Bem-vindo ao painel secreto, {usuario['nome']}!")

print("\n3. Testando controle de acesso:")
usuario_logado = {"nome": "Ana", "logado": True}
usuario_deslogado = {"nome": "Beto", "logado": False}
painel_secreto(usuario_logado)
try:
    painel_secreto(usuario_deslogado)
except PermissionError as e:
    print(f"   {e}")

# 4. Decorator para registrar informações de debug
def debug_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n4. [DEBUG] Chamando '{func.__name__}' com args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"   [DEBUG] '{func.__name__}' retornou: {resultado}")
        return resultado
    return wrapper

@debug_info
def multiplicar_debug(a, b):
    return a * b
multiplicar_debug(3, 4)

# 5. Empilhando decorators
# Os decorators são aplicados de baixo para cima.
@cronometrar
@debug_info
def funcao_empilhada(x):
    print("   - Executando função empilhada...")
    time.sleep(0.1)
    return x * 2

print("\n5. Testando decorators empilhados:")
funcao_empilhada(10)
print("-" * 20 + "\n")