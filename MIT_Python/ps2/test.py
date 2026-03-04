WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()



def match(a, b):
    a = list(a)
    for i in a:
        if i == ' ':
            a.remove(i)
    #print(a)
    b = list(b)
    #print(b)
    r = []
    if len(a) == len(b):
    #    print("length are equal")
        for i in range(len(a)):
            #print("a[i] = " + a[i])
            if a[i] == "_":
               continue
            else:
                if a[i] == b[i]:
                    r.append('t')
                else:
                    r.append('f')
        c = []
        for i in range(len(r)):
            c.append('t')
        r = ''.join(r)
    #    print(r)
        c = ''.join(c)
    #    print(c)
        if r == c:
            return True
        else:
            return False
    else:
    #    print("length not equal")
        return False

def show(w):
    count = 0
    for word in wordlist:
        if match(w, word):
            print(word)
            count = 1
        else:
            #print("No matches found")
            continue
    if count == 0:
        print("No matches found")


#print(match('a_ _ lr', 'apple'))
show("a_ pl_ ")
