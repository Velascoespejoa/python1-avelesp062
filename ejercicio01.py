# from datetime import datetime
# #Metodo que pide y verifica nombre
# def pideNombre():
#     nombre=input("Escribe tu nombre: ")
#     if nombre == '':
#         print("Debes ingresar algun valor")
#         pideNombre()
#     return nombre
# #Metodo que pide, verifica fechaNacimiento y devuelve un string con nombre y años
# def pideFecha(nombre):
#     try:
#         fecha = int(input("año de nacimiento: "))
        
#     except:
#         print("No has ingresado un numero")
#         pideFecha()
#     hoy = datetime.today()
#     añostotal = hoy.year - fecha
#     print(f"¡Hola {nombre}! - Naciste hace, {añostotal} años ")
    


# nombre = pideNombre()
# pideFecha(nombre)


from datetime import datetime

def pideNombre():
    nombre = None
    while True:
        if(nombre == None):
            nombre = input("Dame su nombre: ")
        if(nombre==""):
            print("Debes ingresar algun valor")
            nombre = None       
        else:
            try:
                fecha = int(input("año de nacimiento: "))
            except ValueError:
                print("No has ingresado ningun valor o no es un numero")
            else:
                hoy = datetime.today()
                añostotal = hoy.year - fecha
                print(f"¡Hola {nombre}! - Naciste hace, {añostotal} años ")
                return False

pideNombre()