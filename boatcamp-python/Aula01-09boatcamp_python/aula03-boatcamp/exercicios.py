### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

#quantidade = input("Digite sua quantidade")
# valor = input("Digite seu valor")

# if quantidade > "0" and valor > "0":
#     print("Valor e quantidade valídos")
# else:
#     print("Valores e quantidades invalidos")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# temp_escolhida = 30
# if temp_escolhida < 18:
#  print("Temperatura baixa")
# elif 18 <= temp_escolhida <= 26:
#   print("Temperatura normal")
# else:
#   print("Temperatura alta")



### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.


# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
# if log['level'] == 'ERROR':
#     print(log['message'])



### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# idade = int(input("Digite sua idade:"))
# email = input("Digite seu email ")
# if not 18 <= idade <= 65:
#     print("Idade não autorizada")
#     exit()
# elif "@" not in "email":
#     print("Email invalido")
# else:
#     print("Informações invalidas")



### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# transacao = {'valor': 9000, 'horario': 13}
# if transacao ['valor'] > 10000 or transacao ["horario"] < 9 or transacao ["horario"] > 18:
#  print("Transação Suspeita...") 
# else:
#  print("Transação limpa>>>")



### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# frase = ("Hoje esta calor um bom dia, dia bom para curtir uma praia")
# texto = frase.replace(",", "")
# palavras = texto.split()
# print(palavras)
# lista = {}
# for palavra in palavras:
#     if palavra in lista:
#      lista[palavra] = +1
# else: 
#         lista[palavra] = 1




# texto = "minha terceira aula no boatcamp, aula boa"
# palavras = texto.split()
# contagem_palavras = {}

# for palavra in palavras:
#     if palavra in contagem_palavras:
#         contagem_palavras[palavra] += 1
#     else:
#         contagem_palavras[palavra] = 1

# print(contagem_palavras)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# print(normalizados)



### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando7


# usuarios = [
#     {'nome': 'User1', 'email:': 'user1email@gmail.com'},
#     {'nome': 'User2', 'email:' : ""},
#     {'nome': 'User3', 'email:': 'user3email@gmail.com'}
# ]


# usuarios_valid = [user for user in  usuarios if user['email:']]
# print("Usuarios validos:", usuarios_valid)



### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# lista_num = range(1,21)
# pares = [i for i in lista_num if i % 2 ==0]
# print("Sua lista de números pares é:", pares)

# dados = dict()
# dados = {"nome": 'yan'}
# print(dados['nome'])

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.



# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# total_por_categoria = {}
# for venda in vendas:
#     categoria = venda["categoria"]
#     valor = venda["valor"]
#     if categoria in total_por_categoria:
#         total_por_categoria[categoria] += valor
#     else:
#         total_por_categoria[categoria] = valor

# print(total_por_categoria)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# dados = []
# entrada = ""
# while entrada.lower() != "sair":
#     entrada = input("Digite um valor (ou 'sair' para terminar): ")
#     if entrada.lower() != "sair":
#         print("Você quer continuar, continue:")
#     else:
#         print("Sua decisão foi sair...")

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# numero = int(input("Digite algum número entre 1 e 10:"))
# while numero < 1 or numero > 10:
#  print("Número Invalido")
#  numero = int(input("Por favor, digite um número entre 1 e 10: "))
# print("NUmero Valido")



### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.