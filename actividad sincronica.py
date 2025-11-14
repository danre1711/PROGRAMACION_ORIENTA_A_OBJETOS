#CREAR LA CLASE COMPOSICION LLAMADA MOTOR

class Motor:
    def __init__(self, tipo: str, potencia: int):
        self._tipo = tipo
        self._potencia = potencia

    #PROPIEDADES
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor

    @property
    def potencia(self):
        return self._potencia
    @potencia.setter
    def potencia(self, valor):
        self._potencia = valor

    #COMPORTAMIENTOS
    def encender_motor(self):
        return f"El motor {self._tipo} se ha encendido."

    def detener_motor(self):
        return f"El motor {self._tipo} ha sido detenido."

    def __str__(self):
        return f"Motor(tipo={self.tipo}, potencia={self.potencia}HP)"


class Vehiculo:
    def __init__(self, marca:str, modelo: str, anio: int):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, valor):
        self._anio = valor

    def encender(self):
        return f"El vehiculo {self._modelo} se encendio correctamente"

    def apagar(self):
        return f"El vehiculo {self._modelo} se apago correctamente"

    def __str__(self):
        return f"Vehiculo {self._modelo} {self.anio}"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas, motor:Motor ):
        super().__init__(marca, modelo, anio)
        self._puertas = puertas
        self._motor = motor

    @property
    def puertas(self):
        return self._puertas

    @puertas.setter
    def puertas(self, valor):
        self._puertas = valor

    @property
    def motor(self):
        return self._motor

    def abrir_maletero(self):
        return "El maletero del automóvil ha sido abierto."

    def tocar_claxon(self):
        return "¡Piiiiiiii! El automóvil toca el claxon."

    def __str__(self):
        return f"[Automovil] {super().__str__()} - Puertas: {self._puertas} - {self.motor}"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, cilindraje, motor: Motor):
        super().__init__(marca, modelo, anio)
        self._cilindraje = cilindraje
        self._motor = motor

    @property
    def cilindraje(self):
        return self._cilindraje

    @cilindraje.setter
    def cilindraje(self, valor):
        self._cilindraje = valor

    @property
    def motor(self):
        return self._motor

    def hacer_caballito(self):
        return "La moto está haciendo un caballito "

    def usar_patada_arranque(self):
        return "Se ha usado correctamente la patada de arranque"

    def __str__(self):
        return f"[Motocicleta] {super().__str__()} - Cilindraje: {self._cilindraje}cc - {self.motor}"


# SE CREAN LOS DIFERENTES TIPOS DE MOTORES
motor1 = Motor("Gasolina", 150)
motor2 = Motor("Híbrido", 200)
motor3 = Motor("Gasolina", 90)
motor4 = Motor("Eléctrico", 70)

# SE CREAN AUTOMOVILES
auto1 = Automovil("Toyota", "Corolla", 2020, 4, motor1)
auto2 = Automovil("Honda", "Civic", 2021, 4, motor2)

# SE CREAN MOTOS
moto1 = Moto("Yamaha", "R3", 2022, 321, motor3)
moto2 = Moto("Honda", "CB190R", 2019, 190, motor4)

# COMPORTAMIENTO
print(auto1.encender())
print(auto1.abrir_maletero())
print(auto1.motor.encender_motor())
print(auto1)

print("\n------------------------------\n")

print(moto1.usar_patada_arranque())
print(moto1.hacer_caballito())
print(moto1.motor.detener_motor())
print(moto1)
