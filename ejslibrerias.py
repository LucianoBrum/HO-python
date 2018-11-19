import numpy as np
import matplotlib.pyplot as plt

# tengo la tabla guardada en un txt  (tablita.txt) separada por tabulaciones. Cambié comas por puntos.

#importo columna de x como array
x = np.loadtxt('tablita.txt', usecols= 0)
#importo columna de y como array
y = np.loadtxt('tablita.txt', usecols = 1)


#hacer una regresión lineal primero, polyfit me devuelve los coeficientes, primero el de mayor orden (x)
# guardo en las variables m (mx) y b
m, b = np.polyfit(x, y, 1)


# plotear el scatter
plt.scatter(x, y)
# agregar labels para los datos
for xy in zip(x, y):
    plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
# plotear regresión
plt.plot(x, m * x + b)
# agregar labels de ejes
plt.xlabel('Tiempo')
plt.ylabel('Cositas')
plt.show()


# genero el polinomio con numpy
poly = np.poly1d([1, 1, -4, 4])
# genero los puntos en x
x = np.arange(-10, 10, 0.1)
# genero la derivada
deriv = np.polyder(poly)

#evaluar la funcion a x en los puntos pedidos
y = poly(x)
#encontrar máximo y mínimo locales de la función en el rango dado.
max_rel = max(y)
min_rel = min(y)

#graficar el polinomio y su derivada
plt.plot(x, poly(x), color = 'red')
plt.plot(x, deriv(x), color = 'green')
#marcar máximo y mínimo en el gráfico
plt.plot(10, max_rel, 'b^')
plt.plot(-10, min_rel, 'bv')
plt.text(10, max_rel, 'max', fontsize= 15)
plt.text(-10, min_rel, 'min', fontsize= 15)
plt.title('f(x) y su derivada')
plt.xlabel('x')
plt.ylabel('f(x)')
#poner labels a f(x) y derivada.
plt.grid(True, 'major', 'both')
plt.show()



#generar archivo y guardar (y cerrar)
f_out = open('datagen.txt', 'w')
np.savetxt(f_out, y, fmt= '%f', delimiter= '/t', header= 'f(x)')
#np.savetxt(f_out, x, fmt= '%f', delimiter = '/t', header = 'x')
f_out.close()



