import matplotlib.pyplot as plt
from random_walk import RandomWalk

#hace camino aleatorio, sigue generando mientras el programa este activo
while True:

    rw = RandomWalk(50_000)   #clase que toma las decisiones sobre la direccion del camino
    rw.fill_walk()      #rellena el camino con puntos

    #traza los puntos del camino
    plt.style.use('classic')    #escoge el estilo del punto
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)    #generamos una lista de numeros igual a los puntos del camino

    #pasamos point_numbers al argumento 'c', usamos el mapa de color 'Blues'y quitamos el contorno negro de cada punto
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)  #coordenadas y tamaño de cada punto 
    
    #enfatiza el primer y el ultimo punto
    ax.scatter(0, 0, c='green', edgecolor='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=1)

    #elimina los ejes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()      #abre el visor de matplotlib y muestra el trazado

    keep_running = input("Make another walk? (y/n): ")  #pregunta para continuar o salir
    if keep_running == 'n':
        break
    
