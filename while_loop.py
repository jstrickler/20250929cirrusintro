i = 0
while i < 3:
    print(i)
    i += 1

while True:
    name = input("What is your name? ")
    if name == 'q':
        break   # exit the loop
    if name == '':
        continue  # go back to top
    print(f"Welcome, {name}")