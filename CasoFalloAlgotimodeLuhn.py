from CodigosBase.codigoverificacion import codigoVer

"""
Ejemplo: Se calcula el codigo de verificación del caso mostrado
"""
print(codigoVer("564897"))


"""
Ejemplo 2:

Esta parte muestra para que valores se pueden generar el mismo código de verficiación para codigos en los que fue cambiado
un componente adyacente
"""


for i in range(10):
    for j in range(10): # for que generan numeros de 0 a 9
        
        # Esta sección del código solo se ejecuta si el codigo generado es el mismo y los numeros i y j no son iguales
        
        if codigoVer(str(i)+str(j)+"492702090169") == codigoVer(str(j)+str(i)+"492702090169") and i != j:
            
            # permuta los primeros 2 elementos del código de manera que se intercambién dos digitos adyacentes
            print("")
            print(str(i)+"----"+str(j))
            print(codigoVer(str(i)+str(j)+"492702090169"))
            print(str(j)+"----"+str(i))
            print(codigoVer(str(j)+str(i)+"492702090169"))