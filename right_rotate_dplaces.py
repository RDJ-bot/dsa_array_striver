arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
d = 3
d = d%n

arr[0:n-d] = arr[0:n-d][::-1]
arr[n-d:n] = arr[n-d:n][::-1]
arr[:] = arr[::-1]

print(arr)