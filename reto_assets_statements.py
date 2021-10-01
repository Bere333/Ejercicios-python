def divisors(number):
        divisors = []
        for n in range(1, number + 1):
            if number % n == 0:
                divisors.append(n)
        return divisors

def run():
        num = int(input("Ingresa un número: "))
        assert num > 0, "Debes ingresar un número positivo"
        print(divisors(num))
        print("Termino programa")

if __name__ == "__main__": # entry point o punto de entrada ---> inicia la función cuando ejecutamos el archivo
    run()