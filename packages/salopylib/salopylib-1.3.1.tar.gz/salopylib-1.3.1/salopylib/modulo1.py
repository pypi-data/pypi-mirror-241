import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ajusteKernel:
    '''
    Clase que realiza el ajuste de datos de fecha vs cantidad a una curva suave por medio de un kernel 
    gaussiano, tricube o de Epanechnikov y hace su respectiva graficación, a partir de los siguientes datos:
    
    path: direccción en que se encuentra el archivo csv que contiene los datos. 
    h: factor que determina la "suavidad" de la curva y la exactitud del ajuste. Entre menor sea su valor
        más suave será la curva de ajuste pero más se alejará de los datos ingresados y vicecversa.
    tipo: tipo de kernel a usar, puede ser Gaussiano, Tricube o Epanechnikov. Debe ingresarse de forma literal
        como string
    La columnas del csv a usar deben tener el nombre literal: fecha_actualizacion y nuevos_casos
    '''

    def __init__(self,path:str,h:float,tipo:str):
        self.p = path
        self.h = h
        self.tipo = tipo
    
    def datos(self):
        df = pd.read_csv(self.p)
        return df
    
    def ajusteGauss(self):
        suavizado = []
        df = self.datos()
        df['fecha_actualizacion'] = pd.to_datetime(df['fecha_actualizacion'])

        for f in sorted(df['fecha_actualizacion']):
            df['suave'] = np.exp(
                -(((df['fecha_actualizacion'] - f).apply(lambda x: x.days)) ** 2) / (2 * self.h)
            )
            df['suave'] /= df['suave'].sum()
            suavizado.append(round(df['nuevos_casos'] * df['suave']).sum())
        df['suavizado'] = suavizado
        return df
    
    def ajuste3C(self):
        suavizado = []
        df = self.datos()
        df['fecha_actualizacion'] = pd.to_datetime(df['fecha_actualizacion'])

        for f in sorted(df['fecha_actualizacion']):
            dx = abs(((df['fecha_actualizacion'] - f).apply(lambda x: x.days)) /self.h)
            dxx = dx[dx<=1]
            df['suave'] = (70/81)* (1-dx** 3 )**3
            df['suave'] = df['suave']*dxx
            df['suave'] /= df['suave'].sum()
            suavizado.append(round(df['nuevos_casos'] * df['suave']).sum())
        df['suavizado'] = suavizado
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

    def graph_aj(self):
        if self.tipo == 'Gaussiano':
            df = self.ajusteGauss()
        elif self.tipo == 'Tricube':
            df = self.ajuste3C()
        elif self.tipo == 'Epanechnikov':
            df = self.ajusteEpa()
        else:
            print('No se reconoce el tipo de kernel')
        plt.figure(figsize=(10, 6))
        plt.title('Casos de covid-19 en Colombia')
        plt.xlabel('Fechas [aaaamm]')
        plt.ylabel('Número de casos')
        plt.plot(df['fecha_actualizacion'], df['nuevos_casos'], label='Curva original')
        plt.plot(df['fecha_actualizacion'], df['suavizado'], label='Curva suavizada con kernel %s'%(self.tipo))
        plt.legend()
        plt.savefig("Ajuste.png")
        plt.show()

    
