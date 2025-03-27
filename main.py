import pandas as pd
import numpy as nmp

def limpandodados():
    tabela = pd.read_csv("C:\\Users\\faiel\\OneDrive\\Área de Trabalho\\aulasegunda\\trabalho\\Roubo-a-Transeunte\\bd crimes DF limpo - Página1.csv")
    dataframe = pd.DataFrame(tabela)
    print(dataframe.head())
    print(dataframe.tail())
    return dataframe # retornando o dataframe para ser visivel fora dessa função

dataframe = limpandodados()

def unircolunas():
    dataframe['regiao_ano'] = dataframe['REGIÃO'] + ' - ' + dataframe['ANO'].astype(str)
    somar_regiao_ano = dataframe.groupby('regiao_ano')['ROUBO A TRANSEUNTE'].sum()
    print(somar_regiao_ano)

def chamarfuncoes():
    limpandodados()
    unircolunas()
chamarfuncoes()

