# Función con return
def lista_con_return():
    return [1, 2, 3]

# Función con yield
def lista_con_yield():
    yield 1
    yield 2
    yield 3

# Usando la función con return
#print("Con return:")
#print()
#for numero in lista_con_return():
#    print(numero)

# Usando la función con yield
print("Con yield:")
for numero in lista_con_yield():
    print(numero)