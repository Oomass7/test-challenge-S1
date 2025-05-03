# El programa que vas a desarrollar en este entrenamiento debe:
# Determinar el estado de aprobación:
#   Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
#   Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
# Calcular el promedio:
#   Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
#   Calcular y mostrar el promedio de las calificaciones en la lista
# Contar calificaciones mayores:
#   Preguntar al usuario por un valor específico
#   Contar cuántas calificaciones en la lista son mayores que este valor
# Verificar y contar calificaciones específicas
#   Preguntar al usuario por una calificación específica. 
#   Verificar si esta calificación está en la lista y contar cuántas veces aparece, utilizando break y continue para controlar el flujo del programa. 


while True: #Iniciamos un ciclo while para mantenernos dentro del programa
    try: 
        print("-"*40)
        print("MENU")
        print("1. Aprobacion de materia \n2. Promedio de calificaciones \n3. Calificaciones inferiores \n4. Calificacion especifica en la lista")
        print("-"*40)
        option = int(input("Ingrese el numero de la opcion que desea: "))
        listIntQualifys = []
        numbersCount = []
        match option:
            case 1:
                print("-"*40)
                print("APROBACION DE MATERIA")
                print("-"*40)
                while True:
                    try:
                        qualify = float(input("Ingrese su nota definitiva (de 0 a 100): "))
                        if qualify < 65 and qualify >= 0:
                            print("Has reprobado la materia")
                            break
                        elif qualify > 65 and qualify <= 100:
                            print("Has aprobado la materia") 
                            break 
                        elif qualify < 0 or qualify > 100:
                            print("Recuerda que la nota debe estar dentro del rango indicado")  
                    except:
                        print("Intentaste escribir una letra\n")
                continue
            case 2:
                print("-"*40)
                print("PROMEDIO DE CALIFICACIONES")
                print("-"*40)
                while True:
                    notes = input("Ingresa las calificaciones separadas por comas y sin espacios: ")
                    noteSeparates = notes.split(",")
                    for note in noteSeparates:
                        note = note.strip()
                        try:
                            number = int(note)
                        except:
                            listIntQualifys.clear()
                            print("Intentaste ingresar una letra, intentalo de nuevo\n")
                            break
                        if number < 0 or number > 100:
                            print("Ingresaste un numero que no esta dentro del rango definido, porfavor intenta de nuevo\n")
                            listIntQualifys.clear()
                            break
                        else:
                            listIntQualifys.append(number)
                    if len(listIntQualifys) == 0:
                        break
                    else:
                        print(listIntQualifys)
                        sumQualifys = sum(listIntQualifys)
                        numbersQulifys = len(listIntQualifys)
                        averageQualifys = sumQualifys / numbersQulifys
                        print(f"El promedio de tus notas es de: {averageQualifys:.2f}")
                        break
                    
            case 3:
                print("-"*40)
                print("CALIFICACIONES MAYORES AL VALOR DESEADO")
                print("-"*40)
                notes = input("Ingresa las calificaciones separadas por comas y sin espacios: ")
                noteSeparate = notes.split(",")
                for note in noteSeparates:
                    note = note.strip()
                    try:
                        number = int(note)
                    except:
                        listIntQualifys.clear()
                        print("Intentaste ingresar una letra, intentalo de nuevo\n")
                        break
                    if number < 0 or number > 100:
                        print("Ingresaste un numero menor a cero, porfavor intenta de nuevo\n")
                        listIntQualifys.clear()
                        break
                    else:
                        listIntQualifys.append(number)
                while True:
                    if len(listIntQualifys) == 0:
                        break
                    else:
                        try:
                            noteEspecific = int(input("Ingresa un valor especifico: "))
                            for i in listIntQualifys:
                                if i > noteEspecific:
                                    numbersCount.append(i) 
                                    break
                            print(f"Hay {len(numbersCount)} calificaciones mayores al valor que ingresaste\n")
                            break
                        except:
                            print("Intentaste ingresar una letra")

            case 4:
                print("-"*40)
                print("CALIFICACION ESPECIFICA EN LA LISTA")
                print("-"*40)
                notes = input("Ingresa las calificaciones separadas por comas y sin espacios: ")
                noteSeparate = notes.split(",")
                for note in noteSeparates:
                    note = note.strip()
                    try:
                        number = int(note)
                    except:
                        listIntQualifys.clear()
                        print("Intentaste ingresar una letra, intentalo de nuevo\n")
                        break
                    if number < 0 or number > 100: 
                        print("Ingresaste un numero menor a cero, porfavor intenta de nuevo\n")
                        listIntQualifys.clear()
                        break
                    else:
                        listIntQualifys.append(number)
                while True:
                    if len(listIntQualifys) == 0:
                        break
                    else:
                        try:
                            noteEspecific = int(input("Ingresa un valor especifico: "))
                            for i in listIntQualifys:
                                if i > noteEspecific:
                                    numbersCount.append(i) 
                                    break
                            print(f"Esta nota esta {len(numbersCount)} veces en la lista de acalificaciones\n")
                            break
                        except:
                            print("Intentaste ingresar una letra")
            case 5:
                print("Muchas gracias por utilizar el programa")
                break
            case _:
                print("La opcion que ingresaste no esta en el menu")
    except:
        print("Recuerda que solo tienes que ingresar el numero de la opcion")
exit