def pideNum():
    try:
        num = int(input("Dame un numero: "))
    except:
        print("No has ingresado un numero")
        pideNum()
    for numero in range(0,num+1,2):
        print(numero)

pideNum()
