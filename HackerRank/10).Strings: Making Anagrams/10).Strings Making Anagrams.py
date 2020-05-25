#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):

    count1 = [0]*26
    count2 = [0]*26
    res = 0

    for i in range(len(a)):
        count1[ord(a[i]) - ord("a")] += 1
        i += 1



    for i in range(len(b)):
        count2[ord(b[i]) - ord("a")] += 1
        i += 1



    for i in range(26):
        res += abs(count1[i] - count2[i])


    return res



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
