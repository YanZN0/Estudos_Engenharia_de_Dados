#1. Lista de números ao quadrado

# numeros = list(range(1,11))
# for numero in numeros:
#     print(numero**2)

#2.Modificar lista de linguagen

# linguagens = ["Python", "Java", "C", "JavaScript"]
# linguagens.remove("C")
# linguagens.append("Ruby")
# print(linguagens)


#3. Informações de um livro

# from typing import Dict, Any

# produto: Dict[str, Any] = {
#     "nome": "sutil arte de ligar o fds",
#     "autor": "Mark Manson",
#     "data_lanç": 2017

# }

# produto2: Dict[str, Any] = {
#     "nome": "Game of Thrones",
#     "autor": "Estagiario",
#     "data_lanç": 2007

# }

# list_livros = []
# list_livros.append(produto)
# list_livros.append(produto2)

# print(list_livros)

# list_the_book: dict = {
#     "produto": {"nome": "sutil arte de ligar o fds",
#     "autor": "Mark Manson",
#     "data_lanç": 2017},

#     "produto2": {"nome": "Game of Thrones",
#     "autor": "Estagiario",
#     "data_lanç": 2007}
# }


#4. Contar ocorrências de caracteres

# def contar_caracteres(s):
#     contagem = {}
#     for caractere in s:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem

# print(contar_caracteres("engenharia de dados"))

#5. Preço total da lista de compras

# lista_prod = ["Maçã", "Pera", "Abacaxi"]
# preços = {"Maçã": 2 , "Pera": 3 , "Abacaxi": 4}
# result =sum(preços[item] for item in lista_prod)
# print(f"Um total de: {result} reais")

#6. Eliminação de Duplicatas

# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# emails_unicos = list(set(emails))

# print(emails_unicos)


#7. Filtragem de Dados


# idades = ["22", "18", "15", "17", "25", "16"]
# idade_validas = [int(idade) for idade in idades if int(idade) >= 18]
# print(idade_validas)

#8. Ordenação Personalizada
#Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.


# pessoas = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Carol", "idade": 20}
# ]
# pessoas.sort(key=lambda pessoa: pessoa["nome"])

# print(pessoas)

#9.

# numeros = [50, 20, 30, 40, 50]
# média = sum(numeros) / len(numeros)
# print("Media", média)

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

# valores = range(1,20)
# par = [numero for numero in valores if numero % 2 ==0]
# impar = [numero for numero in valores if numero % 2 != 0]

# print(f"Pares: {par}")
# print(f"Impares: {impar}")

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.


# produtos = [
#     {"id": 1, "nome": "tenis", "preço": 100},
#     {"id": 2, "nome": "camisa", "preço": 50},
#     {"id": 3, "nome": "bola", "preço": 120}
# ]

# for produto in produtos:
#     if produto["id"] ==3:
#      produto["preço"] = 90
     
# print(produtos)


# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}
# fusão = {**dicionario1, **dicionario2}
# print(fusão)


#13. Filtragem de Dados em Dicionário
#Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.


# estoque = {"Bola Hand": 0, "Bola Basquete": 10, "Bola Futsal": 12}

# estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}
# print(estoque_positivo)


# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.


# dicionario = {"a": 1, "b": 2, "c": 3}
# chaves  = list(dicionario.keys())
# valores = list(dicionario.values())
# print("Chaves:", chaves)
# print("Valores:", valores)


# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

# frase = "engenharia de dados é dificil"
# lista = {}
# for caractere in frase:
#  if caractere in lista:
#     lista[caractere] += 1
#  else:
#    lista[caractere] = 1
# print(lista)
