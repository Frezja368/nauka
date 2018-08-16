def checkio(text: str) -> str:
 
      text = text.lower()
    dict_with_lett = {}
    for letter in text:
        if letter.isalpha():
            counting =text.count(letter)
            dict_with_lett[letter]= counting

    sorted_dict= sorted(dict_with_lett.items(), key =lambda x: x[0])
    sorted_l = sorted(sorted_dict, key = lambda x: (-x[1], x[0]))
    first_tuple = [elem[0] for elem in sorted_l]
    return first_tuple[0]




if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
