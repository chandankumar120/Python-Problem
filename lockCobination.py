# Create PIN using three given input numbers

# “Secure Assests Private Ltd”, a small company that deals with lockers has recently started manufacturing digital locks which can be locked and unlocked using PINs (passwords). You have been asked to work on the module that is expected to generate PINs using three input numbers.

# Assumptions : The three given input numbers will always consist of three digits each i.e. each of them will be in range >= 100 and <=999

# 100<=input1<=999

# 100<=input2<=999

# 100<=input3<=999

# Below are the rules for generating the PIN-

# -          The PIN should made up of 4 digits

# -          The unit(ones) position of the PIN should be the least of the units position of the three input numbers

# -          The tens position of the PIN should be the least of the tens position of the three input numbers

# -          The hundreds position of the PIN should be the least of the hundreds position of the three input numbers

# -          The thousands positions of the PIN should be the maximum of all the digits in the three numbers

# Example 1-

# Input1= 123

# Input2= 582

# Input3= 175

# Then PIN=8122

# Example 2-

# Input1= 190

# Input2=267

# Input3= 853

# Then, PIN=9150



num1 = 190
num2 = 267
num3 = 853


def min(a, b, c):
    min = a if a < b else b
    return min if min < c else c


def maximum(a, b, c):
    min = a if a > b else b
    return min if min > c else c


def max(num, greatest):

    if (num > greatest):
        greatest = num
    return greatest


result = ""
list = []
greatest1 = 0
greatest2 = 0
greatest3 = 0
while (num1 != 0):
    frem1 = num1 % 10
    num1 = num1 // 10
    greatest1 = max(frem1, greatest1)
    frem2 = num2 % 10
    num2 = num2 // 10
    greatest2 = max(frem2, greatest2)
    frem3 = num3 % 10
    num3 = num3 // 10
    greatest3 = max(frem3, greatest3)
    pin = min(frem1, frem2, frem3)
    result = str(pin) + result
great = maximum(greatest1, greatest2, greatest3)
print(str(great) + result)
