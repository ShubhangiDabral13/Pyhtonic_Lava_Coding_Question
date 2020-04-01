def find_equilibrium(arr):
    for i in range(1,len(arr)-1):
        p = i
        arr1 = arr[0:p]
        arr2 = arr[p+1:len(arr)]
        if(sum(arr1) == sum(arr2)):
            print("The equilibrium index is {}".format(p))
            return

    print("No equilibrium index")

#Driver function
arr = [-7, 1, 5, 2, -4, 3, 0]
find_equilibrium(arr)
