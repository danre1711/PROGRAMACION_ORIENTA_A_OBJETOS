from persona import Persona


class Empleado(Persona):
    '''
    Clase que hereda de persona para crear un objeto de tipo Empleado
    '''
    def __init__(self, id:int, sueldo:float, nombre:str, cedula:str, email:str,
                 genero:str, edad:int, ocupacion:str):
        Persona.__init__(self, nombre=nombre, email=email, genero=genero
                         , edad=edad, ocupacion=ocupacion, cedula=cedula)
        self._id = id
        self._sueldo = sueldo

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, nuevo_sueldo):
        self._sueldo = nuevo_sueldo

    def __str__(self):
        return f'Empleado: {self.__dict__.__str__()}'


if __name__ == '__main__':
    objEmpleado1 =  Empleado(nombre='Luis Perez', email='lperez@mail.com',genero='M'
                             ,ocupacion='Estudiante', edad=20,cedula='12345683633'
                             ,sueldo=500, id=1)
    print(objEmpleado1)
    print('*'.center(20, '*'))
    print(f'Nombre: {objEmpleado1.nombre}')
    print(f'Email: {objEmpleado1.email}')
    print(f'Sueldo: {objEmpleado1.sueldo}')


