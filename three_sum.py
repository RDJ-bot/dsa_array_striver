#Brute force approach  {TC : O(N^3) and SC : 2(O(unique triplets))}
arr = [-1,0,1,1,2,-1,1]
n = len(arr)
target = 0
temp = []
ans = set()
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if(arr[i] + arr[j] + arr[k] == target):
                temp = [arr[i],arr[j],arr[k]]
                temp.sort()
                ans.add(tuple(temp))
print(ans)


#better solution {TC : O(N^2 x log M)  SC : O(N) + 2(O(unique triplets))}
arr = [-1,0,1,1,2,-1,1]
n = len(arr)
ans = set()

for i in range(n):
    s = set()
    for j in range(i+1,n):
        k = -(arr[i] + arr[j])
        if(k in s):
            temp = [arr[i],arr[j],k]
            temp.sort()
            ans.add(tuple(temp))
        s.add(arr[j])
print(ans)



#optimal  {TC : O(NlogN) + O(N X N)}
arr = [1,1,1,0,0,0,-1,-1,-1,-2,-2,-2]
n = len(arr)
ans = []

for i in range(n):
    #skips if the arr[i] is dupe
    if(i>0 and arr[i] == arr[i-1]):
        continue
    
    #2 pointers
    left = i+1
    right = n-1

    while(left < right):
        sums = arr[i] + arr[left] + arr[right]
        
        if(sums > 0):
            right -= 1

        elif(sums < 0):
            left += 1

        else:
            ans.append([arr[i], arr[left], arr[right]])
            left += 1
            right -= 1

            while(left < right and arr[left] == arr[left-1]):
                left += 1
            
            while(left < right and arr[right] == arr[right+1]):
                right -= 1


print(ans)