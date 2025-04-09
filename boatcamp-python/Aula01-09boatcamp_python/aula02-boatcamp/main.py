
try:
 primeiro = (int(input("Diga algum número para fornecermos o seu resultado em quadrado:")))
except:
 print("Ops, algo deu errado")
 exit()
segundo = (primeiro ** 2)
print(f"o número {primeiro} ao quadrado fica {segundo}")
