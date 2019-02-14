#!/usr/bin/env python
# -*- coding: utf-8 -*-

#3. Crea una clase Libro con los métodos préstamo, devolución y dame_info. La clase contendrá un
#constructor por defecto, un constructor con parámetros y los métodos getters y setters que
#consideres oportunos.

class Libro():
    def __init__(self,euros,devolucion,info):
        self.euros = euros
        self.devolucion = devolucion
        self.info = info

    def prestamo(self):
        return "El libro cuesta:",self.euros

    def devolucion(self):
        print("El libro ha de ser dentro de:", self.devolucion, "dias.")

    def dame_info(self):
        print("Se titula:",self.info)

libro = Libro(3.5,15,"El senyor de los anillos")
prest = libro.prestamo()
dev = libro.devolucion()
info = libro.dame_info()

print(prest,"\n",dev,"\n",info)
