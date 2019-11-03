#!/bin/python3

def count(s, t, a, b, apple, orange):
    print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))

if __name__ == "__main__":
    '''
    Sam's house has an apple tree and an orange tree that yield an abundance of fruit.
    s is the start point, and t is the endpoint for the house.
    The apple tree is to the left of his house, and the orange tree is to its right.
    You can assume the trees are located on a single point, where the apple tree is at point a,
    and the orange tree is at point b.
    When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis.
    A negative value of d means the fruit fell d units to the tree's left,
    and a positive value of d means it falls d units to the tree's right.

    Given the value of d for m apples and n oranges, determine how many apples and oranges will fall on
    Sam's house (i.e., in the inclusive range s,t)?

    The first line contains two space-separated integers denoting the respective values of s and t.
    The second line contains two space-separated integers denoting the respective values of a and b.
    The third line contains two space-separated integers denoting the respective values of m and n.
    The fourth line contains  m space-separated integers denoting the respective distances that each apple falls from point a.
    The fifth line contains  space-separated integers denoting the respective distances that each orange falls from point b.
    '''
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()

    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    count(s, t, a, b, apples, oranges)