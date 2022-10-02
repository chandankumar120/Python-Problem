# Program to print n number of prime number

num = int(input("enter number of prime number to be find\t "))

count=0
i=2
while(True):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count+=1
            print(i)
    i=i+1
    if count==num:
        break
            