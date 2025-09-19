# -*- coding: utf-8 -*-

"""
Guia Definitivo de Módulos e Pacotes em Python

Este arquivo é um guia de estudo completo sobre como criar, importar e gerenciar
módulos e pacotes em Python.

--------------------------------------------------------------------------------------
Conteúdo:

-- Parte 1: Fundamentos --
1.  O que são Módulos?
2.  A Declaração `import`: Importando Módulos Inteiros
3.  A Declaração `from ... import`: Importando Nomes Específicos
4.  Renomeando Módulos e Funções com `as` (Aliasing)
5.  Criando Seus Próprios Módulos

-- Parte 2: Tópicos Intermediários e Avançados --
6.  O Caminho de Busca de Módulos (`sys.path`)
7.  Pacotes e o Arquivo `__init__.py`
8.  Importações Absolutas vs. Relativas
9.  O Bloco `if __name__ == '__main__'`
10. Problemas Comuns: Importações Circulares
11. Ambientes Virtuais e Gerenciamento de Dependências
12. Tópicos Avançados de Importação
--------------------------------------------------------------------------------------
"""

import sys
import os

# ====================================================================================
# Parte 1: Fundamentos
# ====================================================================================

# 1. O que são Módulos?
# ---------------------
# Um módulo é simplesmente um arquivo Python (`.py`) contendo definições e
# declarações. Ele permite organizar o código de forma lógica e reutilizá-lo.
# Python vem com uma vasta biblioteca padrão de módulos.

print("--- 1. O que são Módulos? (5 Exemplos de uso) ---")

# Exemplo 1: Usando o módulo `math` para constantes e funções matemáticas
import math
print(f"1. O valor de PI é {math.pi} e a raiz quadrada de 16 é {math.sqrt(16)}")

# Exemplo 2: Usando o módulo `random` para gerar números aleatórios
import random
print(f"2. Um número aleatório entre 1 e 10: {random.randint(1, 10)}")

# Exemplo 3: Usando o módulo `datetime` para trabalhar com datas e horas
import datetime
print(f"3. A data e hora atuais são: {datetime.datetime.now()}")

# Exemplo 4: Usando o módulo `sys` para interagir com o interpretador Python
print(f"4. Esta versão do Python é: {sys.version[:5]}")

# Exemplo 5: Usando o módulo `os` para interagir com o sistema operacional
print(f"5. O diretório de trabalho atual é: {os.getcwd()}")
print("-" * 20 + "\n")


# 2. A Declaração `import`: Importando Módulos Inteiros
# -----------------------------------------------------
# A forma mais simples de importação. O módulo inteiro é carregado, e você
# precisa usar o nome do módulo como prefixo para acessar suas funções/variáveis.

print("--- 2. A Declaração `import` (5 Exemplos) ---")

# Exemplo 1: Importando e usando o módulo `math`
import math
print(f"1. Cosseno de 0: {math.cos(0)}")

# Exemplo 2: Importando múltiplos módulos na mesma linha
import os, sys
print(f"2. Plataforma do SO: {sys.platform}, Separador de caminho: {os.sep}")

# Exemplo 3: Importando um submódulo
import urllib.request
print("3. O módulo `urllib.request` foi importado.")

# Exemplo 4: O namespace do módulo evita conflitos de nome
pi = "Uma torta"
print(f"4. Minha variável `pi` é '{pi}', mas `math.pi` ainda é {math.pi}")

# Exemplo 5: Importar um módulo que já foi importado não o recarrega
import math
print("5. Importar `math` novamente não tem efeito extra.")
print("-" * 20 + "\n")


# 3. A Declaração `from ... import`: Importando Nomes Específicos
# ----------------------------------------------------------------
# Permite importar nomes específicos (funções, classes, variáveis) de um módulo
# diretamente para o namespace atual, sem a necessidade de usar o prefixo do módulo.

print("--- 3. A Declaração `from ... import` (5 Exemplos) ---")

# Exemplo 1: Importando funções específicas do módulo `math`
from math import sqrt, pow
print(f"1. Raiz de 25 é {sqrt(25)} e 2 elevado a 3 é {pow(2, 3)}")

# Exemplo 2: Importando uma classe do módulo `datetime`
from datetime import date
hoje = date.today()
print(f"2. A data de hoje é: {hoje}")

# Exemplo 3: Importando uma constante
from math import pi
print(f"3. Usando `pi` diretamente: {pi}")

# Exemplo 4: Importando múltiplos nomes
from random import randint, choice
print(f"4. Sorteio: {randint(1, 100)}, Escolha: {choice(['A', 'B', 'C'])}")

# Exemplo 5: Importando tudo com `*` (NÃO RECOMENDADO)
# Isso polui o namespace e pode causar conflitos de nome difíceis de depurar.
from collections import *
contador = Counter("abracadabra") # Counter vem de `collections`
print(f"5. Usando `Counter` após `import *`: {contador}")
print("-" * 20 + "\n")


# 4. Renomeando Módulos e Funções com `as` (Aliasing)
# ---------------------------------------------------
# `as` permite criar um "apelido" para um módulo ou nome importado. É útil para
# evitar conflitos de nome ou para encurtar nomes longos.

print("--- 4. Renomeando com `as` (5 Exemplos) ---")

# Exemplo 1: Renomeando um módulo inteiro
import numpy as np # Convenção muito comum na comunidade de ciência de dados
print("1. Módulo `numpy` importado como `np`.")

# Exemplo 2: Renomeando uma função importada
from math import pow as potencia
print(f"2. Usando `potencia` como apelido para `pow`: {potencia(3, 2)}")

# Exemplo 3: Evitando conflito de nomes
from csv import reader as leitor_csv

class MeuReader:
    pass

print("3. `leitor_csv` e `MeuReader` podem coexistir sem conflito.")

# Exemplo 4: Renomeando uma classe
from datetime import datetime as DataHora
agora = DataHora.now()
print(f"4. Usando `DataHora` como apelido para `datetime`: {agora}")

# Exemplo 5: Renomeando múltiplos imports
from random import randint as inteiro_aleatorio, choice as escolha_aleatoria
print(f"5. Apelidos múltiplos: {inteiro_aleatorio(1, 5)}, {escolha_aleatoria('xyz')}")
print("-" * 20 + "\n")


# 5. Criando Seus Próprios Módulos
# --------------------------------
# Qualquer arquivo `.py` pode ser um módulo. Para usar, basta que ele esteja
# no mesmo diretório ou em um diretório listado no `sys.path`.

print("--- 5. Criando Seus Próprios Módulos (5 Exemplos) ---")

# Para estes exemplos, imagine um arquivo `meu_modulo.py` com o seguinte conteúdo:
#
# PI = 3.14
# def saudar(nome):
#     return f"Olá do meu módulo, {nome}!"
# class Ferramenta:
#     pass
print("1. Crie um arquivo `meu_modulo.py` no mesmo diretório.")

# Exemplo 2: Importando o módulo inteiro
import meu_modulo
print(f"2. Acessando variável do módulo: {meu_modulo.PI}")

# Exemplo 3: Chamando uma função do nosso módulo
print(f"3. Chamando função do módulo: {meu_modulo.saudar('Mundo')}")

# Exemplo 4: Importando nomes específicos do nosso módulo
from meu_modulo import PI, Ferramenta
print(f"4. Usando a constante PI diretamente: {PI}")

# Exemplo 5: Usando a classe importada
ferramenta = Ferramenta()
print(f"5. Instanciando a classe importada: {ferramenta}")

print("-" * 20 + "\n")


# ====================================================================================
# Parte 2: Tópicos Intermediários e Avançados
# ====================================================================================

# 6. O Caminho de Busca de Módulos (`sys.path`)
# ---------------------------------------------
# `sys.path` é uma lista de strings que especifica os diretórios onde o Python
# procura por módulos. A ordem é:
# 1. O diretório do script atual.
# 2. Os diretórios na variável de ambiente `PYTHONPATH`.
# 3. Os diretórios de instalação padrão do Python.

print("--- 6. O Caminho de Busca de Módulos (`sys.path`) (5 Exemplos) ---")

# Exemplo 1: Visualizando o `sys.path`
print("1. O `sys.path` atual contém:")
for i, path in enumerate(sys.path):
    if i < 3: print(f"   - {path}") # Mostra apenas os primeiros

# Exemplo 2: Adicionando um diretório ao `sys.path` em tempo de execução
caminho_customizado = "/caminho/para/meus/modulos"
sys.path.append(caminho_customizado)
print(f"\n2. Adicionado '{caminho_customizado}' ao sys.path.")
sys.path.remove(caminho_customizado) # Limpeza

# Exemplo 3: O primeiro diretório é o do script atual
print(f"\n3. O primeiro caminho na lista é geralmente o diretório do script: '{sys.path[0]}'")

# Exemplo 4: Verificando se um módulo está em um caminho específico
print(f"\n4. O módulo `os` está localizado em: {os.__file__}")

# Exemplo 5: Python não encontrará um módulo se ele não estiver no `sys.path`
try:
    import modulo_que_nao_existe
except ModuleNotFoundError as e:
    print(f"\n5. Erro esperado ao importar módulo inexistente: {e}")
print("-" * 20 + "\n")


# 7. Pacotes (Packages): Organizando Módulos em Diretórios
# --------------------------------------------------------
# Um pacote é uma forma de estruturar o namespace de módulos usando "nomes de
# módulo pontilhados". Um diretório se torna um pacote se contiver um arquivo
# `__init__.py` (pode estar vazio).

print("--- 7. Pacotes e o Arquivo `__init__.py` (5 Exemplos) ---")

# Imagine a seguinte estrutura de diretórios:
# meu_pacote/
# ├── __init__.py
# ├── utils.py
# └── calculos.py
print("1. A estrutura de diretório `meu_pacote/` foi criada.")

# Exemplo 2: Importando um módulo de um pacote
import meu_pacote.utils
print("\n2. Usando uma função do módulo `utils` do pacote:")
meu_pacote.utils.log("Teste de log")

# Exemplo 3: Usando `from` para importar um módulo do pacote
from meu_pacote import calculos
resultado = calculos.somar(5, 5)
print(f"\n3. Resultado da soma do módulo `calculos`: {resultado}")

# Exemplo 4: Importando uma função específica de um módulo dentro de um pacote
from meu_pacote.calculos import somar
resultado = somar(10, 3)
print(f"\n4. Importando `somar` diretamente: {resultado}")

# Exemplo 5: O papel do `__init__.py`
# Pode ser usado para inicializar o pacote ou expor funções de submódulos.
# Se `meu_pacote/__init__.py` contiver `from .utils import log`, você poderia fazer:
# from meu_pacote import log
print("\n5. O arquivo `__init__.py` pode simplificar a API de um pacote.")
print("-" * 20 + "\n")


# 8. Importações Absolutas vs. Relativas
# ---------------------------------------
# - Absoluta: Especifica o caminho completo a partir da raiz do projeto. É a forma preferida.
# - Relativa: Especifica o caminho relativo ao módulo atual, usando `.` e `..`.

print("--- 8. Importações Absolutas vs. Relativas (5 Exemplos) ---")

# Dentro de `meu_pacote/calculos.py`:
# Exemplo 1: Importação absoluta (preferível)
# from meu_pacote import utils
print("1. Importação absoluta: `from meu_pacote import utils`")

# Exemplo 2: Importação relativa (dentro do mesmo pacote)
# from . import utils  # O `.` se refere ao pacote atual (`meu_pacote`)
print("2. Importação relativa: `from . import utils`")

# Imagine a estrutura: `meu_pacote/sub_pacote/modulo_x.py`
# Dentro de `modulo_x.py`:
# Exemplo 3: Importação relativa para "subir" um nível
# from .. import utils # O `..` sobe para `meu_pacote` e importa `utils`
print("3. Importação relativa para subir nível: `from .. import utils`")

# Exemplo 4: Importações absolutas são mais legíveis e menos frágeis
print("4. Vantagem da absoluta: `from meu_pacote.utils import ...` é claro e não quebra se o arquivo for movido.")

# Exemplo 5: Importações relativas só podem ser usadas dentro de pacotes
# Tentar uma importação relativa em um script de nível superior causa um `ImportError`.
print("5. Importações relativas não funcionam em scripts de nível superior.")
print("-" * 20 + "\n")


# 9. O Bloco `if __name__ == '__main__'`
# --------------------------------------
# Este bloco de código só é executado quando o arquivo Python é rodado
# diretamente (como um script), e não quando é importado como um módulo.

print("--- 9. O Bloco `if __name__ == '__main__'` (5 Exemplos) ---")

# Exemplo 1: Verificando o valor de `__name__`
print(f"1. Neste script, o valor de `__name__` é: '{__name__}'")

# Exemplo 2: Código dentro do bloco
if __name__ == "__main__":
    print("2. Este código está dentro do bloco `if __name__ == '__main__'` e será executado.")

# Exemplo 3: Código fora do bloco
print("3. Este código está fora do bloco e sempre será executado, mesmo em importação.")

# Em um arquivo `meu_modulo.py`:
# def funcao_principal():
#     print("Função principal do módulo executada.")
# if __name__ == "__main__":
#     funcao_principal()
print("\n4. Um módulo com este bloco pode ser usado para testes ou como um script.")

# Exemplo 5: Importando o módulo
# Se você importar `meu_modulo`, `funcao_principal` não será chamada automaticamente.
print("5. Ao importar um módulo, o código dentro de `if __name__ == '__main__'` não é executado.")
print("-" * 20 + "\n")


# 10. Problemas Comuns: Importações Circulares
# --------------------------------------------
# Ocorre quando o Módulo A importa o Módulo B, e o Módulo B importa o Módulo A.
# Isso geralmente leva a um `ImportError` ou `AttributeError`.

print("--- 10. Problemas Comuns: Importações Circulares (5 Exemplos) ---")

# Imagine dois arquivos: `a.py` e `b.py`
#
# a.py:
# import b
# def funcao_a():
#     print("Função A")
#     b.funcao_b()
# funcao_a()
#
# b.py:
# import a
# def funcao_b():
#     print("Função B")
# a.funcao_a() # Isso causaria um loop infinito de chamadas

print("1. Uma importação circular ocorre quando `a.py` importa `b.py` e vice-versa.")
print("2. O resultado pode ser um `ImportError` se um módulo tentar usar uma função do outro antes de ser definida.")
print("3. Outro resultado pode ser um `AttributeError` pelo mesmo motivo.")
print("4. Solução 1: Refatorar o código para que a dependência mútua não exista (ex: mover código compartilhado para um terceiro módulo).")
print("5. Solução 2: Adiar a importação para dentro da função que a utiliza (importação local), mas isso é geralmente um sinal de má arquitetura.")
print("-" * 20 + "\n")


# 11. Ambientes Virtuais e Gerenciamento de Dependências
# ------------------------------------------------------
# Ambientes virtuais isolam as dependências de um projeto, evitando conflitos
# entre diferentes projetos que podem precisar de versões diferentes da mesma biblioteca.

print("--- 11. Ambientes Virtuais e Gerenciamento de Dependências (5 Exemplos) ---")

print("1. Criando um ambiente virtual (no terminal): `python3 -m venv .venv`")
print("2. Ativando o ambiente (no terminal Linux/macOS): `source .venv/bin/activate`")
print("3. `pip`: O gerenciador de pacotes do Python, usado para instalar bibliotecas do PyPI.")
print("   - `pip install requests`")
print("   - `pip uninstall requests`")
print("4. `requirements.txt`: Um arquivo para listar as dependências do projeto.")
print("   - Criando o arquivo: `pip freeze > requirements.txt`")
print("   - Instalando a partir do arquivo: `pip install -r requirements.txt`")
print("5. Isolamento: Pacotes instalados em um ambiente virtual não afetam o sistema global ou outros ambientes.")
print("-" * 20 + "\n")


# 12. Tópicos Avançados de Importação
# -----------------------------------

print("--- 12. Tópicos Avançados de Importação (5 Exemplos) ---")

# Exemplo 1: Importações dinâmicas com `importlib.import_module()`
import importlib
nome_modulo = "math"
modulo_math = importlib.import_module(nome_modulo)
print(f"1. Módulo `math` importado dinamicamente. PI = {modulo_math.pi}")

# Exemplo 2: Recarregando um módulo com `importlib.reload()`
# Útil em sessões interativas longas, quando o código do módulo foi alterado.
from importlib import reload
reload(meu_modulo)
print("2. Módulo `meu_modulo` foi recarregado com `importlib.reload()`.")

# Exemplo 3: Controlando o que é importado com `__all__`
# Em um módulo, você pode definir uma lista `__all__` com os nomes
# que devem ser exportados quando se usa `from meu_pacote import *`.
# Se `meu_modulo.py` tivesse `__all__ = ["PI"]`, então `from meu_modulo import *`
# importaria apenas `PI`, e não `saudar` ou `Ferramenta`.
print("3. `__all__` em um módulo controla o que `from modulo import *` importa.")

# Exemplo 4: Pacotes de Namespace (PEP 420)
# Permitem que um pacote seja dividido em múltiplos diretórios.
# Um diretório se torna um pacote de namespace se não contiver um `__init__.py`.
print("4. Pacotes de Namespace (sem `__init__.py`) permitem dividir um pacote em vários locais.")

# Exemplo 5: Importações tardias (Lazy Imports) para otimização
def funcao_que_usa_numpy():
    # A importação só ocorre quando a função é chamada, economizando tempo na inicialização.
    import numpy as np
    print("5. NumPy importado tardiamente.")
    return np.array([1, 2, 3])

print("   A função `funcao_que_usa_numpy` foi definida, mas o numpy ainda não foi importado.")
funcao_que_usa_numpy()
print("-" * 20 + "\n")