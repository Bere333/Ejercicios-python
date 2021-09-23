def run():
    # Devuelve los números al cuadrado que NO son divisibles por 3
    # squares = []
    # for n in range(1,101):
    #     if n % 3 != 0:
    #         squares.append(n**2)
    # print(squares)

    # List comprehensions
        squares = [n**2 for n in range(1,101) if n % 3 != 0]
        print(squares)

if __name__ == "__main__": # entry point o punto de entrada ---> inicia la función cuando ejecutamos el archivo
    run()