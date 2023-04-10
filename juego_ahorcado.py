#!/usr/bin/env python3
#Author: Hacker NoDo
#Juego adivina el numero
from random import randint
from colorama import Fore
print(Fore.GREEN+'''   db    88  88  dP"Yb  88""Yb  dP""b8    db    8888b.   dP"Yb
  dPYb   88  88 dP   Yb 88__dP dP   `"   dPYb    8I  Yb dP   Yb
 dP__Yb  888888 Yb   dP 88"Yb  Yb       dP__Yb   8I  dY Yb   dP
dP""""Yb 88  88  YbodP  88  Yb  YboodP dP""""Yb 8888Y"   YbodP
  
''')
print(''' dP""b8    db    8b    d8 888888
dP   `"   dPYb   88b  d88 88__
Yb  "88  dP__Yb  88YbdP88 88""
 YboodP dP""""Yb 88 YY 88 888888

\n''')
print("Mi canal oficial : https://youtube.com/@hackerNoDo\n")


estimado = 0
Intentos = 0
numero_secreto = randint(1,100)
nombre = input("¿Cual es tu nombre?: ")

print(f"\nBueno {nombre}, he pensado en un numero del 1 al 100,\n\ntienes 8 Intentos para adivinarlo\n\n")

while Intentos < 8:
	estimado = int(input(f"{nombre}, ¿cual es el numero? : "))
	Intentos += 1
		
	
	if estimado < numero_secreto:
		print(f"{nombre}, mi numero es mas alto") 
	
	if estimado > numero_secreto:
		print(f"{nombre}, mi numero es mas bajo")
	
	if estimado == numero_secreto:
		print(f"{nombre}, Has ¡¡¡¡ GANADO en {Intentos} intentos !!!! ")
		break
		
		
if estimado != numero_secreto:
	print(f"{nombre}, Has perdido el numero era {numero_secreto},\n Has agotado los {Intentos} intentos\n\n")

print("Gracias °=°")
	
		
	

