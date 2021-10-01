def divisors(number):
        divisors = []
        for n in range(1, number + 1):
            if number % n == 0:
                divisors.append(n)
        return divisors

def run():
        num = input("Ingresa un número: ")
        assert num.isnumeric(), "Debes ingresar un número"
        print(divisors(int(num)))
        print("Termino programa")

if __name__ == "__main__": # entry point o punto de entrada ---> inicia la función cuando ejecutamos el archivo
    run()