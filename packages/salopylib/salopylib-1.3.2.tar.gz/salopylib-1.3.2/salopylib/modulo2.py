from ajuste import ajusteKernel
import pandas as pd
import matplotlib.pyplot as plt

class compKernel:

    '''
    Clase que realiza la comparacion grafica entre distintos tipos de kernel para ajuste de datos 
    de fecha vs cantidad a una curva suave y hace su respectiva graficación, 
    a partir de los siguientes datos:
    path: direccción en que se encuentra el archivo csv que contiene los datos. 
    h: factor que determina la "suavidad" de la curva y la exactitud del ajuste. Entre menor sea su valor
        más suave será la curva de ajuste pero más se alejará de los datos ingresados y vicecversa.
    La columnas del csv a usar deben tener el nombre literal: fecha_actualizacion y nuevos_casos
    '''

    def __init__(self,path:str,h:float):
        self.p = path
        self.h = h
    
    def plotComp(self):
        ajustes = ajusteKernel(self.p,self.h,'all')
        dfG, df3, dfE = ajustes.ajusteGauss(), ajustes.ajuste3C(), ajustes.ajusteEpa()
        plt.figure(figsize=(10, 6))
        plt.title('Casos de covid-19 en Colombia')
        plt.xlabel('Fechas [aaaamm]')
        plt.ylabel('Número de casos')
        plt.plot(dfG['fecha_actualizacion'], dfG['nuevos_casos'], label='Curva original')
        plt.plot(dfG['fecha_actualizacion'], dfG['suavizado'], label='Kernel Gaussiano')
        plt.plot(df3['fecha_actualizacion'], df3['suavizado'], label='Kernek Tricube')
        plt.plot(dfE['fecha_actualizacion'], dfE['suavizado'], label='Kernel Epanechnikov')
        plt.legend()
        plt.savefig("CompAjuste.png")
        plt.show()
