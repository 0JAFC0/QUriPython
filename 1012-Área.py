A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
atriangulo = (A * C) / 2
acirculo = (3.14159 * C ** 2)
atrapezio = ((A + B) * C / 2)
aquadrado = (B**2)
aretangulo = (A * B)
print("TRIANGULO: {:.3f}".format(atriangulo))
print("CIRCULO: {:.3f}".format(acirculo))
print("TRAPEZIO: {:.3f}".format(atrapezio))
print("QUADRADO: {:.3f}".format(aquadrado))
print("RETANGULO: {:.3f}".format(aretangulo))
