arr=[2,4,6,8,9]
temp = 0
print("Elements of array:- ")
for x in range(0, len(arr)):
    print(arr[x], end=" ")
for x in range(0, len(arr)):
    for y in range(x+1, len(arr)):
        if(arr[x] > arr[y]):
            temp = arr[x]
            arr[x] = arr[y]
            arr[y] = temp
print()
print("Elements of array in ascending order:- ")
for x in range(0, len(arr)):
    print(arr[x], end=" ")

for x in range(0, len(arr)):
    for y in range(x+1, len(arr)):
        if(arr[x] < arr[y]):
            temp = arr[x]
            arr[x] = arr[y]
            arr[y] = temp
print("\nElements of array in descending order:- ")
for x in range(0, len(arr)):
    print(arr[x],end=" ")
