fibo = [0, 1]
suma = 0
while (len(fibo) < 1000000):
    termino = (fibo[-2] + fibo[-1])
    fibo.append(termino)
for i in fibo:
    if (fibo.index(i) < 1000000) and (fibo.index(i) % 2 != 0):
        suma += fibo.index(i)
print(suma)
# esto me come toda la memoria porque son un millon de posiciones.


# fibo = [(1,1), (2,2)]
# suma = 0
#
# while (fibo[-1][0]) < 30:
#     termino = ((fibo[-1][0] + 1), (fibo[-1][1] + fibo[-2][1]))
#     fibo.append(termino)
#
# for elem in fibo:
#     if elem[0] % 2 != 0:
#         suma += i[1]
# print(suma)


# fibo = [0,1,2] / fibo = [0,1]
# suma = 0
# while fibo[-2] + fibo[-1] < 1000000:
#     termino = (fibo[-2] + fibo[-1])
#     fibo.append(termino)
# for i in fibo:
#     if i % 2 != 0:
#         suma += i
# print(suma)
#  esto suma los números impares, yo quiero sumar los términos impares
# entregar esto, cuando lo corro como codigo en la consola i me da el otro número. averiguar que pija hice
# hacer la serie de 0,1






