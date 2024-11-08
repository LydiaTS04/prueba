#Escribir un programa en Python que calcule la suma de los primeros N números pares. 
#El programa debe solicitar al usuario el valor de N y utilizar un bucle para realizar la suma.

n = int(input("escribe un numero entero positivo:"))

while (n<0):
    print ("tiene que ser positivo")
    n = int(input("escribe un numero entero positivo:"))
    
suma_pares=0

for num in range(1,n+1): #n+1 para q cuente del 1 hasta N 
    if num % 2 ==0: #verificar que el numro es par
        suma_pares += num

print("la suma de los primero ",n," numeros pares es: ", suma_pares)
    