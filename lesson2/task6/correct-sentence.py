def correct_sentence(text: str) -> str:
    text=text[0].upper()+text[1:]
    if not text.endswith('.'):
        text +='.'
    return text


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends")
    assert correct_sentence("Greetings, friends") 
    assert correct_sentence("Greetings, friends.") 
    assert correct_sentence("hi")
    print("Coding complete? Click 'Check' to earn cool rewards!")