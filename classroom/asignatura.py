class Asignatura:

    def __str__(self):
        completo = self._nombre+" "+self._salon
        return completo
        
    def __init__(self, nombre, salon="remoto"):
        self._nombre = nombre
        self._salon = salon
