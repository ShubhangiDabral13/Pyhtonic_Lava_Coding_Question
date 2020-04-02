def choco_dis(arr,m):
    if (arr == [] or m == []):
        print("Data is not provided")
        return
    elif(len(arr)<m):
        print("chocolate is not sufficient for student")
        return
    arr.sort()
    first = 0
    last = 0
    min = arr[m-1]+arr[0]
    n = len(arr)
    i = 1
    while(i+m-1<n):
        diff = arr[i+m-1] - arr[i]
        if diff < min:
            min = diff
            first =  i
            last = i +m -1
        i += 1
    return(arr[last] - arr[first])


arr = [12, 4, 7, 9, 2, 23, 25, 41,30, 40, 28, 42, 30, 44, 48, 43, 50]
m = 7 # Number of students
print("Minimum difference is", choco_dis(arr,m)) 
