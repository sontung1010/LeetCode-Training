# Problem Set 2, hangman.py
# Name: Tung Do
# Collaborators:
# Time spent: 5 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are lowercase
    letters_guessed: list (of letters), which letters have been guessed so far; assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed; False otherwise
    '''
    a = []
    for char in secret_word:
        if char in letters_guessed:
            a.append('t')
        else:
            a.append('f')
    b = []
    for i in range(len(a)):
        b.append('t')
    b = ''.join(b)
    a = ''.join(a)
    if a == b:
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents which letters in secret_word have been guessed so far.
    '''
    a = []
    for char in secret_word:
        if char in letters_guessed:
            a.append(char)
        else:
            a.append('_ ')
    a = ''.join(a)
    return a

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not yet been guessed.
    '''
    a = list(string.ascii_lowercase)
    for char in string.ascii_lowercase:
        if char in letters_guessed:
            a.remove(char)

    a = ''.join(a)
    return a



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many letters the secret_word contains and how many guesses s/he starts with.
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Remember to make sure that the user puts in a letter!
    * The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the partially guessed word so far.
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    warning = 3
    print("You have " + str(warning) + " warnings left.")
    print("--------------")
    guess_time = 6
    print("You have " + str(guess_time) + " guesses left.")
    letters_guessed = []
    print("Available letters: " + get_available_letters(letters_guessed))
    vowels = ['a','i','e','o','u']

    while not is_word_guessed(secret_word, letters_guessed):
        a = input("Please guess a letter: ")
        a = str.lower(a)
        if  str.isalpha(a) and a in get_available_letters(letters_guessed):
            letters_guessed.append(a)
            b = get_guessed_word(secret_word, letters_guessed)
            if a in secret_word:
                print("Good guess: " + b)
            else:
                print("Oops! That letter is not in my word: " + b)
                if a in vowels:
                    guess_time -= 2
                else:
                    guess_time -= 1
        elif str.isalpha(a) and a not in get_available_letters(letters_guessed):
            warning -= 1
            b = get_guessed_word(secret_word, letters_guessed)
            if warning >= 0:
                print("Oops! You've already guessed that letter. You have " + str(warning) + " warnings left: " + b)
            else:
                print("Oops! You've already guessed that letter. You have no warnings left")
                print("so you lose one guess: " + b)
                guess_time -= 1
        else:
            warning -= 1
            b = get_guessed_word(secret_word, letters_guessed)
            if warning >= 0:
                print("Oops! That is not a valid letter. You have " + str(warning) + " warnings left: " + b)
            else:
                print("Oops! That is not a valid letter. You have no warnings left")
                print("so you lose one guess: " + b)
                guess_time -= 1
        print("--------------")
        if guess_time <= 0:
            print("Sorry, you ran out of guesses. The word was " + secret_word + ".")
            break
        if is_word_guessed(secret_word, letters_guessed):
            a = len(set(list(secret_word)))
            score = guess_time*a
            print("Congratulations, you won!")
            print("Your total score for this game is: " + str(score))
            break
        print("You have " + str(guess_time) + " guesses left.")
        print("Available letters: " + get_available_letters(letters_guessed))


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the corresponding letters of other_word, or the letter is the special symbol, and my_word and other_word are of the same length; False otherwise:
    '''
    my_word = list(my_word)
    for i in my_word:
        if i == ' ':
            my_word.remove(i)
    other_word = list(other_word)
    r = []
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] == "_":
                continue
            else:
                if my_word[i] == other_word[i]:
                    r.append('t')
                else:
                    r.append('f')
        c = []
        for i in range(len(r)):
            c.append('t')
        r = ''.join(r)
        c = ''.join(c)
        if r == c:
            return True
        else:
            return False
    else:
        return False

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions at which that letter occurs in the secret word are revealed. Therefore, the hidden letter(_ ) cannot be one of the letters in the word that has already been revealed.

    '''
    count = 0
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word, end = " ")
            count = 1
        else:
            continue
    if count == 0:
        print("No matches found")
    print("\n")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many letters the secret_word contains and how many guesses s/he starts with.
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
    * The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the partially guessed word so far.
    * If the guess is the symbol *, print out all words in wordlist that matches the current guessed word.
    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    warning = 3
    print("You have " + str(warning) + " warnings left.")
    print("--------------")
    guess_time = 6
    print("You have " + str(guess_time) + " guesses left.")
    letters_guessed = []
    #b = get_guessed_word(secret_word, letters_guessed)
    b = []
    print("Available letters: " + get_available_letters(letters_guessed))
    vowels = ['a','i','e','o','u']

    while not is_word_guessed(secret_word, letters_guessed):
        a = input("Please guess a letter: ")
        a = str.lower(a)
        if  str.isalpha(a) and a in get_available_letters(letters_guessed):
            letters_guessed.append(a)
            b = get_guessed_word(secret_word, letters_guessed)
            if a in secret_word:
                print("Good guess: " + b)
            else:
                print("Oops! That letter is not in my word: " + b)
                if a in vowels:
                    guess_time -= 2
                else:
                    guess_time -= 1
        elif str.isalpha(a) and a not in get_available_letters(letters_guessed):
            warning -= 1
            b = get_guessed_word(secret_word, letters_guessed)
            if warning >= 0:
                print("Oops! You've already guessed that letter. You have " + str(warning) + " warnings left: " + b)
            else:
                print("Oops! You've already guessed that letter. You have no warnings left")
                print("so you lose one guess: " + b)
                guess_time -= 1
        elif a == "*" and not bool(b):
            print("Can't provide any matches word without correct guess")
        elif a == "*" and bool(b):
            print("Possible word matches are: ")
            show_possible_matches(b)
            #print("\n")
        else:
            warning -= 1
            b = get_guessed_word(secret_word, letters_guessed)
            if warning >= 0:
                print("Oops! That is not a valid letter. You have " + str(warning) + " warnings left: " + b)
            else:
                print("Oops! That is not a valid letter. You have no warnings left")
                print("so you lose one guess: " + b)
                guess_time -= 1
        print("--------------")
        if guess_time <= 0:
            print("Sorry, you ran out of guesses. The word was " + secret_word + ".")
            break
        if is_word_guessed(secret_word, letters_guessed):
            a = len(set(list(secret_word)))
            score = guess_time*a
            print("Congratulations, you won!")
            print("Your total score for this game is: " + str(score))
            break
        print("You have " + str(guess_time) + " guesses left.")
        print("Available letters: " + get_available_letters(letters_guessed))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
