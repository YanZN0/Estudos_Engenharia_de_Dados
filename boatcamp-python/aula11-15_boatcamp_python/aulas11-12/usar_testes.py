from classes_csv import CSVopen



arquivo_csv = "vendas.csv"

csv_past = CSVopen(arquivo_csv)
csv_abrir = csv_past.abrir_csv()
print(csv_abrir)
print(csv_past.filtrar_por(["estado", "preço"], ["SP", "10,50"]))