def dirReduc(arr):
    if len(arr) <= 1:
        return(arr)
    i = 0
    while i <= len(arr)-2:
        print(len(arr))
        if arr[i] == "NORTH" and arr[i+1] == "SOUTH" or arr[i] == "SOUTH" and arr[i+1] == "NORTH":
            arr.pop(i)
            arr.pop(i)
            i = 0
        elif arr[i] == "EAST" and arr[i+1] == "WEST" or arr[i] == "WEST" and arr[i+1] == "EAST":
            arr.pop(i)
            arr.pop(i)
            i = 0
        else:
            i += 1
    return(arr)






a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print((dirReduc(a)))

#1. to delete, they have to be one after another
#2. keep looping until everything that can be deleted has been deleted