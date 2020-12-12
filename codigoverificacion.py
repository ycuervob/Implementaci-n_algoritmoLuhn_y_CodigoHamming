"""
Codigo que encuentra el codigo de verificación para el vector de control especifico ingresado, se ingresa hasta antes del
codigo de verificación. 
"""

def codigoVer(codi):
    
    codst = list(map(int, str(codi)))
    
    cod = []
    for i in range(len(codst)):
        cod.append(int(codst[i])) 
    
    suma = 0
    for i in range(1,len(cod),2):
        cod[i] = (cod[i] * 3) % 10
        
    for i in range(0,len(cod)):
        
        suma = suma + cod[i]
    
    return "El digito de control es: "+ str(10-(suma % 10))