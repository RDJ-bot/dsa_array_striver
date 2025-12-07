arr = [1,1,0,1,1,1,0,1,1]
n = len(arr)

count = 0
max = 0

for i in range(n):
    if(arr[i] == 1):
        count += 1
        if(count > max):
            max = count
    else:
        count = 0

print(max)