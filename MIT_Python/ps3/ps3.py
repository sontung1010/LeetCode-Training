# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Tung Do
# Collaborators : <your collaborators>
# Time spent    : 5 hours

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence and the values are integer counts, for the number of times that an element is repeated in the sequence.
    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.
    You may assume that the input word is always either a string of letters, or the empty string "". You may not assume that the string will only contain lowercase letters, so you will have to handle uppercase and mixed case strings appropriately.
	The score for a word is the product of two components:
	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word and n is the hand length when the word was played
	Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()
    wordlen = len(word)
    freq = get_frequency_dict(word)
    first_comp = 0
    for i in freq:
        first_comp = first_comp + freq[i]*SCRABBLE_LETTER_VALUES[i]
    sec_comp = 7*wordlen - 3*(n - wordlen)
    if sec_comp < 1:
        sec_comp = 1

    return first_comp*sec_comp

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.
    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.
    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note, ceil(n/3) means the smallest integer not less than n/3).
    Hands are represented as dictionaries. The keys are letters and the values are the number of times the particular letter is repeated in that hand.
    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    hand['*'] = 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand
#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as many times as the letter appears in word. Letters in word that don't appear in hand should be ignored. Letters that appear in word more times than in hand should never result in a negative count; instead, set the count in the returned hand to 0 (or remove the letter from the dictionary, depending on how your code is structured).
    Updates the hand: uses up the letters in the given word and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    new_hand_temp = hand.copy()
    word = get_frequency_dict(word.lower())
    for i in new_hand_temp:
        new_hand_temp[i] = new_hand_temp[i] - word.get(i, 0)
    new_hand = new_hand_temp.copy()
    for i in new_hand_temp:
        if new_hand_temp[i] == 0:
            del(new_hand[i])
    return new_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    new_hand = {}
    new_list = []
    word = word.lower()
    if '*' in word:
        star_index = word.index('*')
        for x in word_list:
            if len(x) == len(word):
                if x[star_index] in VOWELS:
                    if x[0:star_index] == word[0:star_index] and x[star_index+1:len(x)] == word[star_index+1:len(word)]:
                        return True
                        break
                    elif star_index == 0 and x[1:len(x)] == word[1:len(word)]:
                        return True
                        break
                    elif star_index == len(x) and x[0:len(x)-1] == word[0:len(x)-1]:
                        return True
                        break

    else:
        if word not in word_list:
            return False
        elif word in word_list:
            word = get_frequency_dict(word)
            for i in word:
                if i not in hand:
                    return False
                else:
                    new_hand[i] = hand.get(i,0) - word.get(i, 0)
            for i in new_hand:
                if new_hand[i] < 0:
                    return False
                else:
                    return True

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string-> int)
    returns: integer
    """
    sum = 0
    for i in hand:
        sum = sum + hand[i]
    return sum

def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.
    * The user may input a word.
    * When any word is entered (valid or invalid), it uses up letters from the hand.
    * An invalid word is rejected, and a message is displayed asking the user to choose another word.
    * After every valid word: the score for that word is displayed, the remaining letters in the hand are displayed, and the user is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters. The user can also finish playing the hand by inputing two exclamation points (the string '!!') instead of a word.
      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
    """
    # Keep track of the total score
    # As long as there are still letters left in the hand:
        # Display the hand
        # Ask user for input
        # If the input is two exclamation points:
            # End the game (break out of the loop)
        # Otherwise (the input is not two exclamation points):
            # If the word is valid:
                # Tell the user how many points the word earned,
                # and the updated total score
            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
            # update the user's hand by removing the letters of their inputted word
    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    # Return the total score as result of function
    total_score = 0
    score = 0
    global sub_time
    global replay_time
    if sub_time == 0:
        print("\n")
        print("Current Hand: ", end="")
        display_hand(hand)
        sub_choice = input("Would you like to substitute a letter? ")
        if sub_choice == "yes":
            sub_time += 1
            letter = input("Which letter would you like to replace: ")
            hand = substitute_hand(hand, letter)
    save_replay_hand = hand
    while len(hand) != 0:
        print("\n")
        print("Current Hand: ", end="")
        display_hand(hand)
        word = input("Please enter a word, or \"!!\" to indicate you are done: ")
        if is_valid_word(word, hand, word_list):
            score = get_word_score(word, len(hand))
            total_score = total_score + score
            print("\"" + word + "\" earn " + str(score) + " points. Total: " + str(total_score) + " points")
        elif word == "!!":
            print("Total score for this hand: " + str(total_score) + " points")
            print("----------")
            break
        else:
            print("That is not a valid word. Please choose another word.")
        hand = update_hand(hand, word)
    if len(hand) <= 0:
        print("\nRan out of letters")
        print("Total score for this hand: " + str(total_score))
        print("----------")
    if replay_time == 0:
        replay_choice = input("Would you like to replay the hand? ")
        if replay_choice == "yes":
            replay_time += 1
            hand = save_replay_hand
            replay_score = 0
            while len(hand) != 0:
                print("\n")
                print("Current Hand: ", end="")
                display_hand(hand)
                word = input("Please enter a word, or \"!!\" to indicate you are done: ")
                if is_valid_word(word, hand, word_list):
                    score = get_word_score(word, len(hand))
                    replay_score = replay_score + score
                    print("\"" + word + "\" earn " + str(score) + " points. Total: " + str(replay_score) + " points")
                elif word == "!!":
                    print("Total score for this hand: " + str(replay_score) + " points")
                    print("----------")
                    break
                else:
                    print("That is not a valid word. Please choose another word.")
                hand = update_hand(hand, word)
            if len(hand) <= 0:
                print("\nRan out of letters")
                print("Total score for this hand: " + str(replay_score))
                print("----------")
            if total_score < replay_score:
                total_score = replay_score
    return total_score
#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user) with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter should be different from user's choice, and should not be any of the letters already in the hand.
    If user provide a letter not in the hand, the hand should be the same.
    Has no side effects: does not mutate hand.
    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were already in the hand.
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    if letter in hand.keys():
        q = hand[letter]
        hand.pop(letter)
        new_choice_list = VOWELS + CONSONANTS
        new_choice_list = list(new_choice_list)
        a = []
        for char in hand.keys():
            a.append(char)
        new_vowel = new_choice_list[:]
        for e in new_choice_list:
            if e in a:
                new_vowel.remove(e)
        new_vowel = ''.join(new_vowel)
        x = random.choice(new_vowel)
        hand[x] = q
        return hand
    else:
        return hand

def play_game(word_list):
    """
    Allow the user to play a series of hands
    * Asks the user to input a total number of hands
    * Accumulates the score for each hand into a total score for the entire series
    * For each hand, before playing, ask the user if they want to substitute one letter for another. If the user inputs 'yes', prompt them for their desired letter. This can only be done once during the game. Once the substitue option is used, the user should not be asked if they want to substitute letters in the future.
    * For each hand, ask the user if they would like to replay the hand. If the user inputs 'yes', they will replay the hand and keep the better of the two scores for that hand.  This can only be done once during the game. Once the replay option is used, the user should not be asked if they want to replay future hands. Replaying the hand does not count as one of the total number of hands the user initially wanted to play.
            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
    * Returns the total score for the series of hands
    word_list: list of lowercase strings
    """
    hand_series = int(input("Enter total number of hands: "))
    total = 0
    global sub_time
    global replay_time
    for times in range(0,hand_series):
        hand = deal_hand(HAND_SIZE)
        point = play_hand(hand, word_list)
        total = total + point
    print("Total score over all hands: " + str(total))

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    sub_time = 0
    replay_time = 0
    word_list = load_words()
    play_game(word_list)
