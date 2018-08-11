def checkio(data: str) -> bool:
    checker = bool(len(data) >= 10)
    digit_bool = any(n.isdigit() for n in data)
    upper_bool = any(u.isupper() for u in data)
    lower_bool = any(l.islower() for l in data)
    print (checker, digit_bool, upper_bool, lower_bool)
    if checker is True:
        if digit_bool is True:
            if  upper_bool is True:
                if  lower_bool is True: 
                  return True
                else:
                   return False
            else:
               return False
        else:
            return False
    else:
        return False
#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")