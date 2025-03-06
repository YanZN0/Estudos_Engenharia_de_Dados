import pandas as pd 



class CSVopen:
    def __init__(self, pasta_csv):
        self.pasta_csv = pasta_csv
        self.df = None
        self.df_filtrado = None


    def abrir_csv(self):
            self.df = pd.read_csv(self.pasta_csv)
            return self.df
    

    def filtrar_por(self, colunas, atributos):
         if len(colunas) != len(atributos):
            raise ValueError("Não tem o mesmo número de colunas e atributos...")
         
         if len(colunas) == 0:
              return self.df
         
         coluna_atual = colunas[0]
         atributo_atual = atributos[0]

         df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

         if len(colunas) == 1:
           return df_filtrado
         else:
           return self.filtrar_por(colunas[1:], atributos[1:])
         



