def checkio(number: int) -> int:
    list_of_numbers = list(str(number))
    new_list= list(map(int, list_of_numbers))
    product =1
    for i in new_list:
        if i == 0:
            i = i+1
            product = product*i
        else:
            product = product*i
            print (product)
    return product

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
