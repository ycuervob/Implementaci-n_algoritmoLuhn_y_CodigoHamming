from CodigosBase.codigohamming import *
from CodigosBase.codigoverificacion import *

"""
Codigo que hace una comparación entre los métodos con el mismo, codigo y probando a transponer digitos
"""
codigo  = 86679035114
codigo2 = 86670935114



for i in range(10):
    for j in range(10): # for que generan numeros de 0 a 9
        
        #Esta sección solo se ejecuta si el vector código generado es el mismo, al permutar todos los posibles 
        #valores adyacentes entre dos digitos
        
        
        if codigoVer(str(i)+str(j)+"86679035114") == codigoVer(str(j)+str(i)+"86679035114") and i != j:
            
            print("Falla conprobacion algoritmo luhn")
            
            # permuta los primeros 2 elementos del código de manera que se intercambién dos digitos adyacentes
            print("")
            print(str(i)+"----"+str(j))
            print(codigoVer(str(i)+str(j)+"86679035114"))
            print(str(j)+"----"+str(i))
            print(codigoVer(str(j)+str(i)+"86679035114"))
            
            print("")
            print("")
            
            
            
        #Esta sección solo se ejecuta si el vector código generado es el mismo, al permutar todos los posibles 
        #valores adyacentes entre dos digitos
        
        if codigohamming(str(i)+str(j)+"86679035114") == codigohamming(str(j)+str(i)+"86679035114") and i != j:
            
            print("Falla conprobacion codigo de hamming")
            
            # permuta los primeros 2 elementos del código de manera que se intercambién dos digitos adyacentes
            print(str(i)+"----"+str(j))
            print(codigohamming(str(i)+str(j)+"86679035114"))
            print(str(j)+"----"+str(i))
            print(codigohamming(str(j)+str(i)+"86679035114"))
            print("")
            print("")
