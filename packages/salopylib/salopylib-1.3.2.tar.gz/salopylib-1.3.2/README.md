# Librería con dos módulos para el ajuste de datos con Kernels diferentes.

## Módulo 1
Cuenta con una clase que realiza el ajuste de datos de fecha vs cantidad a una curva suave por medio de un kernel gaussiano, tricube o de Epanechnikov y hace su respectiva graficación, a partir de los siguientes datos:
    path: direccción en que se encuentra el archivo csv que contiene los datos. 
    h: factor que determina la "suavidad" de la curva y la exactitud del ajuste. Entre menor sea su valor
        más suave será la curva de ajuste pero más se alejará de los datos ingresados y vicecversa.
    tipo: tipo de kernel a usar, puede ser Gaussiano, Tricube o Epanechnikov. Debe ingresarse de forma literal como string
    Nota: La columnas del csv a usar deben tener el nombre literal: fecha_actualizacion y nuevos_casos

## Módulo 2 
Cuenta con una clase que realiza la comparacion grafica entre distintos tipos de kernel para ajuste de datos de fecha vs cantidad a una curva suave y hace su respectiva graficación, a partir de los siguientes datos:
    path: direccción en que se encuentra el archivo csv que contiene los datos. 
    h: factor que determina la "suavidad" de la curva y la exactitud del ajuste. Entre menor sea su valor
        más suave será la curva de ajuste pero más se alejará de los datos ingresados y vicecversa.
    Nota: La columnas del csv a usar deben tener el nombre literal: fecha_actualizacion y nuevos_casos