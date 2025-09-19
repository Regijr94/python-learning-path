# -*- coding: utf-8 -*-

"""
Guia Definitivo de Erros, Exceções e Debugging em Python

Este arquivo é um guia de estudo completo sobre como lidar com erros e exceções,
e como depurar código em Python.

--------------------------------------------------------------------------------------
Conteúdo:

-- Parte 1: Fundamentos do Tratamento de Erros --
1.  Erros de Sintaxe vs. Exceções (Erros de Execução)
2.  Lendo um Traceback
3.  O Bloco `try...except`: Tratando Exceções
4.  Tratando Exceções Específicas
5.  As Cláusulas `else` e `finally`

-- Parte 2: Tópicos Avançados e Depuração --
6.  Levantando Exceções com `raise`
7.  Criando Exceções Customizadas
8.  A Declaração `assert` para Sanity Checks
9.  Debugging com o Módulo `pdb` (Python Debugger)
10. Usando o Módulo `logging` para Depuração
--------------------------------------------------------------------------------------
"""

import pdb
import logging

# ====================================================================================
# Parte 1: Fundamentos do Tratamento de Erros
# ====================================================================================

# 1. Erros de Sintaxe vs. Exceções (Erros de Execução)
# ----------------------------------------------------
# Erros de Sintaxe (SyntaxError): Ocorrem quando o código não segue as regras da
#   linguagem Python. O interpretador detecta esses erros antes de executar o código.
# Exceções (Exceptions): Ocorrem durante a execução do código (runtime). A sintaxe
#   está correta, mas uma operação ilegal é tentada.

print("--- 1. Erros de Sintaxe vs. Exceções (10 Exemplos) ---")

print("1. Erros de Sintaxe (comentados para o script poder rodar):")
# Exemplo 1: Faltando dois pontos (:) em uma definição de função
# def minha_funcao()
#     pass

# Exemplo 2: Parênteses não fechados
# print("Olá, mundo"

# Exemplo 3: Palavra-chave inválida (erro de digitação)
# prnt("Isso não vai funcionar")

# Exemplo 4: Atribuição a uma literal
# "nome" = "Ana"

# Exemplo 5: `if` sem condição
# if :
#     pass

print("\n2. Exceções (Erros de Execução):")
# Exemplo 6: ZeroDivisionError
try:
    10 / 0
except ZeroDivisionError as e:
    print(f"   - Exceção capturada: {e}")

# Exemplo 7: NameError
try:
    print(variavel_inexistente)
except NameError as e:
    print(f"   - Exceção capturada: {e}")

# Exemplo 8: TypeError
try:
    "2" + 2
except TypeError as e:
    print(f"   - Exceção capturada: {e}")

# Exemplo 9: IndexError
try:
    lista = [1, 2]
    print(lista[5])
except IndexError as e:
    print(f"   - Exceção capturada: {e}")

# Exemplo 10: KeyError
try:
    dicionario = {"chave": "valor"}
    print(dicionario["outra_chave"])
except KeyError as e:
    print(f"   - Exceção capturada: {e}")
print("-" * 20 + "\n")


# 2. Lendo um Traceback
# ---------------------
# Um traceback é o relatório de erro que o Python exibe quando uma exceção não é
# tratada. Ele mostra a "pilha de chamadas" (call stack) até o ponto do erro.
# Deve ser lido de baixo para cima: a última linha é o erro, e as linhas acima
# mostram o caminho que o código percorreu para chegar lá.

print("--- 2. Lendo um Traceback (10 Exemplos) ---")

def funcao_c():
    # Esta função causará o erro
    return 10 / 0

def funcao_b():
    # Esta função chama a função que causa o erro
    return funcao_c()

def funcao_a():
    # Esta é a primeira função na nossa pilha de chamadas
    return funcao_b()

print("1. Analisando um traceback (o código abaixo está comentado):")
# try:
#     funcao_a()
# except ZeroDivisionError:
#     # O traceback seria:
#     # Traceback (most recent call last):
#     #   File "debugging_guide.py", line XX, in <module>
#     #     funcao_a()
#     #   File "debugging_guide.py", line XX, in funcao_a
#     #     return funcao_b()
#     #   File "debugging_guide.py", line XX, in funcao_b
#     #     return funcao_c()
#     #   File "debugging_guide.py", line XX, in funcao_c
#     #     return 10 / 0
#     # ZeroDivisionError: division by zero
print("   - O traceback mostra o caminho: funcao_a -> funcao_b -> funcao_c.")

print("\n2-10. Exemplos de erros e suas mensagens típicas no traceback:")
print("   2. `TypeError: can only concatenate str (not \"int\") to str` -> 'a' + 1")
print("   3. `ValueError: invalid literal for int() with base 10: 'abc'` -> int('abc')")
print("   4. `AttributeError: 'list' object has no attribute 'keys'` -> [].keys()")
print("   5. `FileNotFoundError: [Errno 2] No such file or directory: 'a.txt'` -> open('a.txt')")
print("   6. `ImportError: cannot import name 'non_existent' from 'math'` -> from math import non_existent")
print("   7. `KeyError: 'chave_faltando'` -> d = {}; d['chave_faltando']")
print("   8. `IndexError: list index out of range` -> l = []; l[0]")
print("   9. `RecursionError: maximum recursion depth exceeded` -> f(); def f(): f()")
print("   10. `IndentationError: expected an indented block` -> def f():\nprint('oi')")
print("-" * 20 + "\n")


# 3. O Bloco `try...except`: Tratando Exceções
# --------------------------------------------
# Permite que você "tente" executar um bloco de código que pode falhar. Se uma
# exceção ocorrer, o bloco `except` é executado, evitando que o programa pare.

print("--- 3. O Bloco `try...except` (10 Exemplos) ---")

# 1. Tratamento genérico de erro
try:
    resultado = 10 / 0
except Exception as e:
    print(f"1. Um erro ocorreu: {e}")

# 2. Validando entrada do usuário
try:
    idade = int(input("2. Digite sua idade: "))
    print(f"   - Daqui a 10 anos, você terá {idade + 10} anos.")
except ValueError:
    print("   - Por favor, digite um número válido.")

# 3. Acessando um índice de lista que pode não existir
lista_curta = [1, 2]
try:
    print(f"3. O terceiro elemento é {lista_curta[2]}")
except IndexError:
    print("   - A lista não tem um terceiro elemento.")

# 4. Acessando uma chave de dicionário que pode não existir
d = {"a": 1}
try:
    print(f"4. O valor da chave 'b' é {d['b']}")
except KeyError:
    print("   - A chave 'b' não existe no dicionário.")

# 5. Abrindo um arquivo que pode não existir
try:
    with open("arquivo_fantasma.txt", "r") as f:
        print("5. Arquivo aberto com sucesso.")
except FileNotFoundError:
    print("5. O arquivo não foi encontrado.")

# 6. Múltiplas operações dentro de um `try`
try:
    print("6. Tentando múltiplas operações...")
    num = int("10")
    res = num / 2
    print(f"   - Resultado: {res}")
except Exception as e:
    print(f"   - Erro: {e}")

# 7. Loop que continua mesmo com entradas inválidas
for valor in ["10", "abc", "5"]:
    try:
        print(f"7. Convertendo '{valor}': {int(valor)}")
    except ValueError:
        print(f"   - '{valor}' não é um número válido.")

# 8. Tratando erro de atributo
class ObjetoSimples: pass
obj = ObjetoSimples()
try:
    print(f"8. Atributo: {obj.nome}")
except AttributeError:
    print("   - O objeto não tem o atributo 'nome'.")

# 9. Tratando erro de tipo em operações
try:
    resultado = len(123)
except TypeError as e:
    print(f"9. Erro de tipo: {e}")

# 10. Usando `pass` em um `except` para ignorar um erro silenciosamente
try:
    # Tenta importar uma biblioteca opcional
    import biblioteca_inexistente
    print("10. Biblioteca opcional importada.")
except ImportError:
    print("10. Biblioteca opcional não encontrada, continuando silenciosamente.")
    pass
print("-" * 20 + "\n")


# 4. Tratando Exceções Específicas
# ---------------------------------
# É uma boa prática capturar as exceções mais específicas possíveis, em vez de
# usar um `except Exception` genérico. Isso evita esconder bugs inesperados.

print("--- 4. Tratando Exceções Específicas (10 Exemplos) ---")

# 1. Múltiplos blocos `except` para diferentes erros
def processar_valor(valor):
    try:
        numero = int(valor)
        resultado = 100 / numero
        print(f"1. Resultado para '{valor}': {resultado}")
    except ValueError:
        print(f"   - '{valor}' não é um número inteiro.")
    except ZeroDivisionError:
        print("   - Não é possível dividir por zero.")

processar_valor("10")
processar_valor("abc")
processar_valor("0")

# 2. Agrupando múltiplas exceções em um único `except`
def acessar_colecao(colecao, chave_ou_indice):
    try:
        valor = colecao[chave_ou_indice]
        print(f"\n2. Valor encontrado: {valor}")
    except (IndexError, KeyError):
        print(f"   - Chave ou índice '{chave_ou_indice}' não encontrado na coleção.")

acessar_colecao([1, 2, 3], 5)
acessar_colecao({"a": 1}, "b")

# 3. A ordem dos `except` importa: do mais específico para o mais genérico
try:
    resultado = 1 / 0
except Exception as e: # Este bloco capturaria TUDO
    print("\n3. Capturado por `Exception` genérico (não ideal).")
# except ZeroDivisionError: # Este código nunca seria alcançado
#     print("Capturado por `ZeroDivisionError`.")

# 4. Exemplo correto de ordenação
try:
    resultado = 1 / 0
except ZeroDivisionError:
    print("\n4. Capturado corretamente por `ZeroDivisionError` específico.")
except Exception:
    print("   - Capturado por `Exception` genérico (backup).")

print("\n5-10. Exemplos de exceções específicas:")
print("5. `except FileNotFoundError:` para operações de arquivo.")
print("6. `except ConnectionError:` para problemas de rede (com bibliotecas como `requests`).")
print("7. `except TypeError:` para operações com tipos incompatíveis.")
print("8. `except AttributeError:` quando um método ou atributo não existe.")
print("9. `except KeyboardInterrupt:` para quando o usuário pressiona Ctrl+C.")
print("10. `except UnicodeDecodeError:` ao ler arquivos com a codificação errada.")
print("-" * 20 + "\n")


# 5. As Cláusulas `else` e `finally`
# ----------------------------------
# `else`: Executado somente se o bloco `try` for concluído sem exceções.
# `finally`: Executado sempre, ocorra uma exceção ou não. Ideal para limpeza.

print("--- 5. As Cláusulas `else` e `finally` (10 Exemplos) ---")

# 1. `try-except-else` onde o `else` é executado
try:
    print("1. Tentando uma operação bem-sucedida...")
    resultado = 10 / 2
except ZeroDivisionError:
    print("   - Divisão por zero!")
else:
    print(f"   - `else`: Operação bem-sucedida! Resultado: {resultado}")

# 2. `try-except-else` onde o `else` não é executado
try:
    print("\n2. Tentando uma operação que falha...")
    resultado = 10 / 0
except ZeroDivisionError:
    print("   - `except`: Divisão por zero!")
else:
    print("   - `else`: Este bloco não será executado.")

# 3. `try-finally` para garantir a limpeza
try:
    print("\n3. `finally` sempre executa (sem erro):")
    # Simulando abrir um recurso
finally:
    print("   - `finally`: Limpando recursos.")

# 4. `try-except-finally`
try:
    print("\n4. `finally` sempre executa (com erro):")
    10 / 0
except ZeroDivisionError:
    print("   - `except`: Erro capturado.")
finally:
    print("   - `finally`: Limpando recursos mesmo após o erro.")

# 5. O bloco completo: `try-except-else-finally`
try:
    print("\n5. Bloco completo (sem erro):")
    num = 5
except:
    print("   - `except`")
else:
    print(f"   - `else`: O número é {num}.")
finally:
    print("   - `finally`: Fim da operação.")

# 6. `finally` com `return` dentro do `try`
def funcao_com_finally():
    try:
        print("\n6. `finally` com `return` no `try`:")
        return "Retorno do `try`"
    finally:
        print("   - `finally` executa antes do `return` do `try`.")
print(f"   - {funcao_com_finally()}")

# 7. `finally` com `return` dentro do `except`
def funcao_com_finally_erro():
    try:
        print("\n7. `finally` com `return` no `except`:")
        1/0
    except:
        return "Retorno do `except`"
    finally:
        print("   - `finally` executa antes do `return` do `except`.")
print(f"   - {funcao_com_finally_erro()}")

# 8. Caso de uso: Fechando um arquivo
f = None
try:
    f = open("temp_file.txt", "w")
    f.write("Olá")
    print("\n8. Arquivo aberto e escrito.")
finally:
    if f:
        f.close()
        print("   - Arquivo fechado no `finally`.")

# 9. `else` para separar a lógica de sucesso
try:
    dados = {"chave": "valor"}
    valor = dados["chave"]
except KeyError:
    print("\n9. Chave não encontrada.")
else:
    # Código que depende de `valor` fica aqui
    print(f"\n9. `else`: Processando o valor '{valor.upper()}'")

# 10. `finally` para desbloquear um recurso
print("\n10. `finally` é ideal para liberar `locks` em programação concorrente.")
print("-" * 20 + "\n")


# ====================================================================================
# Parte 2: Tópicos Avançados e Depuração
# ====================================================================================

# 6. Levantando Exceções com `raise`
# ----------------------------------
# Você pode deliberadamente "levantar" ou "disparar" uma exceção usando `raise`.
# Isso é útil para sinalizar que uma condição de erro ocorreu na sua função.

print("--- 6. Levantando Exceções com `raise` (10 Exemplos) ---")

# 1. Levantando uma exceção com uma mensagem
def set_idade(idade):
    if idade < 0:
        raise ValueError("A idade não pode ser negativa.")
    print(f"1. Idade definida como {idade}.")
try:
    set_idade(-5)
except ValueError as e:
    print(f"   - Erro: {e}")

# 2. Re-levantando uma exceção capturada
try:
    resultado = 1 / 0
except ZeroDivisionError as e:
    print("\n2. Re-levantando a exceção original...")
    # raise # Re-levanta a última exceção ativa

# 3. Levantando um tipo de exceção diferente
try:
    int("abc")
except ValueError:
    print("\n3. Levantando `TypeError` a partir de um `ValueError`.")
    # raise TypeError("O valor deve ser numérico.")

# 4. `raise from`: encadeando exceções (melhora o traceback)
try:
    1 / 0
except ZeroDivisionError as e:
    print("\n4. Levantando uma nova exceção a partir da original (`raise from`).")
    # raise ValueError("Erro de cálculo") from e

# 5. `NotImplementedError` para métodos abstratos
class Forma:
    def area(self):
        raise NotImplementedError("Subclasses devem implementar este método.")
try:
    Forma().area()
except NotImplementedError as e:
    print(f"\n5. Erro de método não implementado: {e}")

print("\n6-10. Outros usos comuns de `raise`:")
print("6. `raise TypeError` se o tipo de um argumento for inválido.")
print("7. `raise KeyError` em uma estrutura de dados customizada.")
print("8. `raise RuntimeError` para erros que não se encaixam em outras categorias.")
print("9. `raise StopIteration` para sinalizar o fim de um iterador customizado.")
print("10. `raise` sem argumentos dentro de um `except` para re-lançar a exceção capturada.")
print("-" * 20 + "\n")


# 7. Criando Exceções Customizadas
# --------------------------------
# Criar suas próprias classes de exceção (herdando de `Exception`) torna seu
# código mais claro e permite que os usuários da sua API tratem seus erros de forma específica.

print("--- 7. Criando Exceções Customizadas (10 Exemplos) ---")

# 1. Definição de uma exceção customizada simples
class ErroDeAPI(Exception):
    """Exceção base para erros da nossa API."""
    pass

try:
    raise ErroDeAPI("Falha na comunicação com o servidor.")
except ErroDeAPI as e:
    print(f"1. Capturada exceção customizada: {e}")

# 2. Exceção customizada com atributos extras
class ErroDeValidacao(Exception):
    def __init__(self, mensagem, codigo_erro):
        super().__init__(mensagem)
        self.codigo_erro = codigo_erro

try:
    raise ErroDeValidacao("Campo 'email' inválido.", "VAL-001")
except ErroDeValidacao as e:
    print(f"\n2. Erro de validação: '{e}' (Código: {e.codigo_erro})")

# 3. Criando uma hierarquia de exceções
class ErroDeAutenticacao(ErroDeAPI): pass
class ErroDePermissao(ErroDeAPI): pass

try:
    raise ErroDePermissao("Usuário não tem permissão para acessar este recurso.")
except ErroDeAPI as e: # Captura a exceção filha
    print(f"\n3. Capturado erro da API (hierarquia): {e}")

# 4. Sobrescrevendo `__str__` para uma mensagem de erro melhor
class ErroSaldoInsuficiente(Exception):
    def __init__(self, saldo_atual, valor_saque):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
    def __str__(self):
        return f"Tentativa de sacar {self.valor_saque} com saldo de apenas {self.saldo_atual}."

try:
    raise ErroSaldoInsuficiente(100, 500)
except ErroSaldoInsuficiente as e:
    print(f"\n4. Mensagem de erro customizada: {e}")

print("\n5-10. Outros exemplos de exceções customizadas:")
print("5. `ConfigNotFoundError`: para quando um arquivo de configuração não é encontrado.")
print("6. `DatabaseConnectionError`: para falhas de conexão com o banco de dados.")
print("7. `InvalidStateError`: quando uma operação é chamada em um estado inválido do objeto.")
print("8. `PluginError`: exceção base para um sistema de plugins.")
print("9. `TimeoutError` (customizada): para operações que excedem um tempo limite.")
print("10. `APILimitExceededError`: para quando um limite de uso de API é atingido.")
print("-" * 20 + "\n")


# 8. A Declaração `assert` para Sanity Checks
# -------------------------------------------
# `assert` verifica se uma condição é verdadeira. Se não for, levanta um
# `AssertionError`. É usado para verificações internas durante o desenvolvimento,
# não para tratar erros de usuário. Assertivas podem ser desabilitadas.

print("--- 8. A Declaração `assert` (10 Exemplos) ---")

# 1. Verificando uma pré-condição de uma função
def calcular_desconto(preco, desconto):
    assert 0 <= desconto <= 1, "O desconto deve estar entre 0 e 1."
    return preco * (1 - desconto)
print(f"1. Desconto válido: {calcular_desconto(100, 0.2)}")

# 2. `AssertionError` quando a condição falha
try:
    calcular_desconto(100, 1.5)
except AssertionError as e:
    print(f"\n2. Erro de asserção: {e}")

# 3. Verificando uma pós-condição (o estado após a execução)
def remover_item(lista, item):
    tamanho_inicial = len(lista)
    lista.remove(item)
    assert len(lista) == tamanho_inicial - 1
    return lista
print(f"\n3. Pós-condição verificada: {remover_item([1, 2, 3], 2)}")

# 4. Verificando o tipo de um argumento
def processa_lista(lista_de_numeros):
    assert isinstance(lista_de_numeros, list), "O argumento deve ser uma lista."
    print("4. `assert` de tipo passou.")
processa_lista([1,2])

# 5. Verificando invariantes de um loop
print("\n5. Verificando invariante de loop (soma sempre positiva):")
soma_parcial = 0
for i in [1, 5, -2, 8]:
    soma_parcial += i
    assert soma_parcial > 0, "A soma parcial se tornou negativa!"

print("\n6-10. Outros usos de `assert`:")
print("6. `assert 'id' in dados`, para verificar se uma chave obrigatória existe em um dict.")
print("7. `assert resposta.status_code == 200`, em testes de API.")
print("8. `assert x > 0`, para garantir que uma variável matemática é positiva.")
print("9. `assert len(a) == len(b)`, antes de usar `zip` em duas listas que deveriam ter o mesmo tamanho.")
print("10. `assert not esta_logado()`, para garantir que uma seção de código só é acessada por usuários anônimos.")
print("-" * 20 + "\n")


# 9. Debugging com o Módulo `pdb` (Python Debugger)
# -------------------------------------------------
# `pdb` é o depurador interativo do Python. Permite pausar a execução,
# inspecionar variáveis e executar o código linha a linha.

print("--- 9. Debugging com `pdb` (10 Exemplos/Comandos) ---")

def funcao_complexa(a, b):
    resultado_intermediario = a * 10
    # Para iniciar o debugger aqui, descomente a linha abaixo:
    # pdb.set_trace()
    resultado_final = resultado_intermediario + b
    return resultado_final

print("1. Inserindo um breakpoint com `pdb.set_trace()` (código comentado).")
print("   - Dentro do `pdb`, você pode usar comandos como:")
print("   2. `l` (list): mostra o código ao redor da linha atual.")
print("   3. `n` (next): executa a próxima linha.")
print("   4. `c` (continue): continua a execução até o próximo breakpoint ou o fim.")
print("   5. `s` (step): entra em uma chamada de função.")
print("   6. `p <variavel>` (print): imprime o valor de uma variável (ex: `p a`).")
print("   7. `q` (quit): sai do debugger e encerra o script.")
print("   8. `bt` (backtrace): mostra a pilha de chamadas.")
print("   9. `h` (help): mostra a ajuda dos comandos do `pdb`.")
print("10. `r` (return): continua a execução até o retorno da função atual.")

# Exemplo de execução:
# resultado = funcao_complexa(5, 3)
# print(f"Resultado final: {resultado}")
print("-" * 20 + "\n")


# 10. Usando o Módulo `logging` para Depuração
# --------------------------------------------
# O módulo `logging` é uma alternativa mais poderosa e flexível ao `print()`
# para depuração e monitoramento. Permite diferentes níveis de severidade.

print("--- 10. Usando o Módulo `logging` (10 Exemplos) ---")

# 1. Configuração básica do logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 2. Nível DEBUG: Informação detalhada, tipicamente de interesse apenas para diagnóstico.
logging.debug("1. Esta é uma mensagem de debug.")

# 3. Nível INFO: Confirmação de que as coisas estão funcionando como esperado.
logging.info("2. O serviço foi iniciado com sucesso.")

# 4. Nível WARNING: Indicação de que algo inesperado aconteceu, mas o software ainda funciona.
logging.warning("3. A senha está fraca.")

# 5. Nível ERROR: Devido a um problema mais sério, o software não conseguiu realizar uma função.
logging.error("4. Falha ao conectar ao banco de dados.")

# 6. Nível CRITICAL: Um erro sério, indicando que o programa pode não conseguir continuar.
logging.critical("5. O disco está cheio. O programa não pode continuar.")

# 7. Logando variáveis para depuração
x = 10
logging.debug(f"6. O valor da variável x é {x}.")

# 8. Logando exceções
try:
    1 / 0
except ZeroDivisionError:
    logging.error("7. Ocorreu uma exceção", exc_info=True)

# 9. Logando para um arquivo em vez do console
# handler = logging.FileHandler('app.log')
# logger = logging.getLogger()
# logger.addHandler(handler)
print("\n8. O logging pode ser configurado para escrever em arquivos.")

# 10. Criando loggers separados para diferentes partes da aplicação
db_logger = logging.getLogger("database")
db_logger.info("9. Logger específico para o banco de dados.")

print("\n10. Níveis de log permitem filtrar mensagens em produção (ex: mostrar apenas WARNING e acima).")
print("-" * 20 + "\n")