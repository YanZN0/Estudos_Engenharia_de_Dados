# Inteiros (`int`)

#Escreva um programa que soma dois números inteiros inseridos pelo usuário.

#numero1 = int(input("Me diga um numero:"))
#numero2 = int(input("Me diga outro numero:"))
#print(numero1 + numero2)

#2 Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

#numero_user = int(input("Me diga um número"))
#resultado = int(numero_user / 5)
#print(f"o {numero_user} dividido por 5 resulta em {resultado}")

#3Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

#numero = (int(input("Digite o numero para a multiplicação:")))
#seg_numero= int(input("Digite o segundo numero:"))
#resultado = numero * seg_numero
#print(f"Resultado da multiplicação:", resultado)

#Exercício 4: Divisão Inteira do Primeiro pelo Segundo Número

#try:
 #num1 = int(input("Digite o primeiro número inteiro: "))
 #num2 = int(input("Digite o segundo número inteiro: "))
 #resultado_div_inteira = num1 // num2
 #print("O resultado da divisão inteira é:", resultado_div_inteira)
#except:ZeroDivisionError
#print("Impossivel dividir o zero :/")
#exit()


# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

#try:
 
# primeiro = (int(input("Diga algum número para fornecermos o seu resultado em quadrado:")))
# segundo = (primeiro ** 2)
 #print(f"o número {primeiro} ao quadrado fica {segundo}")
#except:
 # print("Ops, algo deu errado")

# Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.


#try:
 #num1 = float(input("Digite seu número:"))
 #num2 = float(input("Digite seu segundo número"))
 #print(resultado)
#except TypeError:
 #print("Você se esqueceu de digitar um número zézin")
 #exit()


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

#num1 = float(input("Digite o número:"))
#num2 = float(input("Digite o número:"))
#result = (num1+num2) / 2
#print(result)


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

#base = float(input("Digite a base da sua potência:"))
#expoente = float(input("Digite o expoente da sua potência:"))
#result = (base ** expoente) 
#print(f"{result:.2f}")



# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

#celsius = float(input("Digite a temperatura desejada para ser convertida a celsius:"))
#result = float(celsius * 9/5) + 32
#print(result)


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

#raio = float(input("Digite o raio do círculo: "))
#area = 3.14159 * raio ** 2
#print("A área do círculo é:",f"{area:.2f}")

# Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

#nome = input("Digite seu nome, ele ficará em maiúsculo:")
#result = nome.upper()
#print(result)


# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

#nome = str(input("Digite seu nome completo, ele ficará em minúsculo:"))
#result = nome.lower()
#print(result)


# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

#frase_escolhida = input("Digite uma frase: ")
#frase_sem_espacos = frase_escolhida.strip()
#print("Frase sem espaços no início e no final:", frase_sem_espacos)


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

#data = str(input("Diga sua data de nascimento:"))
#data.isdigit():
#result = data.split("/")
#print(result)


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.


# palavra1 = str(input("Digite sua primeira palavra:"))
# palavra2 = str(input("Digite a segunda palavra:"))
# result= palavra1 + palavra2
# print(result)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# expressao_1 = True
# expressao_2 = False
# resultado = expressao_1 and expressao_2
# print(f"Expressão 1: {expressao_1}")
# print(f"Expressão 2: {expressao_2}")
# print(f"AND: {resultado}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# expressao_1 = input("Digite True ou False")
# expressao_2 = input("Digite True ou False")
# resultado = expressao_1 or expressao_2
# print(f"Expressão 1: {expressao_1}")
# print(f"Expressão 2: {expressao_2}")
# print(f"OR: {resultado}")


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# entrada = (input("Digite sua resposta Sendo True Ou False:"))
# if entrada == "True":
#  valor1 = True
# elif entrada == "False":
#  valor1 = False
# else:
#  print("Digite True ou False!!")
#  valor1 = None
#  exit()
# result = not valor1
# rint(f"Você digitou: {entrada}")
# print(f"Reesposta invertida: {result}")


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# valor1 = int(input("Digite o número:"))
# valor2 = int(input("Digite o segundo número:"))
# result_igual = (valor1 == valor2)
# print("resultado da diferença:", result_igual)


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# valor1 = int(input("Digite o número:"))
# valor2 = int(input("Digite o segundo número:"))
# result_different = (valor1 != valor2)
# print("resultado da diferença:", result_different)


# try-except e if

# 21: Conversor de Temperatura

# try:
#  celsius = float(input("Digite a temperatura:"))
#  resultado = (celsius * 9/5) + 32
#  print("Convertida a Fahrenheit:", resultado)
# except ValueError:
#  print("Parece que não digitou algum número, digite...")
#  exit()

# # 22: Verificador de Palíndromo

# entrada = input("Digite uma palavra ou frase: ")
# if isinstance(entrada, str):
#     formatado = entrada.replace(" ", "").lower()
#     if formatado == formatado[::-1]:
#         print("É um palíndromo.")
#     else:
#         print("Não é um palíndromo.")
# else:
#     print("Entrada inválida. Por favor, digite uma palavra ou frase.")

#Exercício 23: Calculadora Simples

# try:
#  num1 = float(input("Digite o primeiro número:"))
#  num2 = float(input("Digite o segundo número:"))
#  operador = input("Escolha o operador (+, -, *,/):")
#  if operador == "+":
#   resultado = num1 + num2
#  elif operador == "-":
#   resultado = num1 - num2
#  elif operador == "*":
#   resultado = num1 * num2
#  elif  operador == "/":
#   resultado = num1 // num2
#  else:
#   print("Digite uma conta de números validá!!")
#  print("O resultado da conta desejada é:", resultado)
# except ValueError:
#  print("Digite números, sem letras...")
# except KeyboardInterrupt:
#  print("Parece que você interrompeu a conta :((...))")
 




# # 24: Classificador de Números

# try:
#   num1 = int(input("Digite um número:"))
#   if num1 < 0:
#    print("negativo")
#   elif num1 > 0:
#    print("positivo")
#   else:
#    print("Zer0")
#   if num1 % 2 == 0:
#     print("Par")
#   else:
#    ("impar")
# except ValueError:
#  print("Digite um número...")

# try:
#     numero = int(input("Digite um número: "))
#     if numero > 0:
#         print("Positivo")
#     elif numero < 0:
#         print("Negativo")
#     else:
#         print("Zero")
#     if numero % 2 == 0:
#         print("Par")
#     else:
#         print("Ímpar")
# except ValueError:
#     print("Por favor, digite um número inteiro válido.")

# # 25: Conversão de Tipo com Validação

# entrada_lista = input("Digite uma lista de números separados por vírgula: ")
# numeros_str = entrada_lista.split(",")
# numeros_int = []
# try:
#     for num in numeros_str:
#         numeros_int.append(int(num.strip()))
#     print("Lista de inteiros:", numeros_int)
# except ValueError:
#     print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")
