#!/bin/python3

'''
Given an array of integers, find and print the minimum absolute difference between
any two elements in the array.
'''

def min_abs_diff(arr):
    arr = sorted(arr)
    return min(abs(x-y) for x,y in zip(arr,arr[1:]))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    result = min_abs_diff(arr)
    print(result)