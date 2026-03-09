# calculadora.py
# Programa principal que usa el módulo operaciones

# Importamos las funciones desde el otro archivo
from operaciones import suma, resta

def mostrar_menu():
    """Muestra el menú de la calculadora."""
    print("\n--- Calculadora Básica ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

def main():
    """Función principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '3':
            print("¡Hasta luego!")
            break

        if opcion not in ['1', '2']:
            print("Opción no válida. Intenta de nuevo.")
            continue

        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Por favor, ingresa números válidos.")
            continue

        if opcion == '1':
            resultado = suma(num1, num2)
            print(f"El resultado de {num1} + {num2} es: {resultado}")
        elif opcion == '2':
            resultado = resta(num1, num2)
            print(f"El resultado de {num1} - {num2} es: {resultado}")

if __name__ == "__main__":
    main()