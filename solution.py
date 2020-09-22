alen = list(map(lambda x: int(x), input().split(' ')))
arr = list(map(lambda x: int(x), input().split(' ')))
original = arr.copy()

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        a = 0
        b = 0
        i = 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                arr[i] = left[a]
                a += 1
            else:
                arr[i] = right[b]
                b += 1
            i += 1
        while a < len(left):
            arr[i] = left[a]
            a += 1
            i += 1
        while b < len(right):
            arr[i] = right[b]
            b += 1
            i += 1

merge_sort(arr)

sum = 0
for i in original:
    sum += arr.index(i)
    arr.remove(i)
print(sum)
