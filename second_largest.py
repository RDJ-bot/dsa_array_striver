#brute
arr = [1,2,3,6,3,2,4,7,7,8]
n = len(arr)
for i in range(n-1,0,-1):
    for j in range(i):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)

largest = arr[n-1]
for i in range(n-2,0,-1):
    if(arr[i] != largest):
        second_largest = arr[i]
        break
print(second_largest)

#better
largest = arr[0]
for i in range(n):
    if(arr[i]>largest):
        largest = arr[i]
second_largest = -1
for j in range(n):
    if(arr[j]<largest and arr[j]>second_largest):
        second_largest = arr[j]
print(second_largest)

#optimal
largest = arr[0]
second_largest = -1
for i in range(n):
    if(arr[i]>largest):
        second_largest = largest
        largest = arr[i]
print(second_largest)