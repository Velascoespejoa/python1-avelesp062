def pideNombre():
    while(True):
        nombre = input("dame tu nombre: ")
        print(nombre.upper())
        print(f"tu nombre tiene {len(nombre)} letras")
        for letra in nombre:
            print(nombre)
        continuar = input("Pulse A para repetir: ")
        if(continuar !="A" and continuar !="a"):
            return False
        
pideNombre()