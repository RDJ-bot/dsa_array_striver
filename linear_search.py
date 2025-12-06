arr = [1,2,3,4,54,5,87,5,4,110,111]
target = 110
count = 0

for i in arr:
    if(i == target):
        count = 1
        break

if(count):
    print("Found")
else:
    print("Not Found")


def linear_search(arr,target):
    for i in arr:
        if(i == target):
            return True
    return False

print(linear_search([1,2,3,4,5],9))