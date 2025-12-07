# in a given array, where each element appears twice
# find the number that appaers once

arr = [1,1,2,3,3,4,4]
n = len(arr)


for i in range(n):
    count = 0
    for j in range(n):
        if(arr[j] == arr[i]):
            count += 1
    if(count == 1):
        print(arr[i])
        break


#better

arr = [1,1,2,2,3,4,4]
n = len(arr)
m = arr[n-1]

hash = [0]*n
for i in range(n):
    hash[arr[i]] += 1

for i in range(1,n):
    if(hash[i] == 1):
        print(i)
        break

#optimal
arr = [1,1,2,3,3,4,4]
n = len(arr)
xor = 0
for i in range(n):
    xor = xor^arr[i]
print(xor)