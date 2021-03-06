def divisors(number):
    try:
        if number < 0:
            raise ValueError("No se pueden ingresar números negativos.")
        divisors = []
        for n in range(1, number + 1):
            if number % n == 0:
                divisors.append(n)
        return divisors
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Termino programa")
    except ValueError:
        print("Debes ingresar un valor de tipo número /ᐠ｡ꞈ｡ᐟ\.")

if __name__ == "__main__": # entry point o punto de entrada ---> inicia la función cuando ejecutamos el archivo
    run()