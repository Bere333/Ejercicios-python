# :information_source: Already implemented via itertools.zip_longest()

# Creates a list of elements, grouped based on the position in the original lists.

# Use max combined with list comprehension to get the length of the longest list in 
# the arguments. Loops for max_length times grouping elements. If lengths of lists vary 
# fill_value is used. By default fill_value is None.

def zip(list_1, list_2, list_3):
    all_list = [list_1, list_2, list_3]
    longest_list = [ len(item) for item in all_list]
    max_num = max(longest_list) 
    #print(max_num)

    final_list = []
    for i in range(0, 2):

        if list_1[i] == "is not defined":
            final_list.append(list((None, list_2[i], list_3[i])))
            
        else:
            final_list.append(list((list_1[i], list_2[i], list_3[i])))

        #     final_list.append(list((None, list_2[i], list_3[i])))



    print(final_list)
    # Respuesta correcta
    # def zip(*args, fillvalue=None):
        # max_length = max([len(lst) for lst in args])
        # result = []
        # for i in range(max_length):
        #     result.append([
        #         args[k][i] if i < len(args[k]) else None for k in range(len(args))
        #     ])
        # return result

        




if __name__ == "__main__": # entry point o punto de entrada ---> inicia la función cuando ejecutamos el archivo
    zip(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]] ✔
    zip(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]] 
    # zip(['a'], [1, 2], [True, False], fill_value = '_') # [['a', 1, True], ['_', 2, False]]