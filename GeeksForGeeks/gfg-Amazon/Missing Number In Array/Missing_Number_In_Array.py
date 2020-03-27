"""Algorithm is :-
1. Get the sum of numbers which is total = n*(n+1)/2
2. Subtract all the numbers from sum and
   you will get the missing number
"""

#Function to find missing value
def missing_number(arr):
    n = len(arr)
    #Taken n+1 instead of n because in arr one element is missing
    total = (n+1)*(n+2)//2
    sum_of_arr = sum(arr)
    return (total - sum_of_arr)

#Driver program
arr = [1, 2, 4, 5, 6]
ans = missing_number(arr)
print("The missing element is {}".format(ans))
