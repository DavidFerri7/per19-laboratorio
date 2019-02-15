#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Producto():
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

class Medicamento(Producto):
    def __init__(self,nombre,precio,compuesto,porcentaje):
        super().__init__(nombre,precio)
        self.compuesto = compuesto
        self.porcentaje = porcentaje

    def get_compuesto(self):
        return self.compuesto

    def get_porcentaje(self):
        return self.porcentaje

class Laboratorio():
    def __init__(self,nombre,lista_productos):
        self.nombre = get_nombre
        self.lista_productos = lista_productos

    def get_nombre(self):
        return self.nombre

    def get_lista(self):
        return self.lista_productos


lista_productos = []
prod1 = Producto("Pasta de dientes","5$")
prod2 = Producto("Cepillo","2%")
med1 = Medicamento("Dalsy","12","tetraoxofelanato","5%")
med2 = Medicamento("Ibuprofeno","8","ibuprofenil","67%%")
lista_productos.append(prod1,prod2,med1,med2)

lab = Laboratorio("Pyfarm",lista_productos)
print("El laboratorio se llama {nombre} y contiene {lista_productos}".format(nombre=self.nombre,lista_productos=self.lista_productos))
