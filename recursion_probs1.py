def num_print(i):
    if(i<1):
        return
    num_print(i-1)
    print(i)
num_print(3)


def rev_print(i,n):
    if(i>n):
        return
    rev_print(i+1,n)
    print(i)
rev_print(1,3)



# sum of first n numbers
def sum_of_numbers(i,sum):
    if(i < 1):
        print(sum)
        return
    sum_of_numbers(i-1,sum+i)
sum_of_numbers(3,0)