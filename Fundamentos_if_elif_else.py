year = int(input("Ingrese el Año que desea Validar: "))

if year > 1582:
    if year % 4 != 0:
        print("Es Un Año Comun")
    elif year % 100 != 0:
        print("Es Un Año Bisiesto")
    elif year % 400 != 0:
        print("Es Un Año Comun")
    else:
        print("Es un Año Bisiesto")
else:
    print("No esta dentro del periodo del calendario Gregoriano")