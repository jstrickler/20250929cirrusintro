d1 = {}  # best practice
d2 = dict()  # slightly less good

d3 = {'spam': 22, 'ham': 5, 'eggs': 13}
d3['toast'] = 89
d3['marmalade'] = 1
d3['dhosa'] = 14
d3['toast'] = 126
print(f"{d3 = }")
print(f"{d3['ham'] = }")
d3['dhosa'] = 380283
print(f"{d3 = }")

key = 'waffle'
# print(f"{d3[key] = }")
print(f"{key in d3 = }")

print(f"{d3.get(key) = }")
print(f"{d3.get(key, 0) = }")

print(f"{d3.setdefault(key, 109) = }")
print(f"{d3 = }")


for key, num in d3.items():
    print(key, num)

print(f"{d3.keys() = }")



