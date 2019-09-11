from time import time

def insertion_Sort (lista):
    i = 0
    j = 0
    n = len(lista)
    global comparaciones

    for i in range (1,n):
        val = lista[i]
        j = i
        while j > 0 and lista [j-1] > val:
            lista[j] = lista [j-1]
            j -= 1
            comparaciones +=1
        lista[j] = val
    #return lista


lista = [66, 71, 16, 21, 79, 9, 40, 60, 5]
#lista = [66,71,16,21,79,9,40,60,5,15,1,28,35,100,25,15,36,58,45]
comparaciones = 0
t0 = time()
insertion_Sort(lista)
t1 = time()
print ("Lista ordenada: ")
print (lista, "\n")
print ("Tiempo: {0:f} segundos ".format(t1-t0))
print ("Comparaciones: ", comparaciones)
