#brute
arr = [1,2,0,4,0,5,1,0,3]
n = len(arr)

#inserting non-zero elements to the temp array
temp = []
for i in arr:
    if(i != 0):
        temp.append(i)

x = len(temp)
for i in range(x):
    arr[i] = temp[i]

for i in range(x,n):
    arr[i] = 0
print(arr)


#optimal
arr = [1,0,2,3,4,0,5,0,6]
n = len(arr)

j = -1
for i in range(n):
    if(arr[i] == 0):
        j = i
        break

for i in range(j+1,n):
    if(arr[i] != 0):
        arr[i],arr[j] = arr[j],arr[i]
        j += 1
print(arr)