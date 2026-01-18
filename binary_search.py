arr = [1,2,3,4,5,6,7,8,9]
target = 8
flag = False

left = 0
right = (len(arr))-1

while left <= right:

    mid = (left+right) // 2
    
    if arr[mid] == target:
        ans = mid
        flag = True
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if(flag):
    print(ans)
else:
    print("No element found")