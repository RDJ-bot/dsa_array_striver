# # left rotate an array by one place
# # optimal
# arr = [1,2,3,4,5]
# f = arr[0]
# n = len(arr)
# for i in range(n-1):
#     arr[i] = arr[i+1]
# arr.append(f)
# print(arr)


# # left rotate an array by D places
# #brute force approach
# arr = [1,2,3,4,5,6,7]
# k = 3
# n = len(arr)
# k = k%n
# for i in range(k):
#     temp = arr[0]
#     for j in range(n-1):
#         arr[j] = arr[j+1]
#     arr[n-1] = temp
# print(arr)

# #better
# arr = [1,2,3,4,5,6,7]
# n = len(arr)
# d = 3
# d = d%n
# temp = arr[0:3]
# for i in range(d,n):
#     arr[i-d] = arr[i]
# for j in range(n-d,n):
#     arr[j] = temp[j-(n-d)]
# print(arr)

# #optimal
# arr = [1,2,3,4,5,6,7]
# n = len(arr)
# d = 3
# arr[:d] = arr[:d][::-1]
# arr[d:] = arr[d:][::-1]
# arr[:] = arr[:][::-1]
# print(arr)

# Move zeros to the end of the array
#brute force
# arr = [1,0,2,3,0,0,4,5]
# temp = []
# n = len(arr)

# for i in range(n):
#     if(arr[i] != 0):
#         temp.append(arr[i])

# for i in range(len(temp)):
#     arr[i] = temp[i]

# for i in range(len(temp),len(arr)):
#     arr[i] = 0
# print(arr)

# #optimal
# arr = [1,0,2,0,0,3,0,4,5]
# n = len(arr)
# j = -1
# for i in range(n):
#     if(arr[i] == 0):
#         j = i
#         break
# for i in range(j+1,n):
#     if(arr[i] != 0):
#         arr[i],arr[j] = arr[j],arr[i]
#         j += 1
# print(arr)

# #Linear Search
# arr = [1,5,7,3,9,7]
# target = 10
# flag = False
# for i in range(len(arr)):
#     if(arr[i] == target):
#         flag = True
# if(flag):
#     print("Found")
# else:
#     print("Not")


arr = [1,1,2,3,4,5]
arr1 = [2,3,4,4,5]
temp = []
for i in arr:
    if(i not in temp):
        temp.append(i)
for j in arr1:
    if(i not in temp):
        temp.append(i)
print(temp)