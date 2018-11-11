a = list(range(1000))
suma = 0
for i in a:
    if (i % 3 == 0) or (i % 5 == 0):
        suma += i
print(suma)