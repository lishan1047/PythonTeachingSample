def Fibonacci(n):
    nl = [0, 1]
    for i in range(2, n):
        nl.append(nl[i - 1] + nl[i - 2])
    return nl

print(Fibonacci(5))
print(Fibonacci(8))