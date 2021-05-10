import os
from claseViajeroF import ViajeroFrecuente

class Menu:
      __op = 0
      def __init__(self,opcion=0):
        self.__op = opcion
      def Ejecutar(self,UnViajero):
          os.system('cls')
          salir = False

          while salir == False:
              print('1-\tMostrar cantidad de millas del viajero')
              print('2-\tAcumular Millas')
              print('3-\tCanjear Millas')
              print('0-\tSalir')
              self.__op = int(input('Ingrese la opcion: '))
              if self.__op == 1: #Mostrar Millas    
                  print(f'Cantidad total de millas: {UnViajero.cantidadTotaldeMillas()}')
              elif self.__op == 2: #Acumular Millas
                  millas = int(input('Ingrese la cantidad de millas a acumular:'))
                  print(f'Cantidad de millas actual: {UnViajero.acumularMillas(millas)}')    
              elif self.__op == 3: #CanjearMillas
                  millas = int(input('Ingrese la cantidad de millas a canjear:'))
                  UnViajero.CanjearMillas(millas)
              elif self.__op == 0: #Salir
                  salir = True
              else:
                 print('Opcion ingresada incorrecta')
                 input('Presiona ENTER para continuar...')


          print('Cerrando Menú..')   