#1.2.1 Fibonacci nos
n = int(input("enter the value 15:"))
first_val = 0
second_val = 1
for i in range(0,n):
    if (i <= 1):
        next_num = i
    else:
        next_num = first_val + second_val
        first_val = second_val
        second_val = next_num
    print (next_num)