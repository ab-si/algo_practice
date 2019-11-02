#!/bin/python3

def sum_square(n):
    j=n*(n+1)*(2*n+1)//6
    m=n*(n+1)//2
    m=m*m
    print(m - j)

if if __name__ == "__main__":
    '''
    Find the absolute difference between the sum of the squares of the first N natural numbers
    and the square of the sum.
    '''
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        sum_square(n)