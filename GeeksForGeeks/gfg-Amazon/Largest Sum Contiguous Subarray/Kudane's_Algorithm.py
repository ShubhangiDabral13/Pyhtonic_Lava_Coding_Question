"""
Algorithm:-
Initialize:
    max_so_far = 0
    current_max = 0

Loop for each element of the array
  (a) current_max = current_max + arr[i]
  (b) if(current_max < 0)
            current_max = 0
  (c) if(max_so_far < current_max)
            max_so_far = current_max
return max_so_far
"""

def find(arr):
    max_so_far,current_max = 0,0
    for i in arr:
        current_max += i
        if current_max < 0:
            current_max = 0
        elif max_so_far < current_max:
            max_so_far = current_max

    return max_so_far

#Driver Program
arr = [1, 2, 3, -2, 5]
print("Maximum contiguous sum is {}".format(find(arr)))
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is {}".format(find(arr)))
