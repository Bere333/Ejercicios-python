def divisors(number):
    for n in range(1, number + 1):
        if number % n == 0:
            print(n)

def run():
    divisors(9)

if __name__ == "__main__": # entry point o punto de entrada ---> inicia la función cuando ejecutamos el archivo
    run()