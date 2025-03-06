from typing import List, Dict
import csv

class CSVProcessor:
    def __init__(self, arquivo_do_csv):
        self.arquivo_do_csv = arquivo_do_csv
        self.dict = []


    def ler_csv(self, lista) -> list[dict]:
        lista = self.dict
        with open(self.arquivo_do_csv, mode="r", encoding="UTF-8") as arquivo:
            self.dict = csv.DictReader(arquivo)
            for linha in self.dict:
                lista.append(linha)
            return lista

arquivo_csv = "vendas.csv"
iniciar = CSVProcessor(arquivo_csv)
abrir = iniciar.ler_csv(iniciar)      
print(abrir)

