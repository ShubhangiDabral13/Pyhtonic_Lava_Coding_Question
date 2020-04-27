"""
Given a number n, print all primes smaller than or equal to n.
Time complexity is O(N loglogN)
"""
def prime(n):

    pm = [True for i in range(n+1)]
    p = 2
    while(p*p <= n):

        if pm[p] == True:
            for i in range(p*p , n+1 , p):
                pm[i] = False
        p += 1

    for i in range(2,n+1):
        if pm[i]:
            print(i,end= " ")

n = int(input("Enter a number n, print all primes smaller than or equal to n."))
prime(n)
