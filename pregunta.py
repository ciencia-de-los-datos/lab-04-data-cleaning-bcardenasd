"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df=df.copy()                                       
    df.dropna(inplace=True)                            
    df = df.apply(lambda x: x.str.lower().replace({'-': ' ', '_': ' '}, regex=True) if x.dtype == "object" else x)
    df = df.apply(lambda x: x.replace('[!\"#$%&\'()*+,:;<=>?¿@[\\]^`{|}~]', '', regex=True) if x.dtype == "object" else x)      
    
    df['monto_del_credito'] = df['monto_del_credito'].astype(float)         
    df['estrato'] = df['estrato'].astype(int)                               
    df['comuna_ciudadano'] = df['comuna_ciudadano'].replace(r'\.0$', '', regex=True).astype(int)    
    df.fecha_de_beneficio=pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True, format='mixed')   
    
    df.drop_duplicates(inplace=True)

    return df
