import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-colorblind')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)            #traza un solo punto

#establece el titulo del grafico y las etiquetas de los ejes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

#establece el tamaño de los puntos de los ejes
ax.tick_params(axis='both', which='major', labelsize=14)

#establece el rango para cada eje
ax.axis([0, 1100, 0, 1100000])

plt.show()