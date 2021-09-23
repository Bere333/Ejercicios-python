def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname":"Brenda", "lastname":"Ramos"}

    #Lista que guarde diccionarios
    super_list = [
        {"firstname":"Brenda", "lastname":"Ramos"},
        {"firstname":"Eliza", "lastname":"Santolalla"},
        {"firstname":"Sara", "lastname":"Campos"},
        {"firstname":"Richard", "lastname":"Ramos"},
        {"firstname":"Raquel", "lastname":"Resendiz"}
    ]
    #Un diccionario que contiene listas
    super_dict = {
        "natural_nums" : [1,2,3,4,5],
        "integer_nums" : [-1, -2, 0, 1, 2],
        "floating_nums" : [1.1,4.5,6.43]
    }
    #El método items() recorre al mismo tiempo keys y values de un diccionario en un ciclo for
    for key, value in super_dict.items():
        print(key, "-", value)
    
    for item in super_list:
        for firstname, lastname in item.items():
            print(firstname, "-", lastname)

if __name__ == "__main__": # entry point o punto de entrada ---> inicia la función cuando ejecutamos el archivo
    run()