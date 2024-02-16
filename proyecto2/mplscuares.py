import matplotlib.pyplot as plt

#valores base de calculo de los cuadrados
input_values = [1, 2, 3, 4, 5, 6, 7]

#lista de valores para el grafico
squares = [1, 4, 9, 16, 25, 36, 49]     #primeros numeros al cuadrado

#damos un estilo predefinido al grafico
plt.style.use('seaborn-v0_8-colorblind')

fig, ax = plt.subplots()        #funcion que genera el/los trazados en una misma figura
ax.plot(input_values, squares, linewidth=3)   #funcion que intentara trazar los datos que reciba,con ancho de linea

#establece el titulo del grafico y las etiquetas de los ejes
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

#establece el tamaño de las etiquetas de los puntos de los ejes
ax.tick_params(axis='both', labelsize=14)

plt.show()                        #abre el visor de matplotlib y muestra el trazado
