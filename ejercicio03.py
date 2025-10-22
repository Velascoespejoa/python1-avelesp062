# def pideNum():
#     try:
#         num = int(input("Dame un numero: "))
#     except:
#         print("No has ingresado un numero")
#         return pideNum()
#     for numero in range(0,num+1,2):
#         print(numero)

# pideNum()

def pideNum():
    num = None
    terminar = True
    while num == None and terminar:
        try:
            num = int(input("Dame un número: "))
        except ValueError:
            print("Debe de ser un número")
        else:
            print(f"Números pares hasta {num}:")
            for numero in range(0,num+1,2):
                print(numero)
            confirmar = input("Pulse S para Salir: ")
            if(confirmar == "s" or confirmar == "S"):
                terminar = False
            num = None  


pideNum()

