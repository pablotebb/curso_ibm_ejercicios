# LISTAS DE COMPRESIÓN
# Definir la matriz m
m = [['a1', 'a2', 'a3'], ['b1','b2','b3'], ['c1', 'c2', 'c3']]

# Visualizar la matriz m
# for row in m:
#     print(row)
# Resultado visualizado:
# ['a1', 'a2', 'a3']
# ['b1', 'b2', 'b3']
# ['c1', 'c2', 'c3']

# Extraer el segundo elemento de cada fila en la matriz m
col2 = [row[1] for row in m]
print(col2)
# Resultado visualizado:
# ['a2', 'b2', 'c2']

# Extrae la diagonal de la matriz
col3 = [m[i][i] for i in [0, 1, 2]]
print(col3)
# Resultado visualizado:
# ['a1', 'b2', 'c3']

# Extraemos las longitudes de los elementos de m
col4 = [len(row) for row in m]
print(col4)
# [3, 3, 3]




