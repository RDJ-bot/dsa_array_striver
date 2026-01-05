#Brute force approach {TC : O(N^4) and SC : 2(O(quads))}

arr = [1,0,-1,0,-2,2]
n = len(arr)
s = set()

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            for l in range(k+1,n):
                if(arr[i] + arr[j] + arr[k] + arr[l] == 0):
                    temp = [arr[i],arr[j],arr[k],arr[l]]
                    temp.sort()
                    s.add(tuple(temp))
print(s)


#Better solution {TC : O(N^3) and SC : O(N) + 2 O(quads)}
arr = [1,0,-1,-2,2,0]
n = len(arr)
ans = set()
target = 0

for i in range(n):
    for j in range(i+1,n):
        s = set()
        for k in range(j+1,n):
            l = target - (arr[i] + arr[j] + arr[k])
            if(l in s):
                temp = [arr[i],arr[j],arr[k],l]
                temp.sort()
                ans.add(tuple(temp))
            s.add(arr[k])

print(ans)


#optimal {TC : O(N^3) and SC : O(no.of.quads)}
arr = [1,1,1,2,2,2,3,3,3,4,4,4,5,5]
arr.sort()
n = len(arr)
ans = set()
target = 8

for i in range(n):
    if(i>0 and arr[i] == arr[i-1]):
        continue
    for j in range(i+1,n):
        if(j != i+1 and arr[j] == arr[j-1]):
            continue

        left = j+1
        right = n-1

        while(right > left):
            sums = arr[i]+arr[j]+arr[left]+arr[right]
            if(sums == target):  
                temp = [arr[i],arr[j],arr[left],arr[right]]
                ans.add(tuple(temp))
                left += 1
                right -= 1
                
                while(right > left and arr[right] == arr[right - 1]):
                    right -= 1
                while(right > left and arr[left] == arr[left - 1]):
                    left += 1

            elif(sums > target):
                right -= 1
            else:
                left += 1
print(ans)