# Add your code here:
def get_city_population(populations, city):
    # Verificamos si la ciudad existe en el diccionario que entra por parámetro
    if city in populations:
        return populations[city]
    else:
        # Si no existe, lanzamos la excepción que el sistema está esperando
        raise KeyError(f'City "{city}" not found in population data.')
city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}
city_name = "Tampa"
try:
    print(get_city_population(city_populations, city_name))
except KeyError:
    print("Key not found in dictionary.")
#print(get_city_population(city_populations, city_name))
    