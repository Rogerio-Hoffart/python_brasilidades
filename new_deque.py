from collections import deque

valores_cache = deque(maxlen=3)

def cache(func):
    def passa_cache(*args):
        valores_cache.append(args)
        return func(*args)
    return passa_cache


@cache
def soma(*args):
    resultado = 0
    for r in args:
        resultado += r
    return resultado

print(soma(1, 2, 3))
print(soma(4, 5, 6))
print(soma(7, 8, 9))

print(valores_cache)

print(soma(1, 1, 1))

print(valores_cache)

print(soma(1, 2, 3, 4, 5))

print(valores_cache)