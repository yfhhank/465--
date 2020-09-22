alen = list(map(lambda x: int(x), input().split(' ')))
arr = list(map(lambda x: int(x), input().split(' ')))
original = arr.copy()


def sort(arr):
    for i in range(len(arr)):
        minimun = min(arr[i:])
        min_index = arr[i:].index(minimun)
        arr[i + min_index] = arr[i]
        arr[i] = minimun


sort(arr)

sum = 0
for i in original:
    sum += arr.index(i)
    arr.remove(i)
print(sum)
