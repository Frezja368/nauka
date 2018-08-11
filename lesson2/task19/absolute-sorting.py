def checkio(numbers_array: tuple) -> list:
    new_array = []
    negative_numbers = []
    for n in numbers_array:
        if n < 0:
            negative_numbers.append(n)
            absolute_value= abs(n)
            new_array.append( absolute_value)
            new_array.sort()
           
        else:
            absolute_value= abs(n)
            new_array.append( absolute_value)
            new_array.sort()
            
    print (negative_numbers)       
    for x in negative_numbers:
        for y in new_array:
            if abs(x) == y:
                z=-1*y
                new_array[new_array.index(y)]=z
    return new_array

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")