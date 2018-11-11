def primo(num):
    esPrimo = True
    if num == 1:
        esPrimo = False
    else:
        for i in range(2, num):
            if (num % i) == 0:
                esPrimo = False
    return esPrimo

def factores_primos(num):
    div = []
    for i in range(2, num + 1):
        if num % i == 0:
            if primo(i) and i not in div:
                div.append(i)
                num = int(num / i)
                factores_primos(num)
    return div

#esta versión es más lenta
def divisores_primos(num):
    div = []
    div_primos = []
    for i in range (1, num + 1):
        if num % i == 0:
            div.append(i)
    for i in div:
        if primo(i):
            div_primos.append(i)
    return div_primos

# devolver el máximo

#TODO hacer con un while loop hasta el máximo. no for.

# este codigo anda joya, investigarlo. investigar propiedades de divisibilidad.
# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors

# este funciona abajo, ver numeros más grandes, itera en vez de ir a el rango.
# def factores_primos(num):
#     div = []
#     a = 2
#     while a < num:
#         if num % a == 0:
#             if ej4.primo(a):
#                 div.append(a)
#                 num = int(num / a)
#                 factores_primos(num)
#         else:
#             a += 1
#     return div


# def factores_primos(num):
#     divis = []
#     resto = 0
#     for i in range (2, num + 1):
#         if (num % i) == 0 and primo(i):
#             divis.append(i)
#             resto = int(num / i)
#             break
#     while resto > 1:
#         for i in range(2, resto + 1):
#             if (resto % i) == 0 and primo(resto):
#                 divis.append(resto)
#                 resto = int(resto / i)
#                 break
#     print(divis)
#
# factores_primos(24)
# divis = []
# resto = 0
# for i in range(2, 6):
#     if (6 % i) == 0 and primo(i):
#         divis.append(i)
#         resto = int(6 / i)
#         break
# if resto > 1:
#     for i in range(2, resto):
#         if (resto % i) == 0 and primo(i):
#             divis.append(i)
#             resto = int(resto / i)
#             break
# print(divis)