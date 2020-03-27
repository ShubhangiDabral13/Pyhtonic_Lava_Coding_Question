"""
Algorithm :-
1) Iterate through every element of 12[] starting from last
   element. Do following for every element 12[i]
    a) Store last element of 11[i]: last = ar1[i]
    b) Loop from last element of 11[] while element 11[j] is
       smaller than 12[i].
          11[j+1] = 11[j] // Move element one position ahead
          j--
    c) If any element of 11[] was moved or (j != m-1)
          11[j+1] = 12[i]
          12[i] = last
"""

def merge(l1,l2,m,n):
    for i in range(n-1,-1,-1):
        last = l1[m-1]
        j = m-2
        while(j>= 0  and l1[j] > l2[i]):
            l1[j+1] = l1[j]
            j -= 1

        if(j != m -1 or last>l2[i]):
            l1[j+1] = l2[i]
            l2[i] = last

#Driver program
l1 = [1, 5, 9, 10, 15, 20]
l2 = [2, 3, 8, 13]
m = len(l1)
n = len(l2)

merge(l1, l2, m, n)

print("After Merging \nFirst Array:", end="")
for i in range(m):
    print(l1[i] , " ", end="")

print("\nSecond Array: ", end="")
for i in range(n):
    print(l2[i] , " ", end="")
