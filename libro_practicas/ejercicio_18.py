#ordenar lista de tuplas en ascesdente por el segundo elemento

L = [("Manzana", 15), ("Banana", 8), ("Fresa", 12), ("Kiwi", 9), ("Melocoton", 2)]

L.sort(key = lambda x : x[1])
print(L)
