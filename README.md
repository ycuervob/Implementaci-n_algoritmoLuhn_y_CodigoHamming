# Implementación  algoritmo de Luhn y CodigoHamming

_En este repositorio se encuentran algunos módulos de python donde se hace una implementacion del algorimo de luhn y del código de hamming, así como varias pruebas de su funcionamiento y una comparacion de los mismos_

## Codigos Base

Contiene 3 módulos de python que son la base de las pruebas:

+ codigohamming.py
+ CongirmacionVectorCorrectohamming.py
+ codigoverficacion.py

**codigohamming.py:** Permite ingresar un número que representa el código, lo convierte en binario y luego genera para ese número en binario los digitos de verificación.

**CongirmacionVectorCorrectohamming** Permite con un vector binario generado comprobar si cumple con los criterios de una matriz de comprobacion de hamming la cual genera un vector de ceros si el vector binario cumple con los criterios de la matriz, la idea de esto, es que antes de enviar el código el vector cumple con los criterios de la matriz, por lo tanto después de enviar el código también debe hacerlo.

**codigoverficacion** Permite generar un código de verifiacion para el algorimo de luhn con un vector de control [1,3,1,3,..,3,1]

## Ruta predeterminada

Contiene


_Hecho por: yeison cuervo basurto_
