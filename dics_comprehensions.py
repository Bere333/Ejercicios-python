def run():
    # dic_squares = {}
    # for n in range(1, 101):
    #     if n % 3 != 0:
    #         dic_squares[n] = n**3

    # Dictionary comprehensions
    dic_squares = {n:n**3 for n in range(1, 101) if n % 3 != 0}
    print(dic_squares)

if __name__ == "__main__": # entry point o punto de entrada ---> inicia la función cuando ejecutamos el archivo
    run()