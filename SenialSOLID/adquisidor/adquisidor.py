


from SenialSOLID.modelo.modelo import Senial



class Adquisidor:
    def __init__(self,p_tamanio):
        self.__tamanio = p_tamanio
        self.__buffer = Senial()

    def _leer_dato(self):
        pass

    def leer_senial(self):
        counter = 0
        dato = None
        while counter < self.__tamanio:
            try:
                dato = float(input("Agregar valor: "))
                self.__buffer.poner_valor(dato)
                counter = counter + 1
            except ValueError:
                print("Error: Ingrese un valor numérico")

    def obtener_senial_adquirida(self):

        return self.__buffer
