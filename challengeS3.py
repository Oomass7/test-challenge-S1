


def addProd():
    print("AGREGAR PRODUCTOS")

def searchProd():
    print("BUSCAR PRODUCTOS")

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

def main(option):
    while True:
        showMenu()
        match option:
            case "1":
                addProd()
            case "2":
                searchProd()
            case "3":
                deleteProd()
            case "4":
                calValueInvent()
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    option = 0
    main(option)