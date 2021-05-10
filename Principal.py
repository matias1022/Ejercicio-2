from claseViajeroF import ViajeroFrecuente
from claseManejadorVF import ControlViajerosF

def testar():
    
    testeo = ViajeroFrecuente(5,"43453543","Matias","Gonzalez",8)
    print(testeo)
    testeo.acumularMillas(20)
    print('Cantidad TOTAL de Millas: {}' .format(testeo.cantidadTotaldeMillas()))
    testeo.CanjearMillas(7)
 

if __name__ == '__main__':
    testar()
    lista = ControlViajerosF()
    lista.crear_Instancias()
    print("---Lista De Viajeros---")
    print(lista)
    print("Ingresar numero de viajero frecuente a buscar:")
    num = int(input())
    lista.BuscarViajero(num)