#Ejercicio 1
 

# nombre = input("Cliente: ").strip() 

# while nombre == "" or not nombre.isalpha():
#     print("Error: ingresá un nombre válido.")
#     nombre = input("Cliente: ").strip()

# cantidad_str = input("Cantidad de productos: ").strip()

# while not cantidad_str.isdigit() or int(cantidad_str) <= 0:
#     print("Error: ingresá un número válido positivo.")
#     cantidad_str = input("Cantidad de productos: ").strip()

# cantidad = int(cantidad_str)

# total_sin_descuento = 0
# total_con_descuento = 0.0

# for i in range(1, cantidad + 1):
#     precio_str = input(f"Producto {i} - Precio: ").strip()

#     while not precio_str.isdigit() or int(precio_str) <= 0:
#         print("Error: ingresá un precio válido positivo.")
#         precio_str = input(f"Producto {i} - Precio: ").strip()

#     precio = int(precio_str)

#     desc = input("Descuento (S/N): ").strip().lower()
#     while desc not in ("s", "n"):
#         print("Error: ingresá 'S' para sí o 'N' para no .")
#         desc = input("Descuento (S/N): ").strip().lower()

#     total_sin_descuento += precio

#     if desc == "s":
#         precio_final = precio * 0.90
#     else:
#         precio_final = float(precio)

#     total_con_descuento += precio_final

# ahorro = total_sin_descuento - total_con_descuento
# promedio = total_con_descuento / cantidad

# print(f"Total sin descuentos: ${total_sin_descuento}")
# print(f"Total con descuentos: ${total_con_descuento:.2f}")
# print(f"Ahorro: ${ahorro:.2f}")
# print(f"Promedio por producto: ${promedio:.2f}")

#Ejercicio 2

# USUARIO_CORRECTO = "alumno"
# CLAVE_CORRECTA = "python123"

# clave_actual = CLAVE_CORRECTA

# intento = 1
# acceso_concedido = False

# while intento <= 3 and acceso_concedido == False:
#     usuario = input(f"Intento {intento}/3 - Usuario: ").strip()
#     clave = input("Clave: ").strip()

#     if usuario == USUARIO_CORRECTO and clave == clave_actual:
#         print("Acceso concedido.")
#         acceso_concedido = True
#     else:
#         print("Error: credenciales inválidas.")
#         intento += 1

# if acceso_concedido == False:
#     print("Cuenta bloqueada")
# else:

#     seguir_menu = True

#     while seguir_menu == True:
#         print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
#         opcion_str = input("Opción: ").strip()

#         while not opcion_str.isdigit():
#             print("Error: ingrese un número válido.")
#             opcion_str = input("Opción: ").strip()

#         opcion = int(opcion_str)

#         while opcion < 1 or opcion > 4:
#             print("Error: opción fuera de rango.")
#             opcion_str = input("Opción: ").strip()

#             while not opcion_str.isdigit():
#                 print("Error: ingrese un número válido.")
#                 opcion_str = input("Opción: ").strip()

#             opcion = int(opcion_str)


#         if opcion == 1:
#             print("Inscripto")

#         elif opcion == 2:
#             cambio_exitoso = False

#             while cambio_exitoso == False:
#                 nueva = input("Nueva clave: ").strip()

#                 if len(nueva) < 6:
#                     print("Error: mínimo 6 caracteres.")
#                 else:
#                     confirmacion = input("Confirmar clave: ").strip()

#                     if nueva != confirmacion:
#                         print("Error: las claves no coinciden.")
#                     else:
#                         clave_actual = nueva
#                         print("Clave actualizada correctamente.")
#                         cambio_exitoso = True

#         elif opcion == 3:
#             print("¡Paso a paso: si insistís, te sale!")

#         elif opcion == 4:
#             print("Sesión cerrada.")
#             seguir_menu = False


#Ejercicio 3

# lunes1 = ""
# lunes2 = ""
# lunes3 = ""
# lunes4 = ""

# martes1 = ""
# martes2 = ""
# martes3 = ""

# operador = input("Ingrese su nombre: ").strip()

# while operador == "" or not operador.isalpha():
#     print("Nombre inválido, solo letras y no vacío.")
#     operador = input("Ingrese su nombre: ").strip()

# print(f"\nBienvenido {operador}\n")

# opcion = 0

# while opcion != 5:
#     print("1) Agregar turno")
#     print("2) Quitar turno")
#     print("3) Mostrar agenda")
#     print("4) Ver resumen")
#     print("5) Salir")

#     opcion_str = input("Seleccione una opción: ").strip()

#     while (not opcion_str.isdigit()) or (int(opcion_str) < 1) or (int(opcion_str) > 5):
#         if not opcion_str.isdigit():
#             print("Debe ingresar un número.")
#         else:
#             print("Opción inválida.")
#         opcion_str = input("Seleccione una opción: ").strip()

#     opcion = int(opcion_str)

#     if opcion == 1:
#         dia_str = input("Elegir día (1 o 2): ").strip()

#         while (not dia_str.isdigit()) or (int(dia_str) < 1) or (int(dia_str) > 2):
#             if not dia_str.isdigit():
#                 print("Debe ingresar un número.")
#             else:
#                 print("Día incorrecto.")
#             dia_str = input("Elegir día (1 o 2): ").strip()

#         dia = int(dia_str)

#         paciente = input("Nombre del cliente: ").strip()

#         while paciente == "" or not paciente.isalpha():
#             print("Nombre inválido.")
#             paciente = input("Nombre del cliente: ").strip()

#         repetido = False

#         if dia == 1:
#             if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
#                 repetido = True
#         else:
#             if paciente == martes1 or paciente == martes2 or paciente == martes3:
#                 repetido = True

#         if repetido == True:
#             print("Ese nombre ya tiene turno ese día.\n")
#         else:
#             reservado = False

#             if dia == 1:
#                 if lunes1 == "":
#                     lunes1 = paciente
#                     reservado = True
#                     print("Asignado lunes turno 1\n")
#                 elif lunes2 == "":
#                     lunes2 = paciente
#                     reservado = True
#                     print("Asignado lunes turno 2\n")
#                 elif lunes3 == "":
#                     lunes3 = paciente
#                     reservado = True
#                     print("Asignado lunes turno 3\n")
#                 elif lunes4 == "":
#                     lunes4 = paciente
#                     reservado = True
#                     print("Asignado lunes turno 4\n")
#             else:
#                 if martes1 == "":
#                     martes1 = paciente
#                     reservado = True
#                     print("Asignado martes turno 1\n")
#                 elif martes2 == "":
#                     martes2 = paciente
#                     reservado = True
#                     print("Asignado martes turno 2\n")
#                 elif martes3 == "":
#                     martes3 = paciente
#                     reservado = True
#                     print("Asignado martes turno 3\n")

#             if reservado == False:
#                 print("No hay más turnos disponibles.\n")

#     elif opcion == 2:
#         dia_str = input("Elegir día (1 o 2): ").strip()

#         while (not dia_str.isdigit()) or (int(dia_str) < 1) or (int(dia_str) > 2):
#             if not dia_str.isdigit():
#                 print("Debe ingresar un número.")
#             else:
#                 print("Día incorrecto.")
#             dia_str = input("Elegir día (1 o 2): ").strip()

#         dia = int(dia_str)

#         paciente = input("Nombre a eliminar: ").strip()
#         while paciente == "" or not paciente.isalpha():
#             print("Nombre inválido.")
#             paciente = input("Nombre a eliminar: ").strip()

#         encontrado = False

#         if dia == 1:
#             if lunes1 == paciente:
#                 lunes1 = ""
#                 encontrado = True
#             elif lunes2 == paciente:
#                 lunes2 = ""
#                 encontrado = True
#             elif lunes3 == paciente:
#                 lunes3 = ""
#                 encontrado = True
#             elif lunes4 == paciente:
#                 lunes4 = ""
#                 encontrado = True
#         else:
#             if martes1 == paciente:
#                 martes1 = ""
#                 encontrado = True
#             elif martes2 == paciente:
#                 martes2 = ""
#                 encontrado = True
#             elif martes3 == paciente:
#                 martes3 = ""
#                 encontrado = True

#         if encontrado == True:
#             print("Turno eliminado.\n")
#         else:
#             print("No existe ese turno.\n")

#     elif opcion == 3:
#         dia_str = input("Elegir día (1 o 2): ").strip()

#         while (not dia_str.isdigit()) or (int(dia_str) < 1) or (int(dia_str) > 2):
#             if not dia_str.isdigit():
#                 print("Debe ingresar un número.")
#             else:
#                 print("Día incorrecto.")
#             dia_str = input("Elegir día (1 o 2): ").strip()

#         dia = int(dia_str)

#         if dia == 1:
#             print("\nLunes:")
#             if lunes1 == "":
#                 print("Turno 1: libre")
#             else:
#                 print(f"Turno 1: {lunes1}")

#             if lunes2 == "":
#                 print("Turno 2: libre")
#             else:
#                 print(f"Turno 2: {lunes2}")

#             if lunes3 == "":
#                 print("Turno 3: libre")
#             else:
#                 print(f"Turno 3: {lunes3}")

#             if lunes4 == "":
#                 print("Turno 4: libre")
#             else:
#                 print(f"Turno 4: {lunes4}")
#             print()
#         else:
#             print("\nMartes:")
#             if martes1 == "":
#                 print("Turno 1: libre")
#             else:
#                 print(f"Turno 1: {martes1}")

#             if martes2 == "":
#                 print("Turno 2: libre")
#             else:
#                 print(f"Turno 2: {martes2}")

#             if martes3 == "":
#                 print("Turno 3: libre")
#             else:
#                 print(f"Turno 3: {martes3}")
#             print()

#     elif opcion == 4:
#         ocupados_lunes = 0
#         if lunes1 != "":
#             ocupados_lunes += 1
#         if lunes2 != "":
#             ocupados_lunes += 1
#         if lunes3 != "":
#             ocupados_lunes += 1
#         if lunes4 != "":
#             ocupados_lunes += 1

#         libres_lunes = 4 - ocupados_lunes

#         ocupados_martes = 0
#         if martes1 != "":
#             ocupados_martes += 1
#         if martes2 != "":
#             ocupados_martes += 1
#         if martes3 != "":
#             ocupados_martes += 1

#         libres_martes = 3 - ocupados_martes

#         print("\nResumen:")
#         print(f"Lunes -> {ocupados_lunes} ocupados | {libres_lunes} libres")
#         print(f"Martes -> {ocupados_martes} ocupados | {libres_martes} libres")

#         if ocupados_lunes > ocupados_martes:
#             print("Más ocupado: lunes\n")
#         elif ocupados_martes > ocupados_lunes:
#             print("Más ocupado: martes\n")
#         else:
#             print("Mismo nivel de ocupación\n")

#     elif opcion == 5:
#         print("\nPrograma finalizado\n")



#Ejercicio 4

# vida = 100
# reloj = 12
# puertas_abiertas = 0
# alerta = False
# codigo = ""

# seguidas_fuerza = 0
# sistema_bloqueado = False

# usuario = input("Escribí tu nombre: ").strip()

# while usuario == "" or not usuario.isalpha():
#     print("Nombre inválido.")
#     usuario = input("Escribí tu nombre: ").strip()

# print(f"\n>>> Inicio de misión para {usuario}\n")

# while vida > 0 and reloj > 0 and puertas_abiertas < 3 and sistema_bloqueado == False:

#     if alerta == True and reloj <= 3 and puertas_abiertas < 3:
#         sistema_bloqueado = True

#     else:

#         print("\n--- ESTADO ACTUAL ---")
#         print(f"Vida restante: {vida}")
#         print(f"Tiempo restante: {reloj}")
#         print(f"Puertas abiertas: {puertas_abiertas} de 3")
#         print(f"Alerta activa: {'SI' if alerta else 'NO'}")
#         print(f"Código: {codigo} ({len(codigo)} caracteres)")
#         print("---------------------\n")

#         print("1 -> Forzar")
#         print("2 -> Hackear")
#         print("3 -> Descansar")

#         opcion_str = input("Elegí (1-3): ").strip()

#         while (not opcion_str.isdigit()) or (int(opcion_str) < 1) or (int(opcion_str) > 3):
#             if not opcion_str.isdigit():
#                 print("Entrada inválida.")
#             else:
#                 print("Opción incorrecta.")
#             opcion_str = input("Elegí (1-3): ").strip()

#         opcion = int(opcion_str)

#         match opcion:

#             case 1:
#                 seguidas_fuerza += 1
#                 vida -= 20
#                 reloj -= 2

#                 if seguidas_fuerza == 3:
#                     alerta = True
#                     print("\nSe trabó el mecanismo. Alarma activada.\n")

#                 else:

#                     if vida < 40:
#                         print("\nEnergía baja, posible riesgo.")
#                         riesgo_str = input("Elegí número (1-3): ").strip()

#                         while (not riesgo_str.isdigit()) or (int(riesgo_str) < 1) or (int(riesgo_str) > 3):
#                             print("Número inválido.")
#                             riesgo_str = input("Elegí número (1-3): ").strip()

#                         riesgo = int(riesgo_str)

#                         if riesgo == 3:
#                             alerta = True
#                             print("Se activó la alarma.\n")

#                     if alerta == False and puertas_abiertas < 3:
#                         puertas_abiertas += 1
#                         print("Puerta abierta.\n")
#                     else:
#                         print("No se logró abrir.\n")

#             case 2:
#                 seguidas_fuerza = 0
#                 vida -= 10
#                 reloj -= 3

#                 print("\nHackeo en proceso...")

#                 for paso in range(1, 5):
#                     codigo += "A"
#                     print(f"Paso {paso}: {codigo}")

#                 if len(codigo) >= 8 and puertas_abiertas < 3:
#                     puertas_abiertas += 1
#                     print("Acceso logrado.\n")
#                 else:
#                     print("Hackeo terminado.\n")

#             case 3:
#                 seguidas_fuerza = 0
#                 reloj -= 1

#                 vida += 15
#                 if vida > 100:
#                     vida = 100

#                 if alerta == True:
#                     vida -= 10
#                     print("\nDescanso con penalización.")
#                 else:
#                     print("\nDescanso correcto.")

#                 print(f"Vida ahora: {vida}\n")


# if puertas_abiertas == 3:
#     print("GANASTE: abriste todo.")
# elif sistema_bloqueado == True:
#     print("PERDISTE: sistema bloqueado.")
# elif vida <= 0 or reloj <= 0:
#     print("PERDISTE: sin recursos.")
# else:
#     print("Fin.")



#Ejercicio 5

# print("=== ARENA DE BATALLA ===")

# jugador = input("Ingresá el nombre: ").strip()

# while jugador == "" or not jugador.isalpha():
#     print("Nombre inválido (solo letras).")
#     jugador = input("Ingresá el nombre: ").strip()

# hp_jugador = 100
# hp_rival = 100
# curas = 3
# golpe_fuerte = 15
# golpe_rival = 12
# turno = True

# print("\n>>> COMIENZA LA PELEA <<<\n")

# while hp_jugador > 0 and hp_rival > 0:

#     print(f"\n{jugador} [{hp_jugador} HP]  vs  Rival [{hp_rival} HP]  | Pociones: {curas}")
#     print("1) Golpe fuerte")
#     print("2) Ataque rápido")
#     print("3) Curarse")

#     opcion_str = input("Elegí acción: ").strip()

#     while (not opcion_str.isdigit()) or (int(opcion_str) < 1) or (int(opcion_str) > 3):
#         if not opcion_str.isdigit():
#             print("Entrada incorrecta.")
#         else:
#             print("Opción inválida.")
#         opcion_str = input("Elegí acción: ").strip()

#     opcion = int(opcion_str)

#     match opcion:

#         case 1:
#             dano = golpe_fuerte

#             if hp_rival < 20:
#                 dano = golpe_fuerte * 1.5
#                 print("** Golpe crítico **")

#             hp_rival -= dano
#             print(f"Golpeaste por {dano:.1f} de daño")

#         case 2:
#             print("Ataque múltiple en curso...")

#             for _ in range(3):
#                 hp_rival -= 5
#                 print("- Impacto de 5 daño")

#         case 3:
#             if curas > 0:
#                 hp_jugador += 30
#                 curas -= 1
#                 print("Recuperaste 30 HP")
#             else:
#                 print("Sin pociones disponibles")

#     hp_jugador -= golpe_rival
#     print(f"El rival ataca (-{golpe_rival} HP)")

#     print("\n--- SIGUIENTE RONDA ---")


# if hp_jugador > 0:
#     print(f"\nGANADOR: {jugador}")
# else:
#     print("\nPERDISTE LA PELEA")