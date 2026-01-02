#brute force approach O(N^3)
arr = [2,3,-2,4]
n = len(arr)
maxi = 0
product = 1
for i in range(n):
    for j in range(i+1,n):
        product = 1
        for k in range(i,j):
            product = product*arr[k]
        maxi = max(maxi,product)
print(maxi)

#O(N^2)
arr = [2,3,-2,4]
n = len(arr)
maxi = 0
product = 1

for i in range(n):
    product = 1
    for k in range(i,n):
        product = product*arr[k]
        maxi = max(maxi,product)

print(maxi)


# Optimal O(N)
arr = [2,3,-2,4,1,2]
n = len(arr)
prefix = 1
suffix = 1
maxi = 0
for i in range(n):
    if(prefix == 0):
        prefix = 1
    elif(suffix == 0):
        suffix = 1
    
    prefix = prefix*arr[i]
    suffix = suffix*arr[n-i-1]

    maxi = max(maxi,max(prefix,suffix))

print(maxi)