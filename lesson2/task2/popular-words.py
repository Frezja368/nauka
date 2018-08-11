def popular_words(text: str, words: list) -> dict:
    # your code here
    splitted_words = text.split()
    lower_splitted = [x.lower() for x in splitted_words]
    result = dict((w, lower_splitted.count(w)) for w in words)

    
                #number_of_words = splitted_words.count(i)
                #new_dict = {}
                #new_dict [i] = number_of_words
                #print (new_dict)
       
     
    return result


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
