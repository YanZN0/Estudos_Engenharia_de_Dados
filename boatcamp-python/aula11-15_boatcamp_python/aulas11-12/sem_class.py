import pandas as pd

def ler_um_csv_com_pandas(csv):
    df = pd.read_csv(csv)
    return df 

pasta = "vendas.csv"
função = ler_um_csv_com_pandas(pasta)
print(função)