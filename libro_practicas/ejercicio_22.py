# truncar un numero decimal a dos cifras despues de la coma

numero = str(input("Introduzca un numero con varios decimales: "))

num = numero.split(",")

num2 = num[1]

result = num[0]+","+num2[0]+num2[1]

print(result)
