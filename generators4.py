a, b = int(input('Beginning: ' )), int(input('End: '))
def squares(n1, n2):
    for i in range(n1, n2+1):
        yield i**2
print(list(squares(a, b)))