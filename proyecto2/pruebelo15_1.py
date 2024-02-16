import matplotlib.pyplot as plt

x_values = range(1, 5000)
y_values = [x*x*x for x in x_values]

plt.style.use('seaborn-v0_8-colorblind')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#establece el titulo del grafico y las etiquetas de los ejes
ax.set_title("Cube numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of value", fontsize=14)

ax.axis([0, 5000, 0, 55550000000])

plt.show()

