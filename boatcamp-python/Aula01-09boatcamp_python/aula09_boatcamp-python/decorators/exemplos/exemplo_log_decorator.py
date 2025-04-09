from utils_log import log_decorator



@log_decorator
def soma(valor1, valor2):
    return valor1 + valor2
    
soma(3,5)
soma(100,100)