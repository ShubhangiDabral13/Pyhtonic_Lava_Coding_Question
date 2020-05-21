import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):

    hash_table = {}
    for i in s1:
        if hash_table.get(i) is None:
            hash_table[i] = 1
        else:
            hash_table[i] += 1


    for j in s2:

        if hash_table.get(j) != None:
            return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
