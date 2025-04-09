import csv
from typing import List, Dict


def ler_csv(nome_arquivo_csv: str ) -> list[dict]:
    """Ler um csv"""
    lista = []
    with open(nome_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
     reader = csv.DictReader(arquivo)
     for linha in reader:
        lista.append(linha)
    return lista

def processar_dados(dados: List[Dict[str,int]]) -> Dict[str, List[Dict[str,str]]]:
   categorias = {}
   for item in dados:
      categoria = item["Categoria"]
      if categoria not in categorias:
         categorias[categoria] = []
      categorias[categoria].append(item)

   return categorias

def calcular_vendas_categoria(dados: Dict[str, List[Dict[str, str]]]) -> Dict[str, int]:
    vendas_por_categoria = {}
    for categoria, itens in dados.items():
        total_de_vendas = sum(int(item['quantidade']) * int(item['Venda']) for item in itens)
        vendas_por_categoria[categoria] = total_de_vendas
    return vendas_por_categoria


