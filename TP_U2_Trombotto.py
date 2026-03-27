#ACTIVIDADES
# EJERCICIO 1
#edad = int(input("Ingrese su edad: "))
#if edad >18:
#   print("Usted es mayor de edad.")

# EJERCICIO 2
#nota = float(input("Ingrese la nota obtenida: "))
#if nota >= 6.0:
#    print("Aprobado")
#else:
#    print("Desaprobado")

# EJERCICIO 3
#numero = int(input("Ingrese un número PAR: "))
#if numero % 2 == 0:
#    print("El número es PAR.")
#else:
#    print("El número es IMPAR.")

# EJERCICIO 4
# edad = int(input("Ingrese su edad: "))
# if edad < 12:
#    print("Niño")
# elif edad >= 12 and edad < 18:
#    print("Adolescente")
# elif edad >= 18 and edad < 30:
#    print("Adulto/Joven")
# else:
#    print("Adulto")

# EJERCICIO 5
#contraseña = input("Ingrese su contraseña de 8 caracteres: ")
#if len(contraseña) >= 8 and  len(contraseña) <= 14:
#    print("Contraseña válida.")
#else:
#    print("Contraseña inválida. Debe tener entre 8 y 14 caracteres.")

# EJERCICIO 6
# consumo = float(input("Ingrese el consumo de energía en kWh: "))
# if consumo <= 150:
#    print("consumo bajo")
# elif consumo > 150 and consumo <= 300:
#    print("consumo medio")
# elif consumo > 300 and consumo <= 500:
#    print("consumo alto")
# else:
#    print("Considere medidas de ahorro energético")

# EJERCICIO 7
# palabra = input("Ingrese una palabra o frase: ")
# vocales = "aeiouAEIOU"
# if len(palabra) > 0 and palabra[-1] in vocales:
#    print(palabra + "!")
# else:
#    print(palabra)

# EJERCICIO 8
# nombre = input("Ingrese su nombre: ")
# opcion=input("Seleccione una de las siguientes opciones:\n" \
# "1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n" \
# "2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n" \
# "3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. ")
# if opcion == "1":
#     print(nombre.upper())
# elif opcion == "2":
#     print(nombre.lower())
# elif opcion == "3":
#     print(nombre.title())
# else:
#     print("Opción inválida.")

# EJERCICIO 9
# magnitud = float(input("Ingrese la magnitud del sismo en la escala de Richter: "))
# if magnitud < 3.0:
#     print("Muy leve (imperceptible)")
# elif magnitud >= 3.0 and magnitud < 4.0:
#     print("Leve (igeramente perceptible)")
# elif magnitud >= 4.0 and magnitud < 5.0:
#     print("Moderado (sentido por personas, pero generalmente no causa daños)")
# elif magnitud >= 5.0 and magnitud < 6.0:
#     print("Fuerte (puede causar daños a estructuras débiles)")
# elif magnitud >= 6.0 and magnitud < 7.0:
#     print("Muy fuerte (puede causar daños significativos)")
# elif magnitud >= 7.0:
#     print("Extremo (puede causar graves daños a gran escala)")
# else:
#     print("Valor inválido.")  
# 
# # EJERCICIO 10
# hemisferio = input("Por favor, ingrese el hemisferio (N/S): ")
# hemisferio = hemisferio.lower()
# mes = int(input("Por favor, ingrese el mes del año en números: "))
# dia = int(input("Por favor, ingrese el día del mes en números: "))

# if hemisferio == "s":
#   # Si es después del 21/12, en cualquier momento de enero o febrero, o antes del 20/3 imprimimos "Verano"
#   if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
#     print("Verano")
#   # Si es después del 21/3, en cualquier momento de abril o mayo, o antes del 20/6 imprimimos "Otoño"
#   elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
#     print("Otoño")
#   # Si es después del 21/6, en cualquier momento de julio o agosto, o antes del 20/9 imprimimos "Invierno"
#   elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
#     print("Invierno")
#   # Si es después del 21/9, en cualquier momento de octubre o noviembre, o antes del 20/12 imprimimos "Primavera"
#   elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
#     print("Primavera")
# # Luego colocamos lo relativo al hemisferio norte
# elif hemisferio == "n":
#   # Si es después del 21/12, en cualquier momento de enero o febrero, o antes del 20/3 imprimimos "Invierno"
#   if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
#     print("Invierno")
#   # Si es después del 21/3, en cualquier momento de abril o mayo, o antes del 20/6 imprimimos "Primavera"
#   elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
#     print("Primavera")
#   # Si es después del 21/6, en cualquier momento de julio o agosto, o antes del 20/9 imprimimos "Verano"
#   elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
#     print("Verano")
#   # Si es después del 21/9, en cualquier momento de octubre o noviembre, o antes del 20/12 imprimimos "Otoño"
#   elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
#     print("Otoño")


