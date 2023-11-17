# Libreria con 4 módulos para el ajuste de datos con Kernels diferentes.

## Modulo 1.
Cuenta con una clase que realiza el ajuste de datos de fecha vs cantidad a una curva suave por medio de un kernel gaussiano mediante el metodo ajusteGauss, y los grafica, con el metodo de plotG.

## Modulo 2.
Cuenta con una clase que realiza el ajuste de datos de fecha vs cantidad a una curva suave por medio de un kernel Tricube mediante el método ajuste3C, y los grafica, con el metodo de plot3C.

## Modulo 3.
Cuenta con una clase que realiza el ajuste de datos de fecha vs cantidad a una curva suave por medio de un kernel de Epanechnikov mediante el método ajusteEpa, y los grafica, con el metodo de plotE.

## Módulo 4.
Cuenta con una clase que realiza la comparacion grafica entre los kernels Gaussiano, Tricube y Epanechnikov para ajuste de datos de fecha vs cantidad a una curva suave y hace su respectiva graficación en el método plotComp,

Todos los metodos necesitan los siguientes datos:
    path: direccion en que se encuentra el archivo csv que contiene los datos. 
    h: factor que determina la "suavidad" de la curva y la exactitud del ajuste. Entre menor sea su valor
        mas suave sera la curva de ajuste pero mas se alejara de los datos ingresados y viceversa.

    Nota: La columnas del archivo csv a usar deben tener el nombre literal: fecha_actualizacion y       nuevos_casos