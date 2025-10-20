from datetime import datetime

def pideNombre():
    nombre=input("Escribe tu nombre: ")
    if nombre == '':
        print("Debes ingresar algun valor")
        pideNombre()
    return nombre

def pideFecha(nombre):
    try:
        fecha = int(input("año de nacimiento: "))
        
    except:
        print("No has ingresado un numero")
        pideFecha()
    hoy = datetime.today()
    añostotal = hoy.year - fecha
    print(f"¡Hola {nombre}! - Naciste hace, {añostotal} años ")
    


nombre = pideNombre()
pideFecha(nombre)



