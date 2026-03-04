dictionary = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26,'a':27,'b':28,'c':29,'d':30,'e':31,'f':32,'g':33,'h':34,'i':35,'j':36,'k':37,'l':38,'m':39,'n':40,'o':41,'p':42,'q':43,'r':44,'s':45,'t':46,'u':47,'v':48,'w':49,'x':50,'y':51,'z':52}

sym = "!@#$%^&*()-_+={}[]|\:;'<>?,./\" "

def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a character shifted down the alphabet by the input shift. The dictionary should have 52 keys of all the uppercase letters and all the lowercase letters only.
    shift (integer): the amount by which to shift every letter of the alphabet. 0 <= shift < 26
    Returns: a dictionary mapping a letter (string) to another letter (string).
    '''
    # dictionary = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26,'a':27,'b':28,'c':29,'d':30,'e':31,'f':32,'g':33,'h':34,'i':35,'j':36,'k':37,'l':38,'m':39,'n':40,'o':41,'p':42,'q':43,'r':44,'s':45,'t':46,'u':47,'v':48,'w':49,'x':50,'y':51,'z':52}
    new_dict = dictionary
    if shift >= 0 and shift < 26:
        for i in new_dict:
            if new_dict[i] > shift:
                new_dict[i] = new_dict[i] - shift
            elif new_dict[i] <= shift:
                new_dict[i] = 52 - (shift - new_dict[i])

    return new_dict


if __name__ == '__main__':

    case = []
    result = []
    string = "Hello World!"
    vowels = "aeiou"
    vowels = list(vowels)
    d = "eaiuo"
    d = list(d)
    transpose_dict = dict(zip(vowels, d))
    for char in string:
        if char in transpose_dict:
            if char.isupper():
                case.append(1)
            else:
                case.append(0)
            result.append(transpose_dict[char])
        elif char in sym:
            result.append(char)
            case.append('-')
        else:
            if char.isupper():
                case.append(1)
            else:
                case.append(0)
            result.append(char)
    for i in range(0, len(case)-1):
        if case[i] == 0:
            result[i] = result[i].lower()
        elif case[i] == 1:
            result[i] = result[i].upper()
    result = "".join(result)
    print(result)
