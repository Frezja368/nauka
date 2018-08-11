def checkio(words: str) -> bool:
    splitted_words = words.split()
    count = 0
    print (splitted_words)
    print ("TO GÓWNO", len(splitted_words), "CO tu", splitted_words.index(splitted_words[::-1]))
    for w in splitted_words:
        if w.isalpha():
            count += 1
            if count >= 3:
                return True
            if len(splitted_words) == (splitted_words.index(splitted_words[-1])) and count < 3:
               print ("Mam dość")
               return False
        else:
            count = 0
    
            
            
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
