#Creamos un diccionario para guardar todo los productos
prods = {}
    
def valiDicVoid():
    """Esta funcion valida si el diccionario esta vacio"""

    if len(prods) == 0:
        return False, "No hay productos en el sistema."
    return True, None

def validateNumber(number):
    """Esta funcion valida si el numero ingresado por el usuario es un numero valido"""

    if number.isdigit() and int(number) > 0:
        return True, None
    return False, "Valor no valido."
        
def addProd():
    """En esta funcion el usuario pordra añadir productos (se almacenaran en el diccionario)"""

    print("AGREGAR PRODUCTOS")
    name = input("Ingrese el nombre de producto que desea añadir: ") #Le pedimos un nombre para el producto del usuario

    if name not in prods: #Si este nombre no se encuetra dentro del diccionario
        price = (input("Ingrese el precio del producto: "))
        val, msg = validateNumber(price)
        if val:        
            amount = (input("Ingrese la cantidad del producto: "))
            val, msg = validateNumber(amount)
            if val:
                prods[name] = (price, amount) #Creara una nueva clave la cual guaradara como valor una tupla que contiene el precio el y la cantidad ingresada por el usuario
            else:
                print(msg)
        else:
            print(msg)
    elif name in prods:
        print("El producto ya se encuentra en el sistema.") #En caso de que el nombre del producto ya se encuente le dira al usuario que el producto ya esta dentro del diccionario
    
    print(prods)

def searchProd():
    """En esta funcion el usuario podra buscar productos por medio de su nombre"""

    print("BUSCAR PRODUCTOS")
    val, msg = valiDicVoid()
    if val:
        name = input("Ingrese el nombre del producto que deseas buscar: ") 
        if name in prods: #Si el nombre que busco el usuario esta dentro del diccionario
            print(name, prods[name][0],prods[name][1]) #Le mostrara los datos del producto:
        elif name not in prods: #En caso de que no le dira que el producto no esta en el diccionario
            print("El producto no se encuentra en el sistema.")
    else:
        print(msg)

def updateProd():
    """En esta funcion el usuario podra actualizar el precio de los productos"""

    print("ACTUALIZAR PRODUCTOS")
    val, msg = valiDicVoid()
    if val:
        name = input("Ingrese el nombre del producto que deseas actualizar: ")
        if name in prods: #Si el nombre se encuentra en el diccionario
            newPrice, amount =  prods[name]   
            newPrice = (input("Ingresa el nuevo precio del producto: ")) #Le pedira un nuevo precio para el producto deseado
            val, msg = validateNumber(newPrice)
            if val:     
                prods[name] = (newPrice, amount) #Luego de haber eliminado la tupla antigua crea una nueva para guardar el nuevo valor
                print(name, prods[name][0],prods[name][1])
            else:
                print(msg)
        if name not in prods:
            print("El producto no se encuentra en el sistema")
    else:
        print(msg)

def deleteProd():
    """Esta funcion permite eliminar productos"""

    print("ELIMINAR PRODUCTOS")
    name = input("Ingrese el nombre del producto que desdeas eliminar: ")
    if name in prods: #Si el nombre que ingreso el usuario esta en el diccionario
        prods.pop(name) #Eliminara el producto junto con sus detalles
        print("Producto eliminado.")
    else:
        print("El nombre no se encuentra en el sistema.")
    print(prods)

def calValueInvent():
    """Esta funcion permite calcular el valor total del inventario"""

    print("CALCULAR VALOR INVENTARIO")
    valueTotal = sum(map(lambda products: products[0] * products[1], prods.values())) #se crea una variable que "recorrera" el diccionario y le entrega un valor a cada posicion de la tupla para luego multiplicarlas y guardarlas
    if valueTotal <= 0:
        print("No hay productos en el sistema")
    else:
        print(f"El valor total del inventario es de: ${valueTotal}")

def showMenu():
    """Esta funcion permite mostrar el menu al usuario y preguntarle la opcion que desea ejecutar"""

    print("-"*60)
    print("MENU")
    print("1. Agregar productos")
    print("2. Buscar productos")
    print("3. Eliminar productos")
    print("4. Actualizar productos")
    print("5. Calcular valor de inventario")
    print("6. Salir")
    option = input("Seleccione una opción del menu: ")
    print("-"*60)
    return option

def main():
    """Y por ultimo la funcion main que es la que se encarga de llamar las funciones para que ejectutar cada opcion"""

    while True:
        option = showMenu()
        match option:
            case "1":
                addProd()
            case "2":
                searchProd()
            case "3":
                deleteProd()
            case "4":
                updateProd()
            case "5":
                calValueInvent()
            case "6":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida, intente de nuevo.")

main() #Llamamos la funcion main para que se pueda ejecutar el programa