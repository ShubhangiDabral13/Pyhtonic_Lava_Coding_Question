def Leaders(arr):
    ans = []
    arr_leader = arr[len(arr) -1]
    ans.append(arr_leader)
    for i in range(len(arr)-2,-1,-1):
        if arr[i] > arr_leader:
            ans.append(arr[i])
            arr_leader = arr[i]
    return ans

arr = [16, 17, 4, 3, 5, 2]
result = Leaders(arr)
print("The leaders of array ar as follow:-")
print(result)
