import sys
import geometry  # find and execute geometry.py

print(f"{geometry.PI = }")


circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{square = }")

# 1. current folder
# 2. folders in PYTHONPATH (if it exists)
# 3. predefined location (sys.prefix)
print(f"{sys.prefix = }")

for path in sys.path:
    print(path)

