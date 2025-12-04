arr = [1,2,4,5,1]
n = len(arr)
count = 0
for i in range(1,n):
    if(arr[i-1]>arr[i]):
        count = 1
        break
if(count):
    print("Not sorted")
else:
    print("Sorted")