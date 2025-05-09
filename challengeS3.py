prods = {}




def addProd():
    print("AGREGAR PRODUCTOS")
    name = input("Ingrese el nombre de producto que desea añadir: ")
    if name not in prods:
        price = float(input("Ingrese el precio del producto: "))
        amount = int(input("Ingrese la cantidad del producto: "))
        prods[name] = (price, amount)
    
    print(prods)
def searchProd():
    print("BUSCAR PRODUCTOS")
    name = input("Ingrese el nombre del producto que deseas buscar: ")
    for i, valor in prods.items():
        print(i, valor)
        

def updateProd():
    print("ACTUALIZAR PRODUCTOS")

def deleteProd():
    print("ELIMINAR PRODUCTOS")

def calValueInvent():
    print("CALCULAR VALOR INVENTARIO")

def showMenu():
    print("MENU")
    print("1. Agregar productos")
    print("2. Buscar productos")
    print("3. Eliminar productos")
    print("4. Actualizar productos")
    print("5. Calcular valor de inventario")
    print("6. Salir")
    option = input("Seleccione una opción del menu: ")
    return option

def main():
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

main()