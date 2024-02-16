import matplotlib.pyplot as plt

input_values=[1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('seaborn-v0_8-colorblind')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=8)

#establece el titulo del grafico y las etiquetas de los ejes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Values", fontsize=14)
#establece el tamaño de las etiquetas de los puntos de los ejes.
ax.tick_params(axis='both', labelsize=14)

plt.show()