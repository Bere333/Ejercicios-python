# values_only
# Function which accepts a dictionary of key value pairs and returns a new flat list of only the values.

# Uses the .items() function with a for loop on the dictionary to track both the key and value of 
# the iteration and returns a new list by appending the values to it. Best used on 1 level-deep 
# key:value pair dictionaries and not nested data-structures.

def values_only(ages):
    list_ages = []
    for name, age in ages.items():
        list_ages.append(age)
    return list_ages
        

ages = {
     "Peter": 10,
     "Isabel": 11,
     "Anna": 9,
}

if __name__ == "__main__": # entry point o punto de entrada ---> inicia la función cuando ejecutamos el archivo
    values_only(ages) # [10, 11, 9]