# program to print n natural even number in reverse order.

n = int(input("enter number of term to be print \t"))

for j in range(n * 2 + 1, 1, -1):
    if (j % 2 == 0):
        print(j,end=" ")
