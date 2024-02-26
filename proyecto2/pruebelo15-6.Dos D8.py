from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# crea dos dados de 8 caras
die_1 = Die(8)
die_2 = Die(8)

# tira 1000 veces los dados y guarda el resultado
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analiza los resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualiza loa resultados
x_values = list(range(2, max_result + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1 }
y_axis_config = {'title': 'Frecuency of result'}
my_layout = Layout(title = 'Results of rolling two D8 dice 1000 times',                           
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
