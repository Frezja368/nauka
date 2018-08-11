def sun_angle(time):
    a, b, c, d, e = time
    b = str(b)
    if 06 <= b and b >= 12 :
        print (b)
        
    if "12:00" <= time >= "18:00":
        print ("woow")
    if "18:00" <= time > "6:00":
        print ("I don't see the sun!")
    #replace this for solution
    

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")