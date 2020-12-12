"""
Funcion que permite generar los dígitos de confirmación del código de hamming para palabras de hasta 64 bits, retorna un arreglo de tamaño 2:
    - El primer elemento del arreglo es el código hamming del codigo ingresado, con sus digitos de confirmación incluidos
    - El segundo elemento es el tamaño en binario del código ingresado sin incluir los dígitos de confirmación
"""

def codigohamming(codi):
    
    num = int(codi)
    codbin = []
      
    #Esta parte convierte el numero a binario
    while num >= 1:
        codbin.append(num % 2)
        num = num // 2
    codbin.reverse()
    
    
    #Esta parte selecciona el número de digitos de comrobación según el caso 
    tam = len(codbin)
    if(tam > 64):
        return "Muy Largo"
    elif tam <= 64 and tam > 32:
        bits_agregados = 7
    elif tam <= 32 and tam > 16:
        bits_agregados = 6
    elif tam <= 16 and tam > 8:
        bits_agregados = 5
    elif tam <= 8 and tam > 4:
        bits_agregados = 4
    elif tam <= 4 and tam > 2:
        bits_agregados = 3
    
    #Esta parte genera los digitos de comprobacion
    for j in range(bits_agregados):  
        suma = 0
        for k in range(tam):
            if k != j+1:
                suma = suma + codbin[k]
            
        codbin.append(suma % 2)
        
    
    return([codbin,tam])