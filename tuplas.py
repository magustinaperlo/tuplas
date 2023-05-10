preciomaximo= 2000
marcaespecifica= "maped"

productos = [("lapices",800,6,"simball"),("fibras",1100, 5, "FaberCastell"), ("goma de borrar",100, 20, "maped"), ("boligrafo", 220, 12, "maped")]


productos_dela_lista = []
for t in productos:
    if t [1] <= preciomaximo and t [3] == marcaespecifica:
        productos_dela_lista.append (t)
print (productos_dela_lista)

