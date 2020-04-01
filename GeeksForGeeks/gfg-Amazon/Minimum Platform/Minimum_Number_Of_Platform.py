def min_platform(ar,de,n):
    ar.sort()
    de.sort()
    result = 1
    platform_needed = 1
    i =1
    j  =0
    while(i<n and j<n):
        if(ar[i]<de[j]):
            platform_needed += 1
            i += 1

            if platform_needed > result:
                result = platform_needed

        else:
            platform_needed -= 1
            j += 1

    return result

#main Program
ar = [900, 940, 950, 1100, 1500, 1800]
de = [910, 1200, 1120, 1130, 1900, 2000]
n = len(ar)

print("Minimum Number of Platforms Required = ",
        min_platform(ar, de, n))
