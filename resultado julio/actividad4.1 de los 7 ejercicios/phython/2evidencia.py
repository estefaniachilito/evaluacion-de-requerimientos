n1 = int(input("ingrese primer numero "))
n2 = int(input("ingrese primer numero "))
n3 = int(input("ingrese primer numero ")) 

if n1<n2 and n1< n3:
    print("el numero menor es:",n1)

if n2<n3 and n2<n1:
    print("el numero menor es:",n2)

if n3<n1 and n3 < n2:
    print("el numero menor es:",n3)

if n1<n2 and n1 == n3 :
    print("los numeros primero y tercero son el numero: ",n1," y es el numero menor.")

if n1<n3 and n1 == n2 :
    print("los numeros primero y segundo son el numero: ",n1," y es el numero menor.")

if n3<n1 and n3 == n2 :
    print("los numeros segundo y tercero son el numero: ",n2," y es el numero menor.")