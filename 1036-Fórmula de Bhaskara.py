A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
delta = (((B)**2)-(4*(A)*(C)))#Não potenciar por (1/2)
if(A != 0) and (delta >= 0):
    x1 = (((-1) * (B))+(delta **(1/2)))/(2*A)
    x2 = (((-1) * (B))-(delta **(1/2)))/(2*A)
    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))
else:
    print("Impossivel calcular")
