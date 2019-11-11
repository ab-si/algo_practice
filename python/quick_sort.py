'''
Implement quick sort
'''
def partition(arr, low, high):
    i = low-1
    pivot = arr[high]
    print("I : ", i)
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    print(arr)
    return (i+1)

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print("Pi : ", pi)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    quick_sort(arr, 0 ,len(arr)-1)