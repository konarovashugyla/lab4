from datetime import datetime
y1, m1, d1 =  [int(input()) for i in range(3)]
y2, m2, d2 =  [int(input()) for i in range(3)]
a = datetime(y1, m1, d1)
b = datetime(y2, m2, d2)
d = b - a
print(d.seconds + d.days * 86400)