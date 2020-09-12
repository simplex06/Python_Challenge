# QUESTION:
# This is an interview question asked by Google.
# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# You can modify the input array in-place and you do not need to store the results. 
# You can simply print them out as you compute them.

def max_subarray(lst, k):
    lst_max_subarray = list()
    for i in range(len(lst)-(k-1)):
        lst_max_subarray.append(max(lst[i:i+k]))
    return lst_max_subarray

print(max_subarray([10, 5, 2, 7, 8, 7], 3))