dataToDis = [] #Se crea una lista para guardar los datos ingresados por el usuario mas adelante

while True: #Se crea un ciclo mientras
    nameProd = str(input("Ingrese el nombre del producto: ")) #Se le peidra al usario para que ingrese un nombre de producto y se le asigna a la variable
    dataToDis.append(nameProd) #Se guarda la variable en la ultima posicion de la lista
    if nameProd == "": #Se crea una condicion que se iguala a un espacio en blanco
        print("Ingrese un nombre valido") #Se le pie al usuario que ingrese un nombre valido
    else: #Si no se cumple la condicion
        break #Se rompe el ciclo mientras y continua con el resto del codigo

while True: #Se crea un ciclo mientras
    try: #Se crea un try que continuara con el procedimiento normal del codigo
        priceProd = int(input("Ingrese el precio unitario del producto: ")) #Se le peidra al usario para que ingrese el precio del producto y se le asigna a la variable
        if priceProd <= 0: #Se crea una condicion que si es menor o igual a 0
            print("Ingrese un valor mayor a 0") #Le pedira al usuario que ingrese un valor mayor a 0 
        else: #Si no se cumple la condicion
            break #Se rompe el ciclo mientras y continua con el resto del codigo
    except: #En caso de que el usario ingrese un string 
        print("Intentaste ingresar una letra/palabra") #Se le mostrara que intento ingresar un dato no valido para la variable
    
while True: #Se crea un ciclo mientras
    try: #Se crea un try que continuara con el procedimiento normal del codigo
        amountProd = int(input("Ingrese la cantidad que desea llevar: ")) #Se le peidra al usario para que ingrese la cantidad del producto y se le asigna a la variable
        if amountProd <= 0: #Se crea una condicion que si es menor o igual a 0
            print("Ingresa una cantidad mayor a 0") #Le pedira al usuario que ingrese un valor mayor a 0
        else: #Si no se cumple la condicion
            break #Se rompe el ciclo mientras y continua con el resto del codigo
    except:
        print("Estas intentando ingresar una letra/palabra") #Se le mostrara que intento ingresar un dato no valido para la variable
        
while True: #Se crea un ciclo mientras
    try: #Se crea un try que continuara con el procedimiento normal del codigo
        percentageDiss = int(input("Ingrese el porcentaje del descuento (0-100): ")) #Se le peidra al usario para que ingrese el porcentaje de descuento que tiene el producto y se le asigna a la variable
        if percentageDiss < 0 and percentageDiss > 100: #Se crea una condicion en la que el numero tiene que estar dentro de un rango de 0-100
            print("Ingrese un valor dentro del rango establecido") #Le pedira al usario que ingrese un valor que este dento del rango establecido
        else: #Si no se cumple la condicion
            break #Se rompe el ciclo mientras y continua con el resto del codigo
    except: #En caso de que el usario ingrese un string
        print("Intentaste ingresar una letra/palbra") #Se le mostrara que intento ingresar un dato no valido para la variable
        
priceTotal = amountProd * priceProd #Se iguala una varibale que corresponde al precio total de la compra sin descuento
dataToDis.append(priceTotal) #Se guarda la variable en la ultima posicion de la lista

disscount =  (priceTotal * percentageDiss)/100 #Se iguala una varibale que correspone al valor que se le restara al precio total 

priceTotalWhithDiss = priceTotal - disscount #Se iguala una variable al precio total de la compra con descuento
dataToDis.append(priceTotalWhithDiss) #Se guarda la variable en la ultima posicion de la lista

if percentageDiss > 0:
    print(f"""Nombre del producto: {nameProd}
El precio total de su compra es de: ${priceTotal}
El precio total de su compra con descuento es de: ${priceTotalWhithDiss:.2f}""")
else: #Si no se cumple la condicion
    print(f"El precio total de su compra es de: ${priceTotal}")
        
