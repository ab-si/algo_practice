#!/bin/python3

def min_swap(arr):
    count = 0
    n = len(arr)
    arr_dict = {}
    for index, ele in enumerate(arr):
        arr_dict[ele] = index
    visited = [False]*n

    for ele, index in sorted(arr_dict.items(), key=lambda x: x[0]):
        print(ele, index)
        if visited[index] or ele == index:
            continue
        cycle_count = 0
        i = ele
        while not visited[i]:
            visited[i] = True
            i = arr_dict[i]
            cycle_count += 1
            print(cycle_count)
        count += cycle_count - 1
    print(count)

if __name__ == "__main__":
    '''
    Find the number of minimum swaps required for sorting an array
    The array contains n consecutive numbers in [0,n]
    '''
    arr = [1,3,4,0,2]
    min_swap(arr)