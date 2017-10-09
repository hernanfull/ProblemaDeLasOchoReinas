#!/usr/bin/env python
# -*- coding: utf-8 -*-
from help import *

def init():
    matriz = []
    solucion = []
    soluciones = 0

    for n in range(8):
        matriz.append([])
        for m in range(8):
            matriz[n].append(0)

    j = 0
    while True:
        if sgte(matriz, solucion, j):
            j = 0
        else:
            elemento = solucion.__getitem__(solucion.__len__()-1)
            j = elemento[1] + 1
            matriz[elemento[0]] [elemento[1]] = 0
            solucion.pop()

        if solucion.__len__() == 8:
            soluciones += 1
            printMatriz(matriz)
            print("===============================")
            elemento = solucion.__getitem__(solucion.__len__()-1)
            j = elemento[1] + 1
            matriz[elemento[0]] [elemento[1]] = 0
            solucion.pop()

        if len(solucion) == 0 and elemento == [0, 7]: ## Final del arbol
            print("Final del Arbol - %s Soluciones encontradas" % soluciones)
            return False

    return True

print("=================================")
print(" Problema de las 8 reinas - VDFS")
print("=================================")
init()
