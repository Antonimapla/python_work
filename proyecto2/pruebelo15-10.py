### matplotlib y plotly
import matplotlib.pyplot as plt
from plotly.graph_objs import Bar, Layout
from plotly import offline
from random import randint
from die import Die
from random_walk import RandomWalk

# crea dos dados de 6 caras
die_1 = Die(6)
die_2 = Die(6)

# tira 1000 veces los dados y guarda el resultado
results = []
results = [die_1.roll() + die_2.roll() for x in range(20)]   #uso la comprension
print(results)

fig, ax = plt.subplots()
ax.plot(results)

plt.show()

# camino aleatorio
rw = RandomWalk()
rw.fill_walk()

puntos = list(results)
tiradas = list(range(1, 20))

x = puntos
y = tiradas

# visualiza los resultados
x_values = list(range(2, 13))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1 }
y_axis_config = {'title': 'Frecuency of result'}
my_layout = Layout(title = 'Results of rolling two D6 dice 20 times',                           
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')

# define data


