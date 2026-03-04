import random
hand = {'i':2, 'k':1, 'l':1, 'm':1, 'v':1, 'u':1}
print(hand)
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
letter = 'v'
print(letter)

if letter in hand.keys():
    q = hand[letter]
    hand.pop(letter)
    new_choice_list = VOWELS + CONSONANTS
    new_choice_list = list(new_choice_list)
    print(new_choice_list)
    a = []
    for char in hand.keys():
        a.append(char)
    new_vowel = new_choice_list[:]
    for e in new_choice_list:
        if e in a:
            new_vowel.remove(e)
    new_vowel  = ''.join(new_vowel)
    print(new_vowel)
    x = random.choice(new_vowel)
    print("x = " + x)
    hand[x] = q
    print(hand)
