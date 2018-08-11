def safe_pawns(pawns: set) -> int:
    rows = [1, 2, 3, 4, 5, 6, 7, 8]
    columns = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in columns:
        
    print (rows, columns)
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")