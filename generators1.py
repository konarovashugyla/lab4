a = int(input('Give amount: '))
def squares(n):
    a = 1
    for i in range(n):
        yield a**2
        a+=1
print(list(squares(a)))