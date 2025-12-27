# brute force approach
arr = [0,1,2,0,1,2,1,0]
n = len(arr)
for i in range(n):
    mini = i
    for j in range(i+1,n):
        if(arr[mini] > arr[j]):
            mini = j
    arr[mini],arr[i] = arr[i],arr[mini]
print(arr)

#better
arr = [0,1,2,0,1,2,1,0]
n = len(arr)
c0 = 0
c1 = 0
c2 = 0
for i in range(n):
    if(arr[i] == 0):
        c0 += 1
    elif(arr[i] == 1):
        c1 += 1
    elif(arr[i] == 2):
        c2 += 1
for i in range(c0):
    arr[i] = 0
for j in range(c0,c0+c1):
    arr[j] = 1
for k in range(c0+c1,c0+c1+c2):
    arr[k] = 2
print(arr)

#optimal
#Dutch national flag algo
arr = [2,0,2,1,1,0]
low = 0
mid = 0
high = len(arr)-1

while mid <= high:

    if(arr[mid] == 0):
        arr[low],arr[mid] = arr[mid],arr[low]
        mid += 1
        low += 1
    
    elif(arr[mid] == 1):
        mid += 1
    
    elif(arr[mid] == 2):
        arr[mid],arr[high] = arr[high],arr[low]
        high -= 1

print(arr)