def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1, 11):
    print(i, ":", fibonacci(i))


cache = {}

def fib(n):
    if n in cache:
        return cache[n]

    if n == 1 or n == 2:
        value = 1
    else:
        value = fib(n-1) + fib(n-2)

    cache[n] = value
    return value

for i in range(1, 21):
    print(i, ":", fib(i))


from functools import lru_cache

@lru_cache(maxsize=1000)
def fib3(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib3(n-1) + fib3(n-2)

for i in range(1, 21):
    print(i, ":", fib3(i))

print("\n-----------------------\n")

def TowerOfHanoi(n, source, destination_rod, auxilliary_rod):
    if n == 1:
        print("Move disk 1 from source", source, " to destination ", destination_rod)
        return
    TowerOfHanoi(n-1, source, auxilliary_rod, destination_rod)
    print("Move disk ", n, "from source ", source, "to destination ", destination_rod)
    TowerOfHanoi(n-1, auxilliary_rod, destination_rod, source)

n = 5
TowerOfHanoi(n, 'A', 'B', 'C')
