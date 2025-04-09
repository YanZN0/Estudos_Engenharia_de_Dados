# nome_valido = False
# salario_valido = False
# bonus_valido = False

# # Loop para verificar o nome
# while nome_valido is not True:
#     try:
#         nome_usuario = "Yan"
#         if len(nome_usuario) == 0:
#             raise ValueError("O nome não pode estar vazio.")
#         elif nome_usuario.isdigit():
#             raise ValueError("O nome não deve conter números.")
#         else:
#             print("Nome válido:", nome_usuario)
#             nome_valido = True
#     except ValueError as e:
#         print(e)

# # Loop para verificar o salário
# while salario_valido is not True:
#     try:
#         salario = 3000
#         if salario < 0:
#             print("Por favor, digite um valor positivo para o salário.")
#         else:
#             salario_valido = True
#     except ValueError:
#         print("Entrada inválida para o salário. Por favor, digite um número.")

# # Loop para verificar o bônus
# while bonus_valido is not True:
#     try:
#         bonus = 1.5
#         if bonus < 0:
#             print("Por favor, digite um valor positivo para o bônus.")
#         else:
#             bonus_valido = True
#     except ValueError:
#         print("Entrada inválida para o bônus. Por favor, digite um número.")

# bonus_recebido = 1000 + salario * bonus  # Exemplo simples de cálculo de bônus

# # Imprime as informações para o usuário
# print(f"{nome_usuario}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")
