import time
import random

def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1 

    # traverse through all elements 
    # compare each element with pivot
    for j in range(low, high):  
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

# function to perform quicksort


def quickSort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

i = 0
lista = []
while(i <= 10): #Define Tamaño de Lista
    h = random.randrange(0, 1000)
    lista.append(h)
    i = i+1


print(lista)
inicio = time.time()

# Código a medir
# -------------
quickSort(lista, 0, len(lista) - 1)
print(lista)

time.sleep(1)

fin = time.time()
print(fin-inicio)
