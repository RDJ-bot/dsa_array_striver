# #Find the missing element in an array
# #brute force
# arr = [1,2,3,5]
# n = 5
# for i in range(1,n):
#     flag = False
#     for j in range(n-1):
#         if(arr[j] == i):
#             flag = True
#             break
#     if(flag == False):
#         print(i)

# #better
# arr = [1,2,3,4,5,6,7,9]
# n = 9
# hash = [0]*(n+1)
# for i in range(n-1):
#     hash[arr[i]] += 1
# for i in range(1,n+1):
#     if(hash[i] == 0):
#         print(i)
#         break

# #optimal(sum)
# arr = [1,2,3,5]
# n = 5
# s = 0
# sum = (n*(n+1))//2
# for i in arr:
#     s += i
# print(sum-s)

#optimal (xor)
# arr = [1,2,3,5]
# n = 5

# xor = 0
# for i in range(n-1):
#     xor = arr[i] ^ (i+1)
# xor = xor^n
# print(xor)


# #find the max one's sequence
# #optimal
# arr = [1,1,0,1,1,1,1,0,1,0,1,1,1,1,1]
# n = len(arr)
# count = 0
# maxi = 0
# for i in range(n):
#     if(arr[i] == 1):
#         count += 1
#         maxi = max(maxi,count)
#     else:
#         count = 0
# print(maxi)



#find the number that appaears once
#brute force
arr = [1,1,2,3,3,4,4,5,5]
n = len(arr)
count =0
for i in range(n):
    count = 0
    for j in range(n):
        if(arr[i] == arr[j]):
            count += 1
    if(count == 1):
        print(arr[i])


#better
arr = [1,1,2,2,3,3,4,4,5,5,6,6,7,8,8,9,9]
n = len(arr)
#hash = [0]*(n+2)
maxi = arr[0]
for i in range(1,n):
    maxi = max(maxi,arr[i])
hash = [0]*(maxi+1)
for i in range(n):
    hash[arr[i]] += 1
for i in range(len(hash)):
    if(hash[i] == 1):
        print(i)

#optimal
arr = [1,1,2,3,3,4,4,5,5]
n = len(arr)
xor = 0
for i in range(n):
    xor = xor^arr[i]
print(xor)