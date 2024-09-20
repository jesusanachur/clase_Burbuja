def busquedas(arr,bus):
    if len(arr)>1:
        idx= len(arr)//2
        if arr[idx]==bus:
            return idx
        else:
            bus>arr[idx]
            
    else:
        return None    

