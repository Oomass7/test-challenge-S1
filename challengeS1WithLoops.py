prodTienda = [] #Se crea un lista vacia que recibira valores correspondientes al porducto mas adelante
valorTotalProds = [] #Se crea una lista vacia que recibira el valor total por cantidad de productos que lleve el usuario
agregarProd = "si" #Se cra una variable de cadena para condicionar si volver al ciclo o reomperlo

while True:
    cantidadProd = len(prodTienda)
    print(prodTienda)
    print(cantidadProd)
    agregarProd = input("¿Quiere agregar un nuevo producto? si/no: ") #Se cra una variable de cadena para condicionar si volver al ciclo o reomperlo
    
    if agregarProd == "si": #Se crea un bucle para agregar un producto si el mensaje introducido es igual a la variable
        print("Nuevo producto") #Muestra un mensaje en pantalla que le indica al usuario que va a agregar un nuevo producto    
        while True:
            nombreProd = str(input("Ingrese el nombre del producto: ")) #Le pide al usuario que ingrese el nombre del producto
            if nombreProd == "":
                print("Ingrese un numbre valido")
            else:
                break
            
        while True:
            try:
                valorProd = float(input("Ingrese el valor unitario del producto: ")) #Le pide al usuario que ingrese el valor unitario del producto
                if valorProd <= 0 :
                    print("Ingrese un valor mayor a 0")
                else:
                    break
            except:
                print("Intentaste escribir una letra/palabra")
                
        while True:    
            try:
                cantProd = int(input("Ingrese la cantidad que desea llevar: ")) #Le pide al usuario que ingrese la cantidad que va a llevar de ese producto
                if cantProd <= 0:
                    print("Ingrese un valor valido (mayor que 0)")
                else:
                    break
            except:
                print("Intentaste escribir una letra/palabra")
                
        
        
        producto = { #Se crea un diccionario dentro de la lista para guardar varios valores
                "nombreProd": nombreProd, #Se guarda el nombre del prodcuto en la clave de nombre
                "valorProd": valorProd, #Se guarda el valor del producto en la clave de valor
                "cantProd": cantProd #Se guarda la cantidad del producto en la clave de cantidad
        }
        prodTienda.append(producto) #Se guarda la informacion de la variable producto en la ultima posicion de la lista de producto       
    elif agregarProd == "no" and cantidadProd > 0:
        for i, producto in enumerate(prodTienda): #Se crea un ciclo for para recorrer la lista 
            print(f"""\n
                    Nombre del producto: {producto["nombreProd"]} \n
                    Valor del producto: {producto["valorProd"]} \n
                    Cantidad del producto: {producto["cantProd"]} \n
                    """) #Imprime el nombre, el valor y la cantidad de los productos en la lista
        for producto in prodTienda: #Se crea un ciclo for, en el que buscara producto en la lista de productos
            valorCadaProd = producto["valorProd"] * producto["cantProd"] #Busca el valor clave guardada en el diccionario y se multiplica el valor del producto con la cantidad para saber el valor total del mismo producto
            valorTotalProds.append(valorCadaProd) #Se guarda el valor total del mismo producto en la lista 
        valorTotalCompra = float(0) #Se crea una variable que guardara el valor total de la compra
        valorTotalCompra = sum(valorTotalProds) #Se suman los valores totales de cada producto para saber cual es el valor total de la compra
        for i, producto in enumerate(prodTienda): #Se crea un ciclo for para recorrer la lista nuevamente
            print(f"{producto["nombreProd"]} * {producto["cantProd"]} = {valorTotalProds[i]}") #Busca el valor clave que se guardo en el diccionario y luego se multiplica para mostrar el nombre del producto multiplicado por la cantidad del producto y el valor total a pagar por ese producto 
        if valorTotalCompra > 50000: #Se crea un condicional donde si mayoR a 5000 hara lo siguiente
            valorDes = valorTotalCompra * 0.2 #Se crea la variable de calor final de la compra y lo igualamos al valor total de la compra y lo multiplicamos por el 0.2(20%)
            valorFinalCompra = valorTotalCompra - valorDes #Se le resta el valor del descuento al valor final de la compra
            print("Tienes un descuento del 20% por compras mayores a $50000") #Se le dice al usuario que obtuvo el descuento gracias a que cumplio la condicion
            print(f"El valor a pagar es: ${valorFinalCompra:.2f}") #Se muestra al usaurio la cantidad que debe pagar con el descuento
            break
        else: #Sino se cumple la condicion
            valorFinalCompra = valorTotalCompra #La variable de final de compra es igual al calor total de la compra
            print("No has obtenido el descuento por compras mayores a $50000") #Se le dice al usuario que no obtuvo el descuento
            print(f"EL valor a pagar es: ${valorFinalCompra}") #Se muestra al usuario la cantidad que debve pagar sin el descuento
            break        
    elif agregarProd == "no" and cantidadProd <= 0:
        print("Muchas gracias por visitar la tienda")
        break