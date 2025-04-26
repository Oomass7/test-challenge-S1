#Se crean listas para guardar datos mas adelante
storeProd = []
valueTotalProds = []
addProd = "si" 


#Se crea un ciclo para que el usuario pueda tomar la decicion de agregar de no agregar producto o los que quiera
while True:
    quantityProd = len(storeProd) 
    addProd = input("¿Quiere agregar un nuevo producto? si/no: ")
    #Se crean condiciones para que el usuario ingrese el producto
    if addProd == "si":
        print("Nuevo producto")  
        while True:
            nameProd = str(input("Ingrese el nombre del producto: "))
            if nameProd == "":
                print("Ingrese un numbre valido")
            else:
                break 
        #Se crea un ciclo para preguntar por los dato de los producto
        while True:
            try:
                valueProd = float(input("Ingrese el valor unitario del producto: "))
                if valueProd <= 0 : 
                    print("Ingrese un valor mayor a 0")
                else:
                    break 
            except:
                print("Intentaste escribir una letra/palabra")
        while True:
            try:
                quanProd = int(input("Ingrese la cantidad que desea llevar: "))
                if quanProd <= 0: 
                    print("Ingrese un valor valido (mayor que 0)")
                else:
                    break 
            except:
                print("Intentaste escribir una letra/palabra") 
        #Se almacenan los datos del producto en un dicionario con palbras claves y luego se guardan en la ultima poscion de la lista 
        product = { 
                "nameProd": nameProd, 
                "valueProd": valueProd, 
                "quanProd": quanProd 
        }
        storeProd.append(product)   
        
    #En caso de que el usuario no quiera agregar mas producto pero la lista ya tiene mas de un elemto, el codigo continuara con el resto del proceso
    elif addProd == "no" and quantityProd > 0: 
        #Con el ciclo for le mostraremos al usuario los datos de cada producto
        for i, product in enumerate(storeProd):  
            print(f"\nNombre del producto: {product["nameProd"]} \nValor del producto: {product["valueProd"]} \nCantidad del producto: {product["quanProd"]} \n") 
        #Con el ciclo for recorreremos la lista para guardar el valor de cada producto por su cantidad y se guardara en una lista
        for product in storeProd: 
            valueOfEachProd = product["valueProd"] * product["quanProd"] 
            valueTotalProds.append(valueOfEachProd) 
        #Luego sumaremos todo los precios de los producto de la lista para obtener el valor total de la compra
        valueTotalPay = sum(valueTotalProds) 
        
        #Se crearan condicones de precios para saber cuanto descuento obtendra el usuario
        if valueTotalPay > 80000:
            valueDiss = valueTotalPay * 0.5
            endValuePay = valueTotalPay - valueDiss
            for i, product in enumerate(storeProd): 
                print(f"{product["nameProd"]} = {product["quanProd"]}")
            print(f"EL valor total de la compra es de: ${valueTotalPay}")
            print("Tienes un descuento del 50% por compras mayores a $80000")
            print(f"El valor a pagar es: ${endValuePay:.2f}")
            break
        elif valueTotalPay > 70000:
            valueDiss = valueTotalPay * 0.4
            endValuePay = valueTotalPay - valueDiss
            for i, product in enumerate(storeProd): 
                print(f"{product["nameProd"]} = {product["quanProd"]}")
            print(f"EL valor total de la compra es de: ${valueTotalPay}")
            print("Tienes un descuento del 40% por compras mayores a $70000")
            print(f"El valor a pagar es: ${endValuePay:.2f}")
        elif valueTotalPay > 50000:
            valueDiss = valueTotalPay * 0.2 
            endValuePay = valueTotalPay - valueDiss 
            for i, product in enumerate(storeProd): 
                print(f"{product["nameProd"]} = {product["quanProd"]}")
            print(f"EL valor total de la compra es de: ${valueTotalPay}")
            print("Tienes un descuento del 20% por compras mayores a $50000")
            print(f"El valor a pagar es: ${endValuePay:.2f}")
            break
        else: 
            endValuePay = valueTotalPay
            for i, product in enumerate(storeProd): 
                print(f"{product["nameProd"]} = {product["quanProd"]}")
            print(f"EL valor total de la compra es de: ${valueTotalPay}")
            print("No has obtenido el descuento")
            print(f"EL valor a pagar es: ${endValuePay:.2f}") 
            break    
    #Por ultimo en caso de que el usuario no quiera agregar producto, y la lista no tenga ningun elemento, este lo sacara del programa con un mensaje    
    elif addProd == "no" and quantityProd <= 0: 
        print("Muchas gracias por visitar la tienda") 
        break 