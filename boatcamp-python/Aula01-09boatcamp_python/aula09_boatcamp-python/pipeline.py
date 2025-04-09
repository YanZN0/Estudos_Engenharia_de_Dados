from etl import pipeline_calcular_kpi_de_dados_consolidado

pasta_argumento: str =  'data'
formato_de_saida: list = ['csv', 'parquet']

pipeline_calcular_kpi_de_dados_consolidado(pasta_argumento, formato_de_saida)