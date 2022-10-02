
# Program to count the non-repeating number in a word.

st = "geeksforeeks"
arr = {}
for i in range(len(st)):
    if (st[i] not in arr):
        arr[st[i]] = 1
    else:
        arr[st[i]] += 1

count = 0
for i in arr:
    if (arr[i] == 1):
        count += 1

print(count)



