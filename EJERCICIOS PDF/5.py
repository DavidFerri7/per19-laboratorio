#!/usr/bin/env python
# -*- coding: utf-8 -*-

#5. Crea una clase Complejo con métodos para sumar, restar, multiplicar y dividir números
#complejos.

class Complejo():
    def __init__(self,n,ni,n2,ni2):
        self.n = n
        self.ni = ni
        self.n2 = n2
        self.ni2 = ni2

    def sumar(self):
        return (self.n+self.n2,"+",self.ni+self.ni2,"i")

    def restar(self):
        return (self.n+self.n2,"+",self.ni+self.ni2,"i")

    def multiplicar(self):
        real1 = self.n*self.n2
        real2 =-self.ni*self.ni2
        imag1= self.ni*self.n2
        imag2= self.n*self.ni2
        return (real1 + real2),"+",(imag1 + imag2),"i"

    def dividir(self):
        real1 = self.n*self.n2
        real2 =-self.ni*self.ni2
        imag1= self.ni*self.n2
        imag2= self.n*self.ni2
        numerador_real = real2 + real2
        numerador_imag = imag1 + imag2

        denom=self.n2**2 + self.ni2**2

        return (numerador_real,"+",numerador_imag,"/",denom)


o = Complejo(2,3,-4,8)
suma = o.sumar()
resta = o.restar()
mult = o.multiplicar()
div = o.dividir()

print("La suma de los complejos es:",suma)
print("Y la resta:",resta)
print("Y la multiplicacion:",mult)
print("Y la division:",div)
