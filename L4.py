#Juan Ignacio Montealegre Salazar
#Carné B95001
#Laboratorio 4 de Modelos Probabilísticos de Señales y Sistemas
#Código base modificado para solucionar problema 4 de de la práctica E13
'''
Parte a) Suponiendo que Ω no es una variable aleatoria, 
sino una constante omega. Encuentre el valor medio
 Los parámetros T, t_final y N son elegidos arbitrariamente
'''
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Variables aleatorias C y Z
vaC = stats.norm(5, np.sqrt(0.2))
vaZ = stats.uniform(0, np.pi/2)

#Constante Omega
Omega = 2*np.pi

# Creación del vector de tiempo
T = 100			# número de elementos
t_final = 2# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicialización del proceso aleatorio X(t) con N realizaciones
N = 20
X_t = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

# Creación de las muestras del proceso x(t) (C y Z independientes)
for i in range(N):
	C = vaC.rvs()
	Z = vaZ.rvs()
	x_t = C * np.cos(Omega*t + Z)
	X_t[i,:] = x_t
	plt.plot(t, x_t)

# Promedio de las N realizaciones en cada instante (cada punto en t)
P = [np.mean(X_t[:,i]) for i in range(len(t))]
plt.plot(t, P, lw=6)

# Graficar el resultado teórico del valor esperado
E = (10/np.pi) * (np.cos(Omega*t)-np.sin(Omega*t))
print ("Valor teórico de la media E: ")
print(E)
plt.plot(t, E, '-.', lw=4)

# Mostrar las realizaciones, y su promedio calculado y teórico
plt.title('Realizaciones del proceso aleatorio $X(t)$')
plt.xlabel('$t$')
plt.ylabel('$x_i(t)$')
plt.show()

'''Parte b) Suponga ahora que Ω y Θ son constantes, no variables aleatorias
Obtenga el valor teórico de la correlación'''
Z = 0

# Se redifinen las muestras del proceso x(t) (C y Z independientes)
for i in range(N):
	C = vaC.rvs()
	Z = vaZ.rvs()
	x_t = C * np.cos(Omega*t + Z)
	X_t[i,:] = x_t

    

# T valores de desplazamiento tau
desplazamiento = np.arange(T)
taus = desplazamiento/t_final

# Inicialización de matriz de valores de correlación para las N funciones
corr = np.empty((N, len(desplazamiento)))

# Nueva figura para la autocorrelación
plt.figure()

# Cálculo de correlación para cada valor de tau
for n in range(N):
	for i, tau in enumerate(desplazamiento):
		corr[n, i] = np.correlate(X_t[n,:], np.roll(X_t[n,:], tau))/T
	plt.plot(taus, corr[n,:])

# Valor teórico de correlación
Rxx = 25.2 * np.cos(Omega*t+Z) * np.cos(Omega*(t+taus)+Z)
print ("Valor teórico de la correlación Rxx: ")
print(Rxx)

# Gráficas de correlación para cada realización y la
plt.plot(taus, Rxx, '-.', lw=4, label='Correlación teórica')
plt.title('Funciones de autocorrelación de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{XX}(\tau)$')
plt.legend()
plt.show()
