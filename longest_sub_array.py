#brute force O(n^3)
arr = [1,2,3,1,1,1,4,2,3]
n = len(arr)
sums = 0
maxi = 0
target = 3
for i in range(n):
    for j in range(i,n):
        sums = 0
        for k in range(i,j+1):
            sums += arr[k]
        if(sums == target):
            maxi = max(maxi,j-i+1)
print(maxi)

#O(n^2)
arr = [1,2,3,1,1,1,4,2,3]
n = len(arr)
k = 3
sums = 0
maxi = 0
for i in range(n):
    sums = 0
    for j in range(i,n):
        sums += arr[j]
        if(sums == k):
            maxi = max(maxi,j-i+1)
print(maxi)

#optimal
arr = [1,2,3,1,1,1,4,2,3]
n = len(arr)
target = 3
left = 0
sums = 0
maxi = 0

for right in range(n):
    sums += arr[right]
    if(sums == target):
        maxi = max(maxi,right-left+1)
    while sums > k:
        sums -= arr[left]
        left += 1
print(maxi)