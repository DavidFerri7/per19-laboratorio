#!/usr/bin/env python
# -*- coding: utf-8 -*-

#4. Crea una clase Fraccion con métodos para sumar, restar, multiplicar y dividir fracciones.

class Fraccion():
    def __init__(self,numero,num):
        self.numero = numero
        self.num = num

    def sumar(self):
        return self.numero + self.num

    def restar(self):
        return self.numero - self.num

    def multiplicar(self):
        return self.numero * self.num

    def dividir(self):
        return self.numero / self.num

y = Fraccion(4,7)

suma = y.sumar()
resta = y.restar()
mult = y.multiplicar()
div = y.dividir()

print("La suma de los 2 numeros es:", suma)
print("Y la resta:",resta)
print("Y la multiplicacion:",mult)
print("Y la division:",div)
