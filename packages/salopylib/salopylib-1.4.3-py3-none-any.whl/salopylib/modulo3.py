import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ajusteEpanechnikov:
    '''
    Clase que realiza el ajuste de datos de fecha vs cantidad a una curva suave por medio de un kernel 
    de Epanechnikov y hace su respectiva graficación, a partir de los siguientes datos:
    
    path: direccción en que se encuentra el archivo csv que contiene los datos. 
    h: factor que determina la "suavidad" de la curva y la exactitud del ajuste. Entre menor sea su valor
        más suave será la curva de ajuste pero más se alejará de los datos ingresados y vicecversa.

    La columnas del csv a usar deben tener el nombre literal: fecha_actualizacion y nuevos_casos
    '''

    def __init__(self,path:str,h:float):
        self.p = path
        self.h = h
    
    def datos(self):
        df = pd.read_csv(self.p)
        return df
    
    def ajusteEpa(self):
        suavizado = []
        df = self.datos()
        df['fecha_actualizacion'] = pd.to_datetime(df['fecha_actualizacion'])

        for f in sorted(df['fecha_actualizacion']):
            dx = abs(((df['fecha_actualizacion'] - f).apply(lambda x: x.days)) /self.h)
            dxx = dx[dx<=1]
            df['suave'] = (3/4)* (1-dx** 2 )
            df['suave'] = df['suave']*dxx
            df['suave'] /= df['suave'].sum()
            suavizado.append(round(df['nuevos_casos'] * df['suave']).sum())
        df['suavizado'] = suavizado
        return df

    def plotE(self):
        df = self.ajusteEpa()
        plt.figure(figsize=(10, 6))
        plt.title('Casos de covid-19 en Colombia')
        plt.xlabel('Fechas [aaaamm]')
        plt.ylabel('Número de casos')
        plt.plot(df['fecha_actualizacion'], df['nuevos_casos'], label='Curva original')
        plt.plot(df['fecha_actualizacion'], df['suavizado'], label='Curva suavizada con kernel Epanechnikov')
        plt.legend()
        plt.savefig("AjusteEpanechnikov.png")
        plt.show()

    
