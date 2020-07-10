#!/usr/bin/env python
from sys import *
from math import *


def divisores(n):
	"""Retorna una lista con todos los divisores de un numero"""
	div = []
	for i in xrange(1, n/2+1):
		if n%i == 0:
			div.append(i)
	div.append(n)
	return div


def min_ab(n):
	"""Retorna los divisores a,b de un numero n (a > b) cuya relación de aspecto a/b se acerca a 1."""
	div = []; pareja = []; sdiv = 0
	div = divisores(n)
	sdiv = len(div)
	
	if sdiv%2 == 0:
		ab = [div[sdiv/2], div[sdiv/2-1]]
	else:
		ab = [div[sdiv/2], div[sdiv/2]]

	if ab[0] == n and n>2:
		ab = min_ab(n+1)
		
	return ab


def dibuja_ab(n):
	"""Dibuja un numero en terminos de los divisores a,b de la funcion min_ab."""
	ab = [] 
	largo = 0
	ancho = 0
	linea = ''
	lineaf = ''
	ab = min_ab(n)
	largo = ab[0]
	ancho = ab[1]
	
	#crea las lineas bases
	for j in range(largo):
		linea += '#'
	
	#crea la linea final
	if ancho*largo > n:
		for j in range(largo-1):
			lineaf += '#'
	else:
		lineaf = linea
	
	#imprime todas las lineas
	for i in range(ancho-1):
		print linea
	print lineaf
	print

'''
while True:
	linea = stdin.readline().strip()
	try:
		num = int(linea)
		if num < 0:
			print("Oops! El numero debe ser mayor que cero. Intenta de nuevo...")
			continue
		break
	except ValueError:
		print "Oops! Eso no fue un numero valido. Intenta de nuevo..."
num = int(linea)

num = 1000000
datos = []
linea = []
pareja = []
r = 0.0
ra = 1.618034
nmin = 10
rdmin = 10
pmin = []
k = 0

for n in xrange(1,num+1):
	p = 0
	pareja = min_rel_asp(n)
	r = 1.0*pareja[1]/pareja[0]
	
	rdif = abs(r-ra)

	if rdif < rdmin:
		rdmin = rdif
		nmin = n
		pmin = pareja
	
	k = n*100/num
	if n%(num/100) == 0:
		print k, "%"

print "rdmin = ", rdmin
print "nmin = ", nmin
print "pmin = ", pmin
'''
print min_ab(7)
dibuja_ab(7)
