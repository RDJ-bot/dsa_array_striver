#brute
arr = [1,2,4,5]
n = len(arr)

for i in range(1,n+1):
    flag = 0
    for j in range(n):
        if(arr[j] == i):
            flag = 1
            break

    if(flag == 0):
        print(i)


#better
arr = [1, 2, 3, 5]
n = len(arr)

hash = [0] * (n + 2)

for i in range(n):          # 0 to n-1
    hash[arr[i]] = 1        # mark presence

for i in range(1, n + 1):
    if hash[i] == 0:
        print(i)

#optimal

arr = [1,2,3,4,5,6,7,8,10]
n = len(arr)+1

sum = (n*(n+1))//2
add = 0
for i in range(n-1):
    add += arr[i]

print("Missing Number : ",sum-add)