def sub_arr_sum(arr,sum):
    n = len(arr)

    # Initialize curr_sum as value of first element and starting point as 0
    curr_sum = arr[0]
    start = 0

    # Add elements one by one to curr_sum and if the curr_sum exceeds  the sum, then remove starting element.
    i = 1
    while i < n-1:

        # If curr_sum exceeds the sum, then remove the starting elements
        while curr_sum > sum and start < i-1:
            curr_sum = curr_sum - arr[start]
            start += 1

        # If curr_sum becomes equal to sum, then return true
        if curr_sum  == sum:
            print("The subarray whose sum is {} is from index {} to {}".format(sum,start,i-1))

        # Add this element to curr_sum
        if i<n :
            curr_sum = curr_sum + arr[i]
            i += 1

# Driver program
arr = [15, 2, 4, 8, 9, 5, 10, 23]
sum = 23
sub_arr_sum(arr,sum)
