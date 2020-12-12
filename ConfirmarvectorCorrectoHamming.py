"""
Codigo para confirmar si un codigo recibido es correcto si lo res debe retornar un vector [0,0,..,0]
"""

def retornaConfirmacio(vector):
    res = []
    
    #Esta parte multiplica el vector por la matriz de comprobación adecuada
    for j in range(len(vector[0])-vector[1]):
        suma = 0
        for k in range(vector[1]):
            if k != j+1:
                suma = suma + vector[0][k]
        
        for w in range(len(vector[0])-vector[1]):
            if w == j:
                suma = suma + vector[0][vector[1]+w]
        
        res.append(suma % 2)
        
    return res
