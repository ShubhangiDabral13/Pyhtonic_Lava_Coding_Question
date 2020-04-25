"""
Floyd’s triangle is a triangle with first natural numbers.
"""

def floyd(n):
    val = 1
    for i in range(0,n):

        for j in range(0,i):

            print(val,end =" ")
            val += 1
        print()

n = int(input("Enter the number whose floyd triangle you want to print"))
floyd(n)
