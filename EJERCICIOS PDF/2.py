#!/usr/bin/env python
# -*- coding: utf-8 -*-
#2.Crea una clase Contador con los métodos para incrementar y decrementar el contador.
#La clase contendrá un constructor por defecto, un constructor con parámetros y los métodos getters y setters

class Contador():
    def __init__(self,numero=0):
        self.numero = numero

    def getters(self):
        return self.numero + 1

    def setters(self):
        return self.numero - 1

cont = Contador()
d= cont.getters()
contador = []

for i in range(10):
    contador.append(d+i)

print(contador)
