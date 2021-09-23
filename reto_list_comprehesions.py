def run():
    # Múltiplos de 4, 6 y 9
    numbers = [n for n in range(1,10000) if n % 4 == 0 and n % 6 == 0 and n % 9 == 0]
    print(numbers)
    # xs =[0]
    # res = [False]*2
    # if xs:
    #     res[0] = True
    # if xs[0]:
    #     res[1] = True
    # print(res)

if __name__ == "__main__": # entry point o punto de entrada ---> inicia la función cuando ejecutamos el archivo
    run()