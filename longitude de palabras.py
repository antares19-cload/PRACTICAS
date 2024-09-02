palabra = input("introducle la palabra: ")

longitud = len(palabra)

if 4 <= longitud <= 8:
    print("la palabra es correcta.")

elif longitud <= 4 :
    print(f"Hacen falta letras solo contiene {longitud} letras.")
                
else:
    print(f"Sobran letras. Tiene {longitud} letras.")