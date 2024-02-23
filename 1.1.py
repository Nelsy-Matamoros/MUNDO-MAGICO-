print("hola mundo")

matriz=[

    [10,30,50],
    [40,60,90],
    [20,70,0]

]
def BubbleSort(array):
    length = len(array)-1
    print(length)

    #Bucle para las pasadas
    for j in range(0, length):
        # comparaciones e intercambio
        for i in range(0,length):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1 ]
                array[j + 1] = aux
        return array


scores = [10,30,50,40,60,90,20,70,0]
print("antes de ordenar:")
print(scores)
print("despues de ordenar:")
print(BubbleSort(scores))










