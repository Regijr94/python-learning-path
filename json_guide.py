# -*- coding: utf-8 -*-

"""
Guia Completo sobre JSON em Python: Do Básico ao Avançado

Este arquivo é um guia de estudo completo sobre o módulo `json` em Python,
essencial para trabalhar com dados no formato JSON (JavaScript Object Notation).

--------------------------------------------------------------------------------------
Conteúdo:
1.  O que é JSON?
2.  Serialização: Convertendo Python para JSON (`json.dumps`)
3.  Desserialização: Convertendo JSON para Python (`json.loads`)
4.  Trabalhando com Arquivos (`json.dump` e `json.load`)
5.  Tópicos Avançados e Casos de Uso
--------------------------------------------------------------------------------------
"""

import json
from datetime import datetime
from decimal import Decimal

# 1. O que é JSON?
# -----------------
# JSON (JavaScript Object Notation) é um formato leve de troca de dados, fácil para
# humanos lerem e escreverem, e fácil para máquinas interpretarem e gerarem.
#
# Mapeamento de Tipos Python -> JSON:
# dict          -> object
# list, tuple   -> array
# str           -> string
# int, float    -> number
# True          -> true
# False         -> false
# None          -> null

print("--- 1. O que é JSON? (10 Exemplos de strings JSON) ---")

json_string_1 = '{"nome": "Carlos", "idade": 30}'
json_string_2 = '["maçã", "banana", "cereja"]'
json_string_3 = '{"id": 1, "ativo": true, "saldo": null}'
json_string_4 = '{"temperaturas": [22.5, 23.1, 21.9]}'
json_string_5 = '{"produto": "Livro", "tags": ["leitura", "ficção"]}'
json_string_6 = '{"ponto": {"x": 10, "y": 20}}' # Objeto aninhado
json_string_7 = '[{"id": 1}, {"id": 2}, {"id": 3}]' # Array de objetos
json_string_8 = '"Uma string simples"' # String JSON válida
json_string_9 = '12345' # Número JSON válido
json_string_10 = 'true' # Booleano JSON válido

print("1. Objeto simples:", json_string_1)
print("2. Array simples:", json_string_2)
print("3. Misto (número, booleano, nulo):", json_string_3)
print("4. Array de números:", json_string_4)
print("5. Objeto com array:", json_string_5)
print("6. Objeto aninhado:", json_string_6)
print("7. Array de objetos:", json_string_7)
print("8. String:", json_string_8)
print("9. Número:", json_string_9)
print("10. Booleano:", json_string_10)
print("-" * 20 + "\n")


# 2. Serialização: Convertendo Python para JSON (`json.dumps`)
# -------------------------------------------------------------
# `dumps` significa "dump string" (despejar para string).
# Converte um objeto Python em uma string no formato JSON.

print("--- 2. Serialização com `json.dumps` (10 Exemplos) ---")

dados_python = {
    "id": 87,
    "nome": "Ana",
    "cidade": "São Paulo",
    "cursos": ["Python", "Ciência de Dados"],
    "ativa": True,
    "saldo": None
}

# Exemplo 1: Serialização básica
json_basico = json.dumps(dados_python)
print(f"1. Básico: {json_basico}")

# Exemplo 2: Pretty-printing com `indent`
json_indentado = json.dumps(dados_python, indent=4)
print(f"2. Com indentação:\n{json_indentado}")

# Exemplo 3: Ordenando as chaves com `sort_keys`
json_ordenado = json.dumps(dados_python, indent=4, sort_keys=True)
print(f"3. Com chaves ordenadas:\n{json_ordenado}")

# Exemplo 4: Serialização compacta com `separators`
json_compacto = json.dumps(dados_python, separators=(',', ':'))
print(f"4. Compacto: {json_compacto}")

# Exemplo 5: Lidando com caracteres não-ASCII (acentos)
dados_acento = {"cidade": "São Paulo", "país": "Brasil"}
json_ascii = json.dumps(dados_acento) # Padrão: ensure_ascii=True
json_utf8 = json.dumps(dados_acento, ensure_ascii=False)
print(f"5. Com acentos (ASCII): {json_ascii}")
print(f"   Com acentos (UTF-8): {json_utf8}")

# Exemplo 6: Ignorando chaves não-serializáveis com `skipkeys`
dados_chave_invalida = {(1, 2): "tupla como chave"} # Tupla não é chave JSON válida
try:
    json.dumps(dados_chave_invalida)
except TypeError as e:
    print(f"6. Erro sem skipkeys: {e}")
json_skipkeys = json.dumps(dados_chave_invalida, skipkeys=True)
print(f"   Com skipkeys=True: {json_skipkeys}")

# Exemplo 7: Lidando com tipos não-padrão usando `default`
dados_com_data = {"nome": "Evento", "data": datetime(2023, 10, 26, 10, 30)}
def formatador_default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Objeto do tipo {type(obj).__name__} não é serializável em JSON")

json_com_data = json.dumps(dados_com_data, default=formatador_default)
print(f"7. Serializando datetime com `default`: {json_com_data}")

# Exemplo 8: Serializando um objeto de classe customizada
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

usuario_obj = Usuario("Beto", "beto@email.com")
def usuario_para_dict(obj):
    if isinstance(obj, Usuario):
        return {'nome': obj.nome, 'email': obj.email, '_tipo': 'Usuario'}
    raise TypeError("Tipo não serializável")

json_usuario = json.dumps(usuario_obj, default=usuario_para_dict)
print(f"8. Serializando objeto de classe: {json_usuario}")

# Exemplo 9: Usando uma subclasse de `JSONEncoder`
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj) # Converte Decimal para float
        return super().default(obj)

dados_decimal = {"preco": Decimal("99.90")}
json_decimal = json.dumps(dados_decimal, cls=CustomEncoder)
print(f"9. Usando JSONEncoder customizado: {json_decimal}")

# Exemplo 10: Lidando com valores `NaN`, `Infinity`
dados_float_especial = {"valor": float('inf'), "nao_numero": float('nan')}
# Por padrão, `allow_nan=True`. Em JSON estrito, isso é inválido.
try:
    json.dumps(dados_float_especial, allow_nan=False)
except ValueError as e:
    print(f"10. Erro com allow_nan=False: {e}")
print(f"    Com allow_nan=True (padrão): {json.dumps(dados_float_especial)}")
print("-" * 20 + "\n")


# 3. Desserialização: Convertendo JSON para Python (`json.loads`)
# ----------------------------------------------------------------
# `loads` significa "load string" (carregar de string).
# Converte uma string JSON em um objeto Python.

print("--- 3. Desserialização com `json.loads` (10 Exemplos) ---")

# Exemplo 1: Desserialização básica
json_str = '{"nome": "Carla", "idade": 28, "cidade": "Recife"}'
dados_py = json.loads(json_str)
print(f"1. Básico: {dados_py}, tipo: {type(dados_py)}")

# Exemplo 2: Desserialização de um array JSON
json_array_str = '[10, 20, 30, 40]'
lista_py = json.loads(json_array_str)
print(f"2. Array JSON para lista Python: {lista_py}, tipo: {type(lista_py)}")

# Exemplo 3: Reconstruindo um objeto customizado com `object_hook`
json_usuario_str = '{"nome": "Beto", "email": "beto@email.com", "_tipo": "Usuario"}'
def dict_para_usuario(d):
    if d.get('_tipo') == 'Usuario':
        return Usuario(d['nome'], d['email'])
    return d

usuario_reconstruido = json.loads(json_usuario_str, object_hook=dict_para_usuario)
print(f"3. Reconstruindo objeto com `object_hook`: {usuario_reconstruido}, tipo: {type(usuario_reconstruido)}")

# Exemplo 4: Usando `parse_float` para carregar números como `Decimal`
json_preco_str = '{"preco": 99.90, "desconto": 10.5}'
dados_decimal_obj = json.loads(json_preco_str, parse_float=Decimal)
print(f"4. Usando `parse_float=Decimal`: {dados_decimal_obj['preco']}, tipo: {type(dados_decimal_obj['preco'])}")

# Exemplo 5: Usando `parse_int`
json_id_str = '{"id": 12345678901234567890}'
dados_id = json.loads(json_id_str, parse_int=str) # Carrega inteiro como string
print(f"5. Usando `parse_int=str`: {dados_id['id']}, tipo: {type(dados_id['id'])}")

# Exemplo 6: Usando `object_pairs_hook` para lidar com chaves duplicadas
from collections import OrderedDict
json_duplicado_str = '{"nome": "A", "nome": "B"}' # JSON inválido, mas alguns parsers aceitam
def hook_pares(pares):
    d = OrderedDict()
    for chave, valor in pares:
        if chave in d:
            print(f"Aviso: Chave duplicada '{chave}' encontrada.")
        d[chave] = valor
    return d
dados_pares = json.loads(json_duplicado_str, object_pairs_hook=hook_pares)
print(f"6. Usando `object_pairs_hook`: {dados_pares}")

# Exemplo 7: Lidando com erro de decodificação (`JSONDecodeError`)
json_invalido_str = '{"nome": "Ana", "idade": 30,}' # Vírgula extra no final
try:
    json.loads(json_invalido_str)
except json.JSONDecodeError as e:
    print(f"7. Erro de decodificação capturado: {e}")

# Exemplo 8: Desserializando JSON com caracteres especiais
json_utf8_str = '{"cidade": "São Paulo", "país": "Brasil"}'
dados_utf8 = json.loads(json_utf8_str)
print(f"8. Desserializando UTF-8: {dados_utf8}")

# Exemplo 9: Usando `parse_constant` para constantes customizadas
json_const_str = '{"valor": Infinity, "outro": -Infinity, "vazio": NaN}'
def parse_const_custom(const_str):
    if const_str == 'Infinity': return float('inf')
    if const_str == '-Infinity': return float('-inf')
    if const_str == 'NaN': return float('nan')
    raise ValueError(f"Constante desconhecida: {const_str}")
# Nota: `loads` já faz isso por padrão, mas aqui mostramos como customizar.
dados_const = json.loads(json_const_str, parse_constant=parse_const_custom)
print(f"9. Usando `parse_constant`: {dados_const}")

# Exemplo 10: Usando uma subclasse de `JSONDecoder`
class CustomDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        # Passa o nosso hook para a classe pai
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, d):
        if d.get('_tipo') == 'Usuario':
            return Usuario(d['nome'], d['email'])
        return d

usuario_decoder = json.loads(json_usuario_str, cls=CustomDecoder)
print(f"10. Usando JSONDecoder customizado: {usuario_decoder}, tipo: {type(usuario_decoder)}")
print("-" * 20 + "\n")


# 4. Trabalhando com Arquivos (`json.dump` e `json.load`)
# ---------------------------------------------------------
# `dump`: Escreve um objeto Python em um arquivo no formato JSON.
# `load`: Lê um arquivo JSON e o converte para um objeto Python.

print("--- 4. Trabalhando com Arquivos (10 Exemplos) ---")

arquivo_teste = "dados.json"
dados_para_arquivo = {"id": 101, "produto": "Notebook", "tags": ["tech", "office"]}

# Exemplo 1: Escrevendo em um arquivo com `json.dump`
with open(arquivo_teste, 'w', encoding='utf-8') as f:
    json.dump(dados_para_arquivo, f)
print(f"1. Dados escritos em '{arquivo_teste}'.")

# Exemplo 2: Lendo de um arquivo com `json.load`
with open(arquivo_teste, 'r', encoding='utf-8') as f:
    dados_lidos = json.load(f)
print(f"2. Dados lidos de '{arquivo_teste}': {dados_lidos}")

# Exemplo 3: Escrevendo com indentação para melhor legibilidade
with open(arquivo_teste, 'w', encoding='utf-8') as f:
    json.dump(dados_para_arquivo, f, indent=4, ensure_ascii=False)
print("3. Arquivo reescrito com indentação.")

# Exemplo 4: Lendo e atualizando um arquivo JSON
with open(arquivo_teste, 'r', encoding='utf-8') as f:
    dados_atuais = json.load(f)
dados_atuais['em_estoque'] = True # Adiciona nova informação
with open(arquivo_teste, 'w', encoding='utf-8') as f:
    json.dump(dados_atuais, f, indent=4)
print("4. Arquivo lido, atualizado e reescrito.")

# Exemplo 5: Tratando `FileNotFoundError` ao tentar ler
try:
    with open("arquivo_inexistente.json", 'r') as f:
        json.load(f)
except FileNotFoundError:
    print("5. Tratado: O arquivo 'arquivo_inexistente.json' não foi encontrado.")

# Exemplo 6: Escrevendo dados com acentos em um arquivo
dados_br = {"cidade": "Brasília", "população": 3094325}
with open("dados_br.json", 'w', encoding='utf-8') as f:
    json.dump(dados_br, f, indent=4, ensure_ascii=False)
print("6. Dados com acentos escritos em 'dados_br.json'.")

# Exemplo 7: Lendo dados com acentos de um arquivo
with open("dados_br.json", 'r', encoding='utf-8') as f:
    dados_lidos_br = json.load(f)
print(f"7. Lendo dados com acentos: {dados_lidos_br}")

# Exemplo 8: Usando `dump` com um `default` handler
dados_complexos = {"evento": "Live de Python", "data": datetime.now()}
with open("evento.json", 'w') as f:
    json.dump(dados_complexos, f, default=formatador_default, indent=4)
print("8. Arquivo 'evento.json' escrito com `default` handler.")

# Exemplo 9: Usando `load` com `object_hook`
with open("usuario.json", 'w') as f:
    json.dump(usuario_obj, f, default=usuario_para_dict)
with open("usuario.json", 'r') as f:
    usuario_lido_arquivo = json.load(f, object_hook=dict_para_usuario)
print(f"9. Lendo e reconstruindo objeto de arquivo: {usuario_lido_arquivo}")

# Exemplo 10: Tratando arquivo JSON mal formatado
with open("corrompido.json", 'w') as f:
    f.write('{"chave": "valor"') # JSON incompleto
try:
    with open("corrompido.json", 'r') as f:
        json.load(f)
except json.JSONDecodeError as e:
    print(f"10. Tratado: Erro ao ler arquivo corrompido: {e}")

# Limpeza dos arquivos criados
import os
for file in ["dados.json", "dados_br.json", "evento.json", "usuario.json", "corrompido.json"]:
    if os.path.exists(file):
        os.remove(file)
print("-" * 20 + "\n")


# 5. Tópicos Avançados e Casos de Uso
# ------------------------------------
print("--- 5. Tópicos Avançados (10 Exemplos) ---")

# Exemplo 1: `JSONEncoder` para serializar um conjunto (set)
class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj) # Converte set para list
        return super().default(obj)

dados_set = {"tags": {"python", "json", "guia"}}
json_set = json.dumps(dados_set, cls=SetEncoder)
print(f"1. Serializando um set: {json_set}")

# Exemplo 2: `object_hook` para desserializar datas no formato ISO
json_data_str = '{"evento": "Aniversário", "data": "2024-01-15T12:00:00"}'
def hook_data(d):
    if 'data' in d:
        d['data'] = datetime.fromisoformat(d['data'])
    return d
evento_obj = json.loads(json_data_str, object_hook=hook_data)
print(f"2. Desserializando data ISO: {evento_obj['data']}, tipo: {type(evento_obj['data'])}")

# Exemplo 3: Usando `json.tool` da linha de comando para validar e formatar
# No terminal, você pode executar: echo '{"b":1,"a":2}' | python -m json.tool
# A saída será o JSON formatado e com chaves ordenadas.
print("3. Use `python -m json.tool` no terminal para formatar JSON.")

# Exemplo 4: Serializando para um stream em memória (io.StringIO)
import io
stream_memoria = io.StringIO()
json.dump({"status": "ok"}, stream_memoria)
conteudo_stream = stream_memoria.getvalue()
print(f"4. JSON em stream de memória: {conteudo_stream.strip()}")

# Exemplo 5: Combinando `default` e `object_hook` para um ciclo completo
class Ponto:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"Ponto(x={self.x}, y={self.y})"

def encoder_ponto(obj):
    if isinstance(obj, Ponto):
        return {'_tipo': 'Ponto', 'x': obj.x, 'y': obj.y}
    raise TypeError("Não serializável")

def decoder_ponto(d):
    if d.get('_tipo') == 'Ponto':
        return Ponto(d['x'], d['y'])
    return d

ponto_original = Ponto(10, -5)
ponto_json = json.dumps(ponto_original, default=encoder_ponto)
ponto_reconstruido = json.loads(ponto_json, object_hook=decoder_ponto)
print(f"5. Ciclo completo (objeto -> json -> objeto): {ponto_reconstruido}")

# Exemplo 6: Diferença de performance com bibliotecas alternativas (conceitual)
# Bibliotecas como `ujson` e `orjson` são muito mais rápidas.
# Instalação: pip install ujson orjson
# Uso: import ujson; ujson.dumps(obj)
print("6. Bibliotecas como `ujson` e `orjson` oferecem maior performance.")

# Exemplo 7: Lidando com JSON aninhado de forma complexa
json_complexo = """
{
  "id": "001",
  "data": {
    "items": [
      {"id": "i01", "value": 10},
      {"id": "i02", "value": 20}
    ]
  }
}
"""
dados_complexos_py = json.loads(json_complexo)
soma_valores = sum(item['value'] for item in dados_complexos_py['data']['items'])
print(f"7. Processando JSON aninhado: a soma dos valores é {soma_valores}.")

# Exemplo 8: Criando um JSONL (JSON Lines)
# Cada linha é um objeto JSON válido.
dados_log = [
    {"timestamp": "2023-10-26T10:00:00", "level": "INFO", "message": "Serviço iniciado"},
    {"timestamp": "2023-10-26T10:00:05", "level": "ERROR", "message": "Falha na conexão"}
]
with open("logs.jsonl", "w") as f:
    for entrada in dados_log:
        f.write(json.dumps(entrada) + '\n')
print("8. Arquivo 'logs.jsonl' (JSON Lines) criado.")
os.remove("logs.jsonl") # Limpeza

# Exemplo 9: `JSONDecoder` para decodificar múltiplos objetos de um stream
json_stream = '[1, 2, 3] {"a": 1}'
decoder = json.JSONDecoder()
pos = 0
while pos < len(json_stream):
    obj, lido = decoder.raw_decode(json_stream[pos:])
    print(f"9. Objeto decodificado de stream: {obj}")
    pos += lido
    # Ignora espaços em branco entre os objetos
    while pos < len(json_stream) and json_stream[pos].isspace():
        pos += 1

# Exemplo 10: Serialização de dados binários (bytes)
# Bytes não são serializáveis diretamente. A abordagem comum é codificar em Base64.
import base64
dados_binarios = b'\x00\xDE\xAD\xBE\xEF\xFF'

class BytesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return base64.b64encode(obj).decode('ascii')
        return super().default(obj)

json_bytes = json.dumps({'dados': dados_binarios}, cls=BytesEncoder)
print(f"10. Serializando bytes com Base64: {json_bytes}")

dados_decodificados = json.loads(json_bytes)
bytes_reconstruidos = base64.b64decode(dados_decodificados['dados'])
print(f"    Bytes reconstruídos: {bytes_reconstruidos == dados_binarios}")

print("-" * 20 + "\n")