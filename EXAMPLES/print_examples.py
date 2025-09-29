import sys

city = 'Orlando' 
temperature = 85
hit_count = 5
average = 3.4563892382

# print(str(city) + " " + str(temperature) + ...)
print(city, temperature, hit_count, average)
print()

print(city, end=' ')  # Print space instead of newline at the end
print(temperature)
print()

# Item separator is comma + space
sep = ", "
print(city, temperature, hit_count, average, sep=sep)
print()

# Item separator is empty string
print(city, temperature, hit_count, average, sep="")

print("HELP", file=sys.stderr, flush=True)


