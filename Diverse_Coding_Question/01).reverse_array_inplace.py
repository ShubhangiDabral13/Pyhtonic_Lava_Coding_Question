"""
To reverse an array inplace.
Time complexity is 0(N) where is the length for array
"""
def reverse_array(arr):

    l = len(arr)

    for i in range(0,l//2):
        arr[i],arr[l-1-i] = arr[l-1-i],arr[i]
        
    return arr


arr = [2,4,9,5]
print(reverse_array(arr))

arr = [1,9,5,14,78,29,2]
print(reverse_array(arr))
