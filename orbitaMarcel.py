#Orbitas planetarias. A partir de la segunda ley de Kepler escriba un programa
#que calcule la posiciòn y velocidad en el afelio dada la posiciòn y velocidad
#en al perihelio

from math import pi

G=6.67e-11
m=1.989e30

Rp=float(input("ingrese el radio del perihelio"))
Vp=float(input("ingrese la velocidad del perihelio"))

Va=(((2*G*m)/(Vp*Rp))+((((2*G*m)/(Vp*Rp))**(2))+4*((Vp**2-2*G*m)/Rp))**1/2)/2
Ra=(Rp*Vp)/Va
a=(Rp+Ra)/2
b=(Rp*Ra)**(1/2)
T=(2*pi*a*b)/(Rp*Vp)
e=(Ra-Rp)/(Ra+Rp)

print("Velocidad del afelio es:" ,Va)
print("Radio del afelio:" ,Ra)
print("Semieje Mayor es:" ,a)
print("Semieje Menor es:" ,b)
print("Periodo orbital es:", T)
print("Excentricidad Orbital es:" ,e)
