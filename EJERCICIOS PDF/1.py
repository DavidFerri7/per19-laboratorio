#1.Crea una clase Cuenta con los métodos ingreso, reintegro y transferencia.
#La clase contendrá un constructor por defecto, un constructor con parámetros,
#y los métodos para obtener información (los también llamados getters. Suelen tener la forma get_xxxxx)
#o para almacenar información (también llamados setters. Tienen la forma de set_xxxx)


class Cuenta():
    def __init__(ingreso,reintegro,transferencia):
        self.ingreso = ingreso
        self.reintegro = reintegro
        self.transferencia = transferencia

    def get_ingreso(self):
        return self.ingreso

    def get_reintegro(self):
        return self.reintegro

    def get_transferencia(self):
        return self.transferencia

d = Cuenta(1800,5,500)
g = d.get_ingreso()
print(g)
