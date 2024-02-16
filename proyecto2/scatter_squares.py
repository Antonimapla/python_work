import matplotlib.pyplot as plt

x_values = range(1, 1001)               #valores para los puntos del grafico
y_values = [x**2 for x in x_values]     # "   "  comprension de lista  " "

plt.style.use('seaborn-v0_8-colorblind')    #damos estilo al grafico
fig, ax = plt.subplots()    #funcion que genera los trazos
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)   #coordenadas para un punto, tamaño del punto y color

#establece el titulo del grafico y las etiquetas de los ejes
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

#establece el tamaño de las etiquetas de los puntos de los ejes
ax.tick_params(axis='both', which='major', labelsize=14)

#establece el rango para cada eje
ax.axis([0, 1100, 0, 1100000])      #especificamos el rango de cada eje

plt.show()      #abre el visor de matplotlib y muestra el trazado
