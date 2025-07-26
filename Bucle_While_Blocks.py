blocks = int(input("Ingresa el Numero de Bloques: "))
i=0
altura = 0
while i< blocks:
    i+=1
    altura+=1
    blocks -= i
print("La Altura de la piramide es : " , altura)
