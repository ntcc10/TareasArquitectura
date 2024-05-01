class Cocinero:
    def __init__(self, nombre, salario, estacion):
        self.name=nombre
        self.salary=salario
        self.estacion =estacion
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    def getEstacion(self):
        return self.estacion
    def setSalary(self, sal):
        self.salary = sal
    def setName(self, nom):
        self.name= nom
    def setEstacion(self, est):
        self.estacion = est


def registrarCocinero(cocinero):
    consulta = "INSERT INTO cocineros (nombre, estacion, salario) VALUES (?, ?, ?)"
    valores = (cocinero.getName(), cocinero.getEstacion(), cocinero.getSalary())

    cursor.execute(consulta, valores)

    conn.commit()
    conn.close()
