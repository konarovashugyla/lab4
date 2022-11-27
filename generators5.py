number = int(input('Enter a number:' ))
def decrease(n):
    for i in range(n, -1, -1):
        yield i
print(list(decrease(number)))