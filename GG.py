a=int(input("entre la valeur de ph :"))
b=str(input("entre la categorie:"))
A=0.07
B=0.25
C=0.3
if b == "A" :
 p = A*a + a
elif b == "B" :
 k = B*a + a
elif b == "C" :
 n = C*a + a
 print("la valeur de ph :{n}")
 print("la valeur de ph :{k}")
 print("la valeur de ph:" ,p )



