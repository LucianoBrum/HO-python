fibo = [0,1]
suma = 0
while fibo[-2] + fibo[-1] < 1000000:
    termino = (fibo[-2] + fibo[-1])
    fibo.append(termino)
for i in fibo:
    if i % 2 != 0:
        suma += i
print(suma)







