import random, time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped: break
    return arr


i = 0
lista = []
while(i <= 5000):
    h = random.randrange(0, 1000)
    lista.append(h)
    i = i+1



inicio = time.time()

# Código a medir
# -------------

bubble_sort(lista)

time.sleep(1)

fin = time.time()
print(fin-inicio) 
