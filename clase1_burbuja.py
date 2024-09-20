def quicksort(arr):
    menores=[]
    mayores=[]
    iguales=[]

    idx= len(arr)//2

    if len (arr)>1:
        pivote=arr[idx]
    else:
        return[]

    pivote= arr[ idx ]

    for num in arr:
        if num>pivote:
            mayores.append(num)
        elif num<pivote:
            menores.append(num)
        else:
            iguales.append(num)       

    return menores + iguales + mayores
print()
