"""
To swap number without using 3rd number
"""

def swap(s1,s2):
    s1 = s1 + s2
    s2 = s1 - s2
    s1 = s1 - s2
    print("s1 is now {}".format(s1))
    print("s2 is now {}".format(s2))

s1 = 10
s2 = 5
swap(s1,s2)
