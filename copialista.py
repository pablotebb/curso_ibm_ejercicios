la = [1, 2, 3]

# copiamos la lista 
lb = la[:]
lc = list(la)

la[2] = 'z'

print(la)
# [1, 2, 'z']
print(lb)
# [1, 2, 3]
print(lc)
# [1, 2, 3]



