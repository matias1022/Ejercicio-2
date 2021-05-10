

class ViajeroFrecuente:
    numero_viajero=0
    dni=""
    nombre=""
    apellido=""
    millas_acum=0.0

    def __init__ (self, numero_viajero = 0, dni = "", nombre = "", apellido = "", millas_acum = 0.0):     
        self.__numero_viajero = numero_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

    def cantidadTotaldeMillas(self):
        return self.__millas_acum

    def acumularMillas(self,millas):
        self.__millas_acum+=millas
        return self.__millas_acum
    def __str__(self):
        return f"Numero de viajero:{self.__numero_viajero}\nNombre:{self.__nombre}\nApellido:{self.__apellido}\nDNI:{self.__dni}\nCantidad de millas:{self.__millas_acum}\n"
   
    def CanjearMillas(self,cantMillas):
        if cantMillas <= self.__millas_acum:
           self.__millas_acum =self.__millas_acum - cantMillas
           print("Millas canjeadas: {}, Total de millas: {}".format(cantMillas,self.__millas_acum))
        else:
           print("Error en la operacion")
    def obtenerNumero(self):
        return self.__numero_viajero