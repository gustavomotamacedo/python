t1 = 1
t2 = 1
t3 = 0
cont = 2

print('{}, {}, ' .format(t1, t2))
while cont < 10:
    t3 = t1 + t2
    print('{}, ' .format(t3))
    t1 = t2
    t2 = t3
    cont += 1
