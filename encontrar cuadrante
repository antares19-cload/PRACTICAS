# determinar cuadrante (x, Y)
def determinar_cuadrante(x, y):
    # comprueba que la cordenada no es  0
    if x == 0 or y == 0:
        return ("Error: Las coordenadas no deben ser cero.")

    # ubica el cuadrante
    if x > 0 and y > 0:
        return "El punto se encuentra en el cuadrante I"
    elif x < 0 and y > 0:
        return "El punto se encuentra en el cuadrante II"
    elif x < 0 and y < 0:
        return "El punto se encuentra en el cuadrante III"
    elif x > 0 and y < 0:
        return "El punto se encuentra en el cuadrante IV"

def main():
    while True:
        try:
            #pide las cordenadas al usuario
            x = float(input("ingresa x:"))
            y = float(input("ingresa y:"))
            #determina donde se e ncuentra el cuadrante 
            resultado = determinar_cuadrante(x, y)
            #imprime el resultado de la operacion y muestra donde se encuentra el cuadrante 
            print(resultado)
        except ValueError:
            print("error: porfavor, ingrese valore numericos validos.")
        except KeyboardInterrupt:
            print("\n Programa terminado.")
        break
if __name__ == "__main__":
    main()
