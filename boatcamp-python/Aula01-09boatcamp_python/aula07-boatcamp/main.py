#1.Calcular Média de Valores em uma Lista


# from typing import List

# def calcular_média (valores = List[float]) -> float:
#     """Calcula a média dos números inseridos, 
#     e da o resultado através de uma lista
#     """
#     resultado = sum(valores) / len(valores)
#     return resultado


#2.Filtrar Dados Acima de um Limite

# from typing import List

# def filtração(dados = List[float], limite = 1000) -> List[float]:

#     """
#     Só adiciona dados em um lista, caso esse número
#     seja maior que o limite    
#     """
#     resultado = []
#     for valor in dados:
#         if valor > limite:
#             resultado.append(valor)
#     return resultado

# valores = 1000, 2000, 3000, 50, 100, 40
# dados_acima_do_limite = filtração(valores)
# print(f"Resultado: {dados_acima_do_limite}")
        
#3.Contar Valores Únicos em uma Lista

# from typing import List

# def valores_unicos(valor_unico = list[int]) -> int:
#     return len(set(valor_unico))


#4.Converter Celsius para Fahrenheit em uma Lista

# from typing import List

# def conversão_de_temperatura(conversão = list[float]) -> list[float]:
#     """Converte Celsius em Fahrenheit
#     e retorna o resultado em uma lista
#     """
#     resultado = []
#     for celsius in conversão:
#         Fahrenheit = (celsius * 9/5) + 32
#         resultado.append(Fahrenheit)
#     return resultado

# temperaturas = [34.2]
# temperatura_convertida = conversão_de_temperatura(temperaturas)
# print(temperatura_convertida)

#5.Calcular Desvio Padrão de uma Lista

# from typing import List

# def calcular_desvio_padrao(valores: List[float]) -> float:
#     """Calcular o desvio padrão da média"""
#     media = sum(valores) / len(valores)
#     variancia = sum((x - media) ** 2 for x in valores) / len(valores)
#     return variancia ** 0.5

# valores = [1, 2, 3, 4, 5]
# desvio_padrao = calcular_desvio_padrao(valores)
# print(f"O desvio padrão é: {desvio_padrao })





#6.Encontrar Valores Ausentes em uma Sequência

# from typing import List

# sequencia = [1, 2, 3, 5, 6, 8, 10]

# def encontrar_valores_ausentes(valores = List[int]) -> List[int]:
#     """Descobre números que faltam em uma sequencia
#     na lista"""
#     for numero_ausente in valores:
#      completo = set(range(min(sequencia), max(sequencia) +1))
#      return list(completo - set(sequencia))

# numeros_ausentes = encontrar_valores_ausentes(sequencia)
# print("Lista Completa:", numeros_ausentes)

