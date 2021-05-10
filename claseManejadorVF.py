import csv, os
from claseViajeroF import ViajeroFrecuente
from menu import Menu

class ControlViajerosF:
    __listaViajerosF = []
    def __init__(self):
        self.__listaViajerosF = []
    def agregarViajeros(self,viajeroF):
        self.__listaViajerosF.append(viajeroF)
        
    def crear_Instancias(self):
        archivo = open('ViajerosFrecuentes.csv','r')
        leer = csv.reader(archivo,delimiter=',')
        for fila in leer:
            id_pas = int(fila[0])
            dni = fila[1]
            name = fila[2]
            surname = fila[3]
            millas = int(fila[4])
            viajero = ViajeroFrecuente(id_pas,dni,name,surname,millas)
            self.agregarViajeros(viajero)
        archivo.close()

    def __str__(self): 
         for i in self.__listaViajerosF:
             return f'{self.__listaViajerosF[0]},{self.__listaViajerosF[1]},{self.__listaViajerosF[2]},{self.__listaViajerosF[3]},{self.__listaViajerosF[4]}'+'\n\n'

    def BuscarViajero(self,numeroViajero):
        encontro = False
        for viajero in self.__listaViajerosF:
            if numeroViajero == viajero.obtenerNumero():
                encontro = True
                break
        if encontro == True:
            ObjetoMenu = Menu()
            ObjetoMenu.Ejecutar(viajero)    
           
        else:
            print('Viajero ingresado incorrecto o inexistente')  