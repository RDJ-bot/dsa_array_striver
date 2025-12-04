#find the number of unique elements
arr = [1,2,4,4,3,3,5]
n = len(arr)
i = 0
for j in range(1,n):
    if(arr[j] != arr[i]):
        arr[i+1] = arr[j]
        i += 1
print(i+1)
print(arr)