import matplotlib.pyplot as plt

from random_walk import RandomWalk

#sigue generando caminos nuevos mientras el programa este activo
#hace un camino aleatorio
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    #traza los puntos del camino
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=5)
        
    #enfatiza el primer y el ultimo punto
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    #elimina los ejes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
