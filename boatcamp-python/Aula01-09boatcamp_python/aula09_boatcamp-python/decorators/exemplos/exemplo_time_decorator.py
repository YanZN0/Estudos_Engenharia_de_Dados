from time_decorator import time_measure_decorator
import time

@time_measure_decorator
def soma(valor1, valor2):
    time.sleep(3)
    return valor1 + valor2
    
soma(3,5)
soma(100,100)