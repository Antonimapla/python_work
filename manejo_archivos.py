from io import open

archivo_texto = open("archivo.txt", "a")
"""
# frase = "Estupendo dia para estudiar python \n el miercoles"
# archivo_texto.write(frase)
# archivo_texto.close()

texto = archivo_texto.read()
archivo_texto.close()
print(texto)

lineas_texto = archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto[1])
"""
archivo_texto.write("\n siempre es una buena ocasion para estudiar python.")
archivo_texto.close()
