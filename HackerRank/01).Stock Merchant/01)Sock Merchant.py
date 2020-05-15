import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    count = 0
    hashtable = {}

    for i in range(n):

        if hashtable.get(ar[i]) != None:
            hashtable[ar[i]] += 1

        else:
            hashtable[ar[i]]  = 1

    for i in hashtable:
        if hashtable[i] > 1:
            count =  count + hashtable[i] // 2

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
