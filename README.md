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

Contiene 2 modulos de python en donde se hacen algunas pruebas:

+ CasoFalloAlgotimodeLuhn.py
+ ComparacionLuhnHamming.py

**CasoFalloAlgotimodeLuhn.py** Muestra varios casos donde falla el algoritmo de luhn para el vector de comprobacion [1,3,1,3,..,3,1]
**ComparacionLuhnHamming.py** Compara los casos donde falla el algorimo de luhn y donde el algoritmo de hammign no falla, se hace una comparación usando un codigo con números enteros, sin embargo para usar el codigo de hamming se recomienda usar directamente un codigo con números binarios, pues el codigo hamming permite en caso de un error en un digito saber cual digito es el errado.

## Documento en google colab

Un documento con la información mas detallada se puede entontrar en el siguiente link de colaboratory de [google colab](https://colab.research.google.com/notebooks/intro.ipynb#recent=true), un cuaderno de python, donde se encuentran los códigos anteriores con una explicación mas detallada.

+ [![Link de cuaderno de notebook en colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1b5oWEBxpD90aoT4fA5ET8MupgAaz97QR?usp=sharing)

_Hecho por: yeison cuervo basurto_
