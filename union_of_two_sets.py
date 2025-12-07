arr = [1,2,2,3,4,5,5]
n = len(arr)
arr1 = [1,4,5,6,6,6,4]
m = len(arr1)

s = set()
for i in arr:
    s.add(i)
for j in arr1:
    s.add(j)

union = []
for i in s:
    union.append(i)

print(union)