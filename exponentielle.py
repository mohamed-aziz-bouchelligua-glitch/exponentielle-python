from math import exp

EPS = 10**-6

x = float(input("Donner x : "))

s = 1
terme = 1
i = 1

while abs(terme) > EPS:
    terme = terme * x / i
    s = s + terme
    i = i + 1

print("Approximation de e^x :", s)
print("Valeur de reference :", exp(x))
print("Nombre de termes :", i)
