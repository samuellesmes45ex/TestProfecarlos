def menu():
    print(""" Bienvenido a este Cajero Automatico
    
1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir...
 Ingrese una opcion de 1 - 4:   """ )



def leer_opcion():
    opcion = input()
    while(not opcion.isdigit() or int (opcion)
    <1 or int(opcion) > 4):
        print("Opción inválida. Digite un numero de 1 a 4.")
        menu()
        opcion = input()
    return int(opcion)

def Depositar_dinero(saldo):
    try:
        monto = float(input("Ingrese un monto a Depositar: "))
        if monto <= 0:
            print("Error, ingrese un valor mayor a 0")

        elif monto > 0: 
            saldo += monto
            print(f"Tu nuevo saldo es: $ {saldo}")

    except:ValueError



def Retirar_dinero(saldo):
    try:
        monto = float(input("Ingrese un monto a retirar: "))

        if monto < 0:
            print("Error, El valor debe ser mayo a 0")
            return main

        elif monto > 0: 
            saldo -= monto
            print("Dinero retirado")
            print(f"Este es su nuevo saldo: {saldo} ")
            return main

    except ValueError:
        print("Error")



def Consultar_saldo(saldo):
    print(f"Su saldo actual es {saldo}")
    return main

def main():
    saldo = 1000
    while True:
        menu()
        opcion = leer_opcion()
        if opcion == 1:
            Consultar_saldo(saldo)
        elif opcion == 2:
            Depositar_dinero(saldo)
        elif opcion == 3:
            Retirar_dinero(saldo)
        else:
            print("Gracias por usar este cajero automatico")

        input("\n\nPresione cualquier tecla para continuar...")

main()
