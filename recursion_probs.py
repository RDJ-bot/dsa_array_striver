count = 0
def name_print(name):
    global count
    if(count == 3):
        return
    print(name)
    count += 1
    name_print(name)
name_print("Jeswin")


def num_print(i,n):
    if i > n:
        return
    print(i)
    num_print(i+1,n)
num_print(1,5)

print("\n")
def print_rev(n):
    print(n)
    if(n == 1):
        return
    print_rev(n-1)
print_rev(5)