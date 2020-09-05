arr1 = list(map(lambda x: int(x), input().split(' ')))
arr2 = list(map(lambda x: int(x), input().split(' ')))

alen1 = arr1[0]
alen2 = arr2[0]
if alen1 == 0 and alen2 == 0:
    print(0)

a, b = 1, 1
count = alen1 + alen2
print(count,end=" ")

while a <= alen1 and b <= alen2:
    if alen1 != 0 and alen2 != 0:
        if arr1[a] <= arr2[b]:
            print(arr1[a],end=" ")
            a += 1
        else:
            print(arr2[b],end=" ")
            b += 1
    elif alen1 != 0 and alen2 == 0:
        print(arr1[a],end=" ")
        a += 1
    else:
        print(arr2[b],end=" ")
        b += 1

if a <= alen1:
    for x in arr1[a:]:
        print(x,end=" ")
if b <= alen2:
    for i in arr2[b:]:
        print(i,end=" ")
