from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#crea un d6
die = Die()
#hace algunas tiradas y guarda los resultados en una lista
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

    #analiza los resultados
    frequencies = []
    for value in range(1, die.num_sides+1):
        frequency = results.count(value)
        frequencies.append(frequency)
    
    #visualiza resultados
    x_values = list(range(1, die.num_sides+1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result'}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title='Results of rollingone D6 1000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
    
print(frequencies)