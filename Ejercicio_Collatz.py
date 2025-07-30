c0 = int(input("Ingresa un Numero : "))

while c0>0:
    if c0 % 2 == 0:
        c0/=2
        print(c0)
    else:
        c0 = 3 * c0 + 1
    if c0 != 1:
        print(c0)
        continue