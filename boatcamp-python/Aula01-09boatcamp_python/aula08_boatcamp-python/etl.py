import pandas as pd
import os
import glob


#função de extract que le e consolida o json

def extrair_dados_e_consolidar(pasta:str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=False)
    print(df_total)
    return df_total


#função que transforma

def calculo_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


def carregar_dados(df: pd.DataFrame, format_saida: list):
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet", index=False)


def pipeline_calcular_kpi_de_dados_consolidado(pasta_argumento: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta=pasta_argumento)
    data_frame_calculado = calculo_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)


#uma funcção que da load em csv ou parquet

