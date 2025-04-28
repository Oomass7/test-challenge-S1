# qualify = float(input("Ingrese su calificacion de 0-100: "))
qualifyList = []
numbersQua = int(input("Ingrese la cantidad de calificaciones que desea ingresar: "))
j = 0

while True: 
    if j < numbersQua:
        notes = float(input(f"Ingrese nota {j + 1}: "))
        j += 1
        qualifyList.append(notes)
        print(qualifyList)
    elif j == numbersQua:
        break

totalQua = sum(qualifyList)
average = totalQua / len(qualifyList)

print(average)


# if qualify > 50:
    # print("Usted ha aprobado")
