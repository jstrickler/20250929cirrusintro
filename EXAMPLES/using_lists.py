colors = []   # empty list
items = list()  # empty list

cities = ['Portland', 'Pittsburgh', 'Peoria']  # , 55, ('a', 'b'), [1, 2, 3]]
print(f"cities: {cities}\n")

cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)
x = [cities, more_cities]   # x[0][2]
print(f"cities: {cities}\n")

cities[0] = "Milwaukee"
# LIST.append(obj) LIST.insert(idx, obj) LIST.extend(iterable)

del cities[3]

print(f"cities: {cities}\n")

cities.remove('Buffalo')
print(f"cities: {cities}\n")

city = cities.pop(len(cities)-1)
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3) 
print(f"city: {city}")
print(f"cities: {cities}\n")

# del LIST[idx]  LIST.remove(value) LIST.pop() LIST.pop(idx)    