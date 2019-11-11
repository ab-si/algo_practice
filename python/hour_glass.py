#!/bin/python3

'''
Given a 6x6 2D array,
We define an hourglass in A to be a subset of values with indices falling
in this pattern in A's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in A

Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.
'''

def hour_glass(arr):
    res = []
    for x in range(0, 4):
        for y in range(0, 4):
            s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
            res.append(s)
    print(max(res))

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    hour_glass(arr)
