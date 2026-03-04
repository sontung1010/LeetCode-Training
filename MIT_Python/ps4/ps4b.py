# Problem Set 4B
# Name: Tung Do
# Collaborators:
# Time Spent: 10:00

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing the list of words to load
    Returns: a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while to finish.
    '''
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    # print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring capitalization and punctuation
    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    Returns: True if word is in word_list, False otherwise
    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip("!@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

dictionary = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26,'a':27,'b':28,'c':29,'d':30,'e':31,'f':32,'g':33,'h':34,'i':35,'j':36,'k':37,'l':38,'m':39,'n':40,'o':41,'p':42,'q':43,'r':44,'s':45,'t':46,'u':47,'v':48,'w':49,'x':50,'y':51,'z':52}

sym = "!@#$%^&*()-_+={}[]|\:;'<>?,./\" "

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
        text (string): the message's text
        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''

        self.message_text = text
        self.valid_words = load_words('words.txt')

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        Returns: a COPY of self.valid_words
        '''
        valid_words_copy = self.valid_words
        return valid_words_copy

    def build_shift_dict(self, shift):
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


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the alphabet by some number of characters determined by the input shift
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26
        Returns: the message text (string) in which every character is shifted down the alphabet by the input shift
        '''
        # print(self.message_text)
        # print(dictionary)
        case = []
        result = []
        text = []
        for char in self.message_text:
            if char in dictionary:
                if char.isupper():
                    case.append(1)
                else:
                    case.append(0)
                result.append(dictionary[char])
            if char in sym:
                result.append(char)
                case.append('-')
        # print(result)
        # print(case)
        d2 = self.build_shift_dict(shift)
        # print(d2)
        for num in result:
            if str(num) in sym:
                text.append(str(num))
            for key, value in d2.items():
                if value == num:
                    text.append(key)
        # print(len(case))
        # print(len(text))
        for i in range(0, len(case)-1):
            if case[i] == 0:
                text[i] = text[i].lower()
            elif case[i] == 1:
                text[i] = text[i].upper()
        # print(text)
        text = "".join(text)
        return text


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object
        text (string): the message's text
        shift (integer): the shift associated with this message
        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.message_text = text
        self.valid_words = load_words('words.txt')
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        Returns: a COPY of self.encryption_dict
        '''
        encryption_dict_copy = self.encryption_dict
        return encryption_dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other attributes determined by shift.
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26
        Returns: nothing
        '''
        self.shift = shift

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
        text (string): the message's text
        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.message_text = text
        self.valid_words = load_words('words.txt')

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value and find the "best" one. We will define "best" as the shift that creates the maximum number of real words when we use apply_shift(shift) on the message text. If s is the original shift value used to encrypt the message, then we would expect 26 - s to be the best shift value for decrypting it.
        Note: if multiple shifts are equally good such that they all create the maximum number of valid words, you may choose any of those shifts (and their corresponding decrypted messages) to return
        Returns: a tuple of the best shift value used to decrypt the message and the decrypted message text using that shift value
        '''
        count = 0
        best_probability = []
        best_shift_value = []
        result = []
        for s in range(26):
            text = self.apply_shift(26-s)
            text = text.split()
            # print(text)
            for t in text:
                if is_word(load_words('words.txt'), t):
                    count += 1
                else:
                    count += 0
            best_probability.append(count)
            # if is_word(load_words('words.txt'),text):
            # if count > 0:
                # result.append(text)
                # best_shift_value.append(26-s)

            # if count > 0:
            result.append(text)
            best_shift_value.append(26-s)
            count = 0

        a = best_probability.index(max(best_probability))
        # print(a)
        return (best_shift_value[a], " ".join(result[a]))


if __name__ == '__main__':

   plaintext = PlaintextMessage('hello', 2)
   print('Expected Output: jgnnq')
   print('Actual Output:', plaintext.get_message_text_encrypted())
   plaintext = PlaintextMessage('My name is Tung', 8)
   print('Expected Output: Ug vium qa Bcvo')
   print('Actual Output:', plaintext.get_message_text_encrypted())
   plaintext = PlaintextMessage('Hello, World!', 4)
   print('Expected Output: Lipps, Asvph!')
   print('Actual Output:', plaintext.get_message_text_encrypted())

   ciphertext = CiphertextMessage('jgnnq')
   print('Expected Output:', (24, 'hello'))
   print('Actual Output:', ciphertext.decrypt_message())
   ciphertext = CiphertextMessage('Ug vium qa Bcvo')
   print('Expected Output:', (18, 'My name is Tung'))
   print('Actual Output:', ciphertext.decrypt_message())
   ciphertext = CiphertextMessage('Lipps, Asvph!')
   print('Expected Output:', (22, 'Hello, World!'))
   print('Actual Output:', ciphertext.decrypt_message())

   ciphertext = CiphertextMessage(get_story_string())
   print('Appropriate shift value and unencrypted story:')
   print(ciphertext.decrypt_message())
