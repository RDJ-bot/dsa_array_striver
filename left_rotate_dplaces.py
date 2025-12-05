#brute
arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
d = 2

#temp array
temp = []
for i in range(d):
    temp.append(arr[i])

#rotation
for i in range(n-d):
    arr[i] = arr[i+d]

#adding temp
for i in range(d):
    arr[(n-d)+i] = temp[i]

print(arr)



#optimal
arr = [1,2,3,4,5]
d = 3
n = len(arr)

arr[0:d] = arr[0:d][::-1]
arr[d:n] = arr[d:n][::-1]
arr[::] = arr[::-1]
print(arr)  