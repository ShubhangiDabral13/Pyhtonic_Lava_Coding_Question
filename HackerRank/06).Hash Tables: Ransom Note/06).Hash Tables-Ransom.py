import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    hash_words = {}
    for m_word in magazine:

        if hash_words.get(m_word) == None:
            hash_words[m_word] = 1
        else:
            hash_words[m_word] += 1


    # Check if exist the word in the hash table
    for r_word in note:
        if hash_words.get(r_word) is None or hash_words[r_word] == 0:

            print("No")
            return
        else:
            hash_words[r_word] -= 1

    print("Yes")
    

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
