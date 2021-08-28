class modelo:
    """
    Clase modelo (señal)
    """
    def __init__(self):
        self._senial = []
        self._tamanio_senial = 0

    def obtener_tamanio(self):
        self._tamanio_senial=len(self._senial)

    def obtener_valor(self, var):
        if (self._tamanio_senial == 0 ) or (var>self._tamanio_senial):
            raise Exception("Error")
        return (self._senial[var])

    def poner_valor(self, valor):
        self._senial.append(valor)