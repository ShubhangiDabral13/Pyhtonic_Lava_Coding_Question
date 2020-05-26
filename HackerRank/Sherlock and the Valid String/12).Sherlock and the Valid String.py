#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):

    count_char = {}
    for i in s:

        if i in count_char:
            count_char[i] += 1
        else:
            count_char[i] = 1

    min_count = count_char[i]
    max_count = count_char[i]

    count_value = {}

    for char,value in count_char.items():

        if value in count_value:
            count_value[value] += 1

        else:
            count_value[value]  = 1

        if value < min_count:
            min_count = value

        if value > max_count:
            max_count = value



    if len(count_value) == 1:
        return "YES"

    elif len(count_value) == 2:

        if count_value[max_count] == 1 and max_count - min_count == 1:
            return "YES"

        if count_value[min_count] == 1 and  min_count == 1:
            return "YES"
        else:
            return "NO"

    else:
        return "NO"




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
