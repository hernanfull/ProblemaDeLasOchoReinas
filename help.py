def printMatriz(matriz):
    for i in range(8):
        for j in range(8):
            print(matriz[i][j], end="   ")
        print("\n")

def validMatriz(matriz):
    count = 0
    limite = 7
    for i in range(8):
        aux = 0
        aux2 = 0
        aux3 = 0
        aux4 = 0
        aux5 = 0
        aux6 = 0
        for j in range(8):
            if matriz[i][j] == 1: # Filas
                aux += 1

            if matriz[j][i] == 1: # Columnas
                aux2 += 1

            if(j <= limite):
                if(matriz[j][j+count] == 1): # Diagonales superiores principales
                    aux3 += 1

                if(matriz[j+count][j] == 1): # Diagonales inferiores principales
                    aux4 += 1

            if(i >= j):
                if(matriz[j][i - j] == 1): # Diagonales superiores secundarias
                    aux5 += 1

            if(i+j <= 7):
                if(matriz[(7-j)][i + j] == 1): # Diagonales inferiores secundarias
                    aux6 += 1


        limite -= 1
        count += 1

        if(aux > 1) or (aux2 > 1) or (aux3 > 1) or (aux4 > 1) or (aux5 > 1) or (aux6 > 1):
            return False

    return True

def sgte(matriz, solucion, j=0):
    fila = solucion.__getitem__(solucion.__len__()-1)[0] + 1 if len(solucion) != 0 else 0
    for i in range(j, 8):
        matriz[fila][i] = 1
        if validMatriz(matriz):
            solucion.append([fila, i])
            return True
        else:
            matriz[fila][i] = 0

    return False
