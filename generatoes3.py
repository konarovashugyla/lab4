n = int(input('Give a number:'))
def evens(n):
    i = 1
    for i in range(n+1):
        if i%2==0:
            yield i
l = list(evens(n))
print(*l, sep=',')