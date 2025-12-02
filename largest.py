#brute
arr = [5,7,3,1,2,5,9]
n = len(arr)
for i in range(n):
    min = i
    for j in range(i+1,n):
        if(arr[j]<arr[min]):
            min = j
    arr[min],arr[i] = arr[i],arr[min]
print(arr)

print("Largest Element of the array : ",arr[n-1])


#optimal
largest = arr[0]
for i in range(n):
    if(arr[i]>largest):
        largest = arr[i]
print(largest)
