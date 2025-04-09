
nome_de_usúario = input("Digite seu no0me:")
if nome_de_usúario.isdigit():
    print("Ops, você digitou algo errado")
    exit()
elif len(nome_de_usúario) == 0:
    print("Você se esqueceu de digitar")
    exit()
salario_do_usuario = float(input("Digite seu salario:"))
bonus_usúario = (float(input("Digite o bonús recebido:")))
CONSTANTE_BONUS = 1000
valor_do_bonus = CONSTANTE_BONUS + salario_do_usuario * bonus_usúario
print(f"o usúario {nome_de_usúario} possui um valor total de  {valor_do_bonus}")