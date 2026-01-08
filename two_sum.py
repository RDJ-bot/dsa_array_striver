#brute force approach
arr = [2,5,8,11,6]
n = len(arr)
sums = 0
target = 14
flag = False
for i in range(n):
    for j in range(i+1,n):
        sums = arr[i] + arr[j]
        if(sums == target):
            flag = True
            print(arr[i] ,arr[j])
        if(flag):
            break
 
#better
arr = [2,5,8,11,6]
n = len(arr)
#arr.sort
target = 14
dic = dict()
for i in range(n):
    compliment = target - arr[i]
    if(compliment in dic):
        print(compliment,arr[i])
        break
    dic[arr[i]] = i

#optimal
arr = [2,5,8,11,6]
n = len(arr)
left = 0
right = n-1
target = 14
sums = 0

while right > left:
    sums = arr[left] + arr[right]
    if(sums == target):
        print(left, right)
        print(arr[left], arr[right])
        break
    elif(sums > target):
        right -= 1
    elif(sums < target):
        left += 1