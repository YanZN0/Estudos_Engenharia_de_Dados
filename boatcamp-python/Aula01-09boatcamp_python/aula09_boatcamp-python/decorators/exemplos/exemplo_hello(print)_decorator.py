from hello_decorator import hello


@hello
def soma(valor1, valor2):
    return valor1 + valor2
    
soma(3,5)
soma(100,100)