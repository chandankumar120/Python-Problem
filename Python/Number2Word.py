l1 = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
    'Nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen'
]
l2 = [
    '', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy',
    'eighty', 'ninety'
]

l3 = ""


def number(n):

    if n < 20:
        l3 = l1[n]
    if n < 100 and n >= 20:
        l3 = l2[n // 10] + " " + l1[n % 10]
    if n < 1000 and n >= 100:
        l3 = l1[n // 100] + " hundred " + number(n % 100)
    if n < 10000 and n >= 1000:
        l3 = l1[n // 1000] + " thousand " + number(n % 1000)
    return l3


num = int(input("enter number upto four digit\t"))
if num > 9999:
    print("Number greater than four digit not supported")
else:
    print(number(num))