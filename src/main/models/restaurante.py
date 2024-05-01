class Restaurante:
    def __init__(self, nombre,ubicacion,dueño):
        self.name = nombre
        self.ubicacion = ubicacion
        self.dueño = dueño
    def getNombre(self):
        return self.nombre
    def getUbi(self):
        return self.ubicacion
    def getDueño(self):
        return self.dueño
    def setNombre(self,name):
        self.name = name
    def setUbi(self,ubi):
        self.ubicacion= ubi
    def setDueño(self,dueño):
        self.dueño= dueño
            