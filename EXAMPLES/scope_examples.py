x = 42  # global variable


def function_a():
    y = 5  # local variable to function_a(), or nonlocal to function_b()
    print(f"{y = }")
    print(f"{x = }")

    return 42    

f = function_a()  # calling function_a, which returns function_b

print(f"{f = }")
