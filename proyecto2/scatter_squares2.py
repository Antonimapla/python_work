import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8-colorblind')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)            #traza un solo punto

##establece el titulo del grafico y las etiquetas de los ejes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

#establece el tamaño de los puntos de los ejes
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()