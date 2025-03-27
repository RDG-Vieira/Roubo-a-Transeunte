import pandas as pd

def limpandodados():
    tabela = pd.read_csv("C:\\Users\\faiel\\OneDrive\\Área de Trabalho\\aulasegunda\\trabalho\\Roubo-a-Transeunte\\roubo a transeuntes DF.csv")
    dataframe = pd.DataFrame(tabela)
    print(dataframe.head())
    print(dataframe.tail())
    print(dataframe.info())
    print(dataframe.describe())
    return dataframe # retornando o dataframe para ser visível fora dessa função
dataframe = limpandodados()

def unircolunas(dataframe):
    dataframe['REGIÕES POR ANO'] = dataframe["REGIÃO"] + ' - ' + dataframe['ANO'].astype(str)
    somar_regiao_ano = dataframe.groupby('REGIÕES POR ANO')['ROUBO A TRANSEUNTE'].sum().reset_index()
    dataframe = dataframe.merge(somar_regiao_ano, on='REGIÕES POR ANO', how='left')
    dataframe.rename(columns={'ROUBO A TRANSEUNTE_y': 'TOTAL DE ROUBOS'}, inplace=True)
    dataframe.rename(columns={'ROUBO A TRANSEUNTE_x': 'ROUBO A TRANSEUNTES'}, inplace=True)
    return dataframe  # Retorna o DataFrame atualizado
    
def drop_duplicates(dataframe):
   if 'REGIÕES POR ANO' in dataframe.columns and 'TOTAL DE ROUBOS' in dataframe.columns:
        dataframe_sem_duplicadas = dataframe.drop_duplicates(subset=['REGIÕES POR ANO', 'TOTAL DE ROUBOS'], keep='first') # keep garante deixar a primeira ocorrencia de duplicação e excluir o resto
        print("\n DataFrame sem duplicatas: \n")
        print(dataframe_sem_duplicadas)
        return dataframe_sem_duplicadas
   else:
        print("\nErro: As colunas 'REGIÕES POR ANO' ou 'TOTAL DE ROUBOS' não existem no DataFrame.")
        return dataframe

def chamarfuncoes():
    dataframe = limpandodados()
    dataframe = unircolunas(dataframe)
    print(dataframe.columns)
    dataframe_sem_duplicatas = drop_duplicates(dataframe)
    
    # Salvando o DataFrame final sem duplicatas
    dataframe_sem_duplicatas.to_csv("C:\\Users\\faiel\\OneDrive\\Área de Trabalho\\aulasegunda\\trabalho\\Roubo-a-Transeunte\\dataframe_final.csv", index=False)
    print("\nDataFrame final salvo como: dataframe_final.csv")
    print(dataframe.head())
    print(dataframe.tail())
    print(dataframe.info())
    print(dataframe.describe())
chamarfuncoes()

