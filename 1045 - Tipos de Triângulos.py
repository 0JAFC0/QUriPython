A, B, C = str(input()).split()
A = float(A);B = float(B);C = float(C)
lista = [A, B, C]
lista.sort(reverse = True)# Colocar os itens em ordem Decrescente
A = lista[0]; B = lista[1]; C = lista[2]
if(A >= (B + C)):
    print("NAO FORMA TRIANGULO")
else:
    if((A**2) == ((B**2)+(C**2))):
        print("TRIANGULO RETANGULO")
    if((A**2) > ((B**2)+(C**2))):
        print("TRIANGULO OBTUSANGULO")
    if((A**2) < ((B**2)+(C**2))):
        print("TRIANGULO ACUTANGULO")

        
    if(A == B == C):
       print("TRIANGULO EQUILATERO")
    elif(B == C or A == B or A == C):
       print("TRIANGULO ISOSCELES")
