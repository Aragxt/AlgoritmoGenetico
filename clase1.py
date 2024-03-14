## CREADO Versión inicial NDD Sept 2020
## Modificaciones posteriores

import random
import numpy as np


"""   Comentarios son Una Linea: #
O triple comilla doble: Un bloque"""

#Si se desea una población inicial no aleatoria
# 10
# MEJORA: Tamaño de la Población como parametro 
#random.seed(1)
#print("\n","aletorio:", random.randrange(2)) #Entero 0 o 1

##### FUNCIONES PARA OPERADORES


def evalua(n,x,poblIt,utilidad):
    suma=0
    total=0
    for i in range(0, n):
      for j in range(0,x):
        suma+=poblIt[i,j]*utilidad[j]
      fitness[i]=suma
      total+=suma
      suma=0
    return fitness,total

def imprime(n,total,fitness,poblIt):
    #Tabla de evaluación de la Población
    acumula=0
    print ("\n",'Tabla Iteración:',"\n")
    for i in range(0, n):
      probab=fitness[i]/total
      acumula+=probab
      print([i+1]," ",poblIt[i],"  ",fitness[i]," ","{0:.3f}".format(probab)," ","{0:.3f}".format(acumula))
      acumulado[i]=acumula
    print("Total Fitness:      ", total)
    return acumulado

def seleccion(acumulado):
    escoje=np.random.rand()
    print("escoje:      ", escoje)

    for i in range(0,n):
      if acumulado[i]>escoje:
         padre=poblIt[i]
         break
    print("ESTE ES EL ACUMULADO: ", acumulado[i])
    return (padre)



def cruce(a1,p1,p2,a2,x):
    cruces = 1/(n-1)
    #print("Cruces: ", cruces)
    print("El punto de corte es: ", a2)
    if a1<Pcruce:
        print("Mas grande", Pcruce, "que ", a1, "-> Si Cruzan")
        #Error en cruce siempre fijo
        print("_____________________________________________________________________________________________________________________________________________________________")
        print("ENTRO AL CRUCE ")
      #Reemplace por x para que sea mas general en caso que nos 
      #den un valor mayor a 4
        s = 0
        i = 0
        while s == 0: #0,89
          i += 1
          if a2<cruces: #0,33
            # print("Cruce entre ", i, "y ", i+1)
            temp1=p1[0:i]
            temp2=p1[i:x]
            temp3=p2[0:i]
            temp4=p2[i:x] 
            hijo1 = list(temp1)
            hijo1.extend(list(temp4))
            hijo2 = list(temp3)
            hijo2.extend(list(temp2))
            print("YA LOS CRUZO Y EL RESULTADO ES")
            print(hijo1)
            print(hijo2)
            i = x
            return hijo1,hijo2
          else:
             cruces += 1/(n-1)

    else:
      print("Menor", Pcruce, "que ", a1, "-> NO Cruzan")
      hijo1=p1
      hijo2=p2
      return hijo1,hijo2

    

#En esta función se realiza la verificación de la restricción de peso
def verificacromosoma(hijo, pesos):
  contador=0
  for i in range(0,x):
    contador+=hijo[i]*pesos[i]
  if contador <=pesmax:
    return True
  else:
    print("Se da pena de muerte a: ",hijo)
    return False

def calpeso(hijo, pesos):
  contador=0
  for i in range(0,x):
    contador+=hijo[i]*pesos[i]
  return contador

#En esta función se realiza la mutación
def mutacion (x,p,Pmuta):
    #print("ENTRO A MUTAR")
    valores=[]
    for i in range(0,x):
      valores.append(np.random.rand())
    for i in range(0,x):
      if valores[i]<Pmuta:
        if p[i]==1:
          p[i]=0
        else:
          p[i]=1
    return p



#### Parametros #####
#x=4  #numero de variables de decision - Elementos diferentes: x
#n=4  #numero de individuos en la poblacion - cromosomas: n
Pcruce=0.98  #Probabilidad de Cruce
Pmuta=0.1   #Probabilidad de Mutación
print("Ingrese el tamaño de la población: ")
n = int(input())
print("Ingrese el tamaño de los cromosomas: ")
x = int(input())
print("Ingrese el peso máximo de la mochila: ")
pesmax = int(input())
print("Ingrese el número de iteraciones: ")
iteraciones = int(input())
# x=4
# n = 4
print("ESTO ES: ", n, x)

fitness= np.empty((n))
acumulado= np.empty((n))
suma=0
total=0

#Individuos, soluciones o cromosomas
poblInicial = np.random.randint(0, 2, (n, x)) # aleatorios (n por x) enteros entre [0 y 2)
#random.random((4,5)) # 4 individuos 5 genes

# Ingresar los datos del Problema de la Mochila - Peso y Utilidad de los Elementos

pesos = np.random.randint(0, 7, (n))
utilidad = np.random.randint(0, 7, (n))

# pesos = [7, 6, 8, 2]
# utilidad = [4, 5, 6, 3]

#pesos = [5, 7, 10, 30, 25]
#utilidad = [10, 20, 15, 30,15]

print("Poblacion inicial Aleatoria:","\n", poblInicial)
print("\n","Utilidad:", utilidad) 
print("\n","Pesos", pesos )   
poblIt=poblInicial

######  FIN DE LOS DATOS INICIALES



##Llama función evalua, para calcular el fitness de cada individuo
fitness,total=evalua(n,x,poblIt,utilidad)
#####print("\n","Funcion Fitness por individuos",  fitness)
#####print("\n","Suma fitness: ",  total)

##### imprime la tabla de la iteracion
imprime(n,total,fitness,poblIt)

##### ***************************************
# Inicia Iteraciones

# Crear vector de 5x2 vacio  a = numpy.zeros(shape=(5,2))
iter = 0
niter = 0 
while iter < (iteraciones):
  niter += 1
  print("\n","Iteración ", iter+1)
  iter += 1 
  for i in [1]:  ## Para el bloque de 2 hijos cada vez
    # Para la prueba habiamos puesto un valor fijo de escoje
    # lo volvi a poner aletorio par que cada vez se escoja un padre diferente
    papa1=seleccion(acumulado) #escoje = 0.0404) # Padre 1
    print("padre 1:", papa1)
    papa2=seleccion(acumulado) #escoje = 0.5121) # Padre 2
    print("padre 2:", papa2)

    hijoA,hijoB=cruce(np.random.rand(),papa1,papa2, np.random.rand(),x)
    print("hijo1: ", hijoA)
    #poblIt[i]=hijoA
    print("hijo2: ", hijoB)
    #poblIt[i+1]=hijoB
    valor1=mutacion(x,hijoA,Pmuta)
    hijoA=valor1
    #print("ESTO ES VALOR1: ", valor1,x)
    poblIt[i]=hijoA
    #print("ESTO ES POBLIT I: ", poblIt[i])
    valor2=mutacion(x,hijoB,Pmuta)
    hijoB=valor2
    poblIt[i+1]=hijoB
    if verificacromosoma(hijoA,pesos) and verificacromosoma(hijoB,pesos):
       print("El peso de A es: ",calpeso(hijoA, pesos))
       print("El peso de B es: ",calpeso(hijoB, pesos))
    elif verificacromosoma(hijoA,pesos) == False and verificacromosoma(hijoB,pesos) == False:
      print("Se da pena de muerte al hijo A: ",hijoA)
      print("Se da pena de muerte al hijo B: ",hijoB)
      iter -= 1
    elif verificacromosoma(hijoB,pesos) == False or verificacromosoma(hijoA,pesos) == False:
        if verificacromosoma(hijoA,pesos) == False:
          print("Se da pena de muerte al hijo A: ",hijoA)
          print("El peso de B es: ",calpeso(hijoB, pesos))
          iter -= 1
        else: 
          print("El peso de A es: ",calpeso(hijoA, pesos))
          print("Se da pena de muerte al hijo B: ",hijoB)
          iter -= 1


    

  print("\n","Poblacion Iteración ", iter+1,"\n", poblIt)
  fitness,total=evalua(n,x,poblIt,utilidad)

  #### print("\n","Funcion Fitness por individuos",  fitness)
  #### print("\n","Suma fitness: ",  total)

  ##### imprime la tabla de la iteracion
  imprime(n,total,fitness,poblIt)
  print("Numero de iteraciones total1: ", niter)