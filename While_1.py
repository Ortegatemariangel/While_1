# input
n = int(input("Digite el valor de n: "))

# Processing
s= 0
i= 1
while i<= n:
    s = s+i
    i = i+1
print ("La suma de los " + str (n) + "primeros numeros naturales es " + str (s))