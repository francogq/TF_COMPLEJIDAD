import math
import random
import numpy as np
from statistics import mode

class cartilla():
    def __init__(self):
        self.fila=6
        self.columna=16
        self.cartilla=[]
    
    # Genera la cartilla principal en forma de matriz
    def generarCartilla(self):
        self.cartilla=np.ones(shape=(self.fila,self.columna)).astype(int)*0
        
    # Rellena diamantas de manera aleatoria desde el numero 5 al 10 (6 colores)
    def rellenarDiamantes(self):
        for f in range(self.fila):
            for c in range(4,self.columna):
                self.cartilla[f][c]=random.randint(5,10)

    # Rellena Jugadores de manera aleatoria desde el principio si es que asi lo desean
    def rellenarJugadoresPrincipio(self,n):
        
        while n<0 or (n-1)==0 or (n-1)>3:
            print("NO ESTAS INGRESADNO CORRECTAMNETE ")
            n=int(input("ingresa valor :"))
        
        if (n-1)==1:
            print("INGRESARON DOS JUGADORES")
            self.cartilla[random.randint(0,5)][0]=1
            self.cartilla[random.randint(0,5)][1]=2
        if (n-1)==2:
            print("INGRESARON TRES JUGADORES")
            self.cartilla[random.randint(0,5)][0]=1
            self.cartilla[random.randint(0,5)][1]=2
            self.cartilla[random.randint(0,5)][2]=3
        if (n-1)==3:
            print("INGRESARON TRES JUGADORES")
            self.cartilla[random.randint(0,5)][0]=1
            self.cartilla[random.randint(0,5)][1]=2
            self.cartilla[random.randint(0,5)][2]=3
            self.cartilla[random.randint(0,5)][3]=4

  

    # Quitar diamantes por posicion que debe insertar
    def quitarDiamantes(self,posicion):
        contador=1
        lista=[]
        for c in range(4,self.columna):
            if self.cartilla[posicion-1][c]!=0 and  contador<=2:
                lista.append(self.cartilla[posicion-1][c])
                self.cartilla[posicion-1][c]=0
                contador+=1
        return lista

    #Mejor Posicion a quitar diamantes si no encuentra me retorna 22
    def posicionMejorAquitarDiamantesComputadora(self):
        contador=1
        for f in range(self.fila):
            for c in range(4,self.columna-1):
                if contador<2:
                    if self.cartilla[f][c]!=0  and self.cartilla[f][c]==self.cartilla[f][c+1]:
                        return f
                    contador+=1
            contador=1    
        return 22
               
            
    #  Inserta jugadores por posicion que desean
    def setJugador1(self,posicion):
        for f in range(self.fila):
            if self.cartilla[f][0]== 0 and f==posicion:
                self.cartilla[f-1][0]=1
    def setJugador2(self,posicion):
        for f in range(self.fila):
            if self.cartilla[f][1]== 0 and f==posicion:
                self.cartilla[f-1][1]=2
    def setJugador3(self,posicion):
        for f in range(self.fila):
            if self.cartilla[f][2]== 0 and f==posicion:
                self.cartilla[f-1][2]=3
    def setJugador4(self,posicion):
        for f in range(self.fila):
            if self.cartilla[f][3]== 0 and f==posicion:
                self.cartilla[f-1][3]=4

   
        
    # Mostrar toda la cartilla
    def mostrarCartilla(self):
        print(self.cartilla)
        


carti=cartilla()
carti.generarCartilla()
carti.rellenarDiamantes()
'''
carti.generarCartilla()
carti.rellenarDiamantes()
N=int(input("INGRESE NUMERO DE JUGADORES :"))

carti.rellenarJugadoresPrincipio(N)
print("CARTILLA CON JUGADORES")
carti.mostrarCartilla()

'''
'''
carti.mostrarCartilla()
print('retornar mejor poscion')
print(carti.posicionMejorAquitarDiamantesComputadora())'''


