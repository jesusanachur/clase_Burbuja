
def Burbuja(arr):
    n =len(arr)
    i =0
    while i<n-1:
        j = i +1
        while j<n:
            print(arr[i], arr[j])
            if arr[i] < arr[j]:
                tempo=arr[j]
                arr[j]=[i]
                arr[i]=tempo
            j+=1
        i+=1
    return arr 
    
print( Burbuja([5,6,7,1,2]) )                