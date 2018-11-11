import numpy as np
import matplotlib.pyplot as plt

# tengo la tabla guardada en un txt  (tablita.txt) separada por tabulaciones. Cambié comas por puntos.

#importo columna de x como array
x = np.loadtxt('tablita.txt', usecols= 0)
#importo columna de y como array
y = np.loadtxt('tablita.txt', usecols = 1)

#mostrar el scatter básico, se pueden tocar los parámetros
plt.scatter(x, y)
plt.show()

#hacer una regresión lineal primero, polyfit me devuelve los coeficientes, primero el de mayor orden (x)
# guardo en las variables m (mx) y b
m, b = np.polyfit(x, y, 1)

#plotear la regresión, (checkear que esté bien)
# plt.plot(x, m * x + b)
# plt.show()

#hacer las dos cosas juntas
plt.scatter(x, y)
plt.plot(x, m * x + b)
plt.xlabel('Tiempo')
plt.ylabel('Cositas')
# hacer labels para datos
#plt.
plt.show()

#ver bien los fits polinómicos. hacer alguno de otro orden

#Ej polinomio (rústico)
#generar los puntos en x y la función en y
#x = np.linspace(-10,10)
#y =  (x ** 3) + (x ** 2) - 4 * x + 4
#graficar el polinomio
#plt.plot(x, y)
#plt.xlabel('x')
#plt.ylabel('f(x)')
#plt.grid(True, 'major', 'both')

# genero el polinomio con numpy
poly = np.poly1d([1, 1, -4, 4])
# genero los puntos en x
# opcion
# x = np.linspace(-10,10)
x = np.arange(-10, 10, 0.1)
# genero el gráfico directamente ploteando x y el poly(x)
#plt.plot(x, poly(x))
# genero la derivada
deriv = np.polyder(poly)

#graficar
plt.plot(x, poly(x), color = 'red')
plt.plot(x, deriv(x), color = 'green')
plt.title('f(x) y su derivada')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, 'major', 'both')
plt.show()

#evaluar la funcion a x en los puntos pedidos
y = poly(x)

#generar archivo y guardar (y cerrar)
f_out = open('datagen.txt', 'w')
np.savetxt(f_out, y, fmt= '%f', delimiter= '/t', header= 'f(x)')
f_out.close()



