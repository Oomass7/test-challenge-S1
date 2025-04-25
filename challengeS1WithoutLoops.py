dataToDis = []

while True:
    nameProd = str(input("Ingrese el nombre del producto: "))
    nameProd = nameProd.startswith
    dataToDis.append(nameProd)
    if nameProd == "":
        print("Ingrese un nombre valido")
    else:
        break

while True:
    try:
        priceProd = int(input("Ingrese el precio unitario del producto: "))
        if priceProd <= 0:
            print("Ingrese un valor mayor a 0")   
        else:
            break
    except:
        print("Intentaste ingresar una letra/palabra")
    
while True:
    try:
        amountProd = int(input("Ingrese la cantidad que desea llevar: "))
        if amountProd <= 0:
            print("Ingresa una cantidad mayor a 0")
        else:
            break
    except:
        print("Estas intentando ingresar una letra/palabra")
        
while True:
    try:
        percentageDiss = int(input("Ingrese el porcentaje del descuento (0-100): "))
        if percentageDiss < 0 and percentageDiss > 100:
            print("Ingrese un valor dentro del rango establecido")
        else:
            break
    except:
        print("Intentaste ingresar una letra/palbra")
        
priceTotal = amountProd * priceProd
dataToDis.append(priceTotal)

disscount =  (priceTotal * percentageDiss)/100

priceTotalWhithDiss = priceTotal - disscount
dataToDis.append(priceTotalWhithDiss)

if percentageDiss > 0:
    print(f"""Nombre del producto: {nameProd}
El precio total de su compra es de: ${priceTotal}
El precio total de su compra con descuento es de: ${priceTotalWhithDiss:.2f}""")
else:
    print(f"El precio total de su compra es de: ${priceTotal}")
        
        
    