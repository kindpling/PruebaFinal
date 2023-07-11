departamentos ='''
-----departamento-----
1.-tipo A
1.-tipo B
1.-tipo C
1.-tipo D
'''    


run = ()
matriz = [
    ["[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]"],
    ]
# Funciones auxiliares
def menu():  
    print("----- MENÚ PRINCIPAL -----")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    
def comprar_departamento():
    piso = int(input("Ingresa el número de piso (1-10): "))
    print('''
-----departamento-----
1.-tipo A
2.-tipo B
3.-tipo C
4.-tipo D
'''   )
    departamento = int(input("Ingresa el tipo de departamento: "))
    # Validar piso y tipo de departamento ingresados
    if piso < 1 or piso > 10:
        print("Piso inválido. Por favor, ingresa un número de piso válido (1-10).")
        return
    
    if matriz[piso - 1][departamento - 1] == "[ ]":
        # Solicitar datos del usuario
        rut = input("Ingrese su RUT: ")
        matriz[piso - 1][departamento - 1] = "[X]"
    
    # Lógica para comprar el departamento seleccionado
    print(f"Has seleccionado el departamento {departamento} en el piso {piso}.")

def mostrar_departamentos_disponibles():
    print("                tipo         ")
    print("       a      b      c      d")
    for i, fila in enumerate(reversed(matriz), start=1):
        print(f"{i:2d}: {fila}")    
    #A RIVERS SE LE CAYO

def ver_listado_compradores():
    # Lógica para ver el listado de compradores
    print("Has seleccionado la opción Ver listado de compradores")

def mostrar_ganancias_totales():
    # Lógica para mostrar las ganancias totales
    print("Has seleccionado la opción Mostrar ganancias totales")

def salir():
    global continuar
    continuar = False
    print("Saliendo del programa...")

continuar = True
# Menú principal
while continuar:
    menu()

    opcion = input("Ingresa el número de opción que deseas ejecutar: ")

    if opcion == "1":
        comprar_departamento()
    elif opcion == "2":
        mostrar_departamentos_disponibles()
    elif opcion == "3":
        ver_listado_compradores()
    elif opcion == "4":
        mostrar_ganancias_totales()
    elif opcion == "5":
        salir()
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
        
        
        
        
        
        
        
        

