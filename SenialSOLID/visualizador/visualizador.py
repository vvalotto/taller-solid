class Visualizador:

    def mostrar_datos(self, senial):
            print('Mostrar la senial')
            for i in range(0, senial.obtener_tamanio()):
                print(senial.obtener_valor(i))

