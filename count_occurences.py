# count_occurences
# :information_source: Already implemented via list.count().

# Counts the occurrences of a value in an list.

# Uses the list comprehension to increment a counter each time you encounter the specific value inside the list.

def count_occurrences(lst, val):
    print(type(val))
    print(len([x for x in lst if x == val and type(x) == type(val)]))
    return len([x for x in lst if x == val and type(x) == type(val)])


count_occurrences([1, 1, 2, 1, 2, 3], 1) # 3