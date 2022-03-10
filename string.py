mensaje = "Hola"
mensaje += " "
mensaje += "Fredy"
print(mensaje)

print("Concatenación:")

mensaje = "Hola"
espacio = " "
nombre = "Fredy"
print(mensaje + espacio + nombre)

numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("El resultado de la suma es: " + resultado)

print("Busqueda")
mensaje = "Hola Fredy"
buscar_subcadena = mensaje.find("Fredy")
print(buscar_subcadena)

mensaje = "Hola Fredy"
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)

print("Comparación:")
mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)
