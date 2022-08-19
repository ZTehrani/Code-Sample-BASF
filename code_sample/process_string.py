"""
Class for storing and processing strings
"""
from itertools import permutations

class StringManipulation:
    """
    Class for storing and processing strings
    """

    def append_string(self, existing_string, new_string):
        """
        appending a new string to the existing string
        """
        all_strings = [existing_string, new_string]
        existing_string = "".join(all_strings)
        return existing_string

    def remove_substring(self, phrase, sub):
        """
        removing a substring
        """
        new_phrase = phrase.replace(sub,"")
        return new_phrase

    def mirror_string(self, phrase):
        """
        mirroring a string
        """
        mirror = {'A':'Z',
                 'B':'Y',
                 'C':'X',
                 'D':'W',
                 'E':'V',
                 'F':'U',
                 'G':'T',
                 'H':'S',
                 'I':'R',
                 'J':'Q',
                 'K':'P',
                 'L':'O',
                 'M':'N',
                 'N':'M',
                 'O':'L',
                 'P':'K',
                 'Q':'J',
                 'R':'I',
                 'S':'H',
                 'T':'G',
                 'U':'F',
                 'V':'E',
                 'W':'D',
                 'X':'C',
                 'Y':'B',
                 'Z':'A',
                 ' ':' '}

        mirrored_phrase = ''
        for char in phrase:
            if char.isupper():
                mirrored_phrase = self.append_string(mirrored_phrase, mirror[char])
            else:
                char = char.upper()
                new_char = mirror[char]
                mirrored_phrase = self.append_string(mirrored_phrase, new_char.lower())
        return mirrored_phrase

    def read_file(self, file_name):
        """
        read a file
        return a list, each item represents each line of file
        """
        end_line = '\n'
        #pylint: disable=unspecified-encoding
        with open(file_name, 'r') as file:
            lines = file.readlines()
        # pylint: disable=consider-using-enumerate
        for i in range(len(lines)):
            if end_line in lines[i]:
                lines[i] = lines[i].replace('\n','')
        return lines

    def write_file(self, file_name, line):
        """
        write content to file
        """
        lines_list = self.read_file(file_name)
        # pylint: disable=unspecified-encoding
        with open(file_name, 'a') as file:
            if len(lines_list) != 0:
                file.write('\n')
            file.write(line)

class Anagram(StringManipulation):
    """
    Child class of StringManipulation
    """
    def create_anagrams(self, phrase):
        """
        anagrams of a string
        """
        # pylint: disable=unnecessary-comprehension
        phrase_chrs = [ch for ch in phrase]
        anagrams = permutations(phrase_chrs, len(phrase_chrs))
        anagrams_words = []
        for permu in list(anagrams):
            new_word = "".join(permu)
            anagrams_words.append(new_word)
        # remove the original string from which
        #   anagrams were made. So in final list
        #   there are only anagrams of the string not
        #   the string itself as well
        anagrams_words.remove(phrase)
        return anagrams_words

class Palyndrom(StringManipulation):
    """
    Child class of StringManipulation
    """
    # pylint: disable=inconsistent-return-statements
    def save_palyndrome(self, phrase):
        """
        returning palindromes
        """
        if len(phrase) > 1:
            phrase_list = list(str(phrase))
            phrase_list_rev = phrase_list[::-1]
            if phrase_list_rev == phrase_list:
                return phrase

if __name__ == '__main__':

    cl = StringManipulation()
    # appending a new string
    CURRENT_STR = 'This is '
    NEW_STR = 'new string'
    NEW_PHRASE = cl.append_string(CURRENT_STR, NEW_STR)
    print("Existing string is: ", CURRENT_STR)
    print("New string is: ", NEW_STR)
    print("Appended string is: ", NEW_PHRASE)
    print('############################')
    # removing a substring
    SUB_STR = 'new'
    NEW_PHRASE = cl.remove_substring(NEW_PHRASE, SUB_STR)
    print('Substring is: ', SUB_STR)
    print('Edited string is: ', NEW_PHRASE)
    print('############################')
    # mirroring a string
    STRING_TO_MIRROR = 'How you doing'
    MIRRORED_STRING= cl.mirror_string(STRING_TO_MIRROR )
    print('String to mirror is: ', STRING_TO_MIRROR )
    print('Mirrored string is: ', MIRRORED_STRING)
    print('############################')
    # read file
    LINES = cl.read_file('text_file.txt')
    print('Lines from text_file.txt are: ', LINES)
    print('############################')
    # write to file
    NEW_LINE = 'This is new line, written by the code'
    cl.write_file('text_file_to_write.txt', NEW_LINE)
    print("Line:", '"', NEW_LINE, '"', " was written to text_file_to_write.txt")
    print('############################')
    # creating anagrams
    cl_anagram= Anagram()
    WORD = 'You'
    word_anagrams = cl_anagram.create_anagrams(WORD)
    print('String to create anagrams for is: ', WORD)
    print('Anagrams of the string are: ', word_anagrams)
    print('############################')
    # saving palindromes
    cl_polyndrom = Palyndrom()
    words_list = ['level', 'civic','hi','dad','apple','refer','orange','green']
    palindromes_list = [cl_polyndrom.save_palyndrome(word) for _, word in enumerate(words_list)]
    print('The list from which palindromes would be saved is: ', words_list)
    print('Palindromes present in the list are: ')
    for _, palyndrom in enumerate(palindromes_list):
        if palyndrom is not None:
            print(palyndrom)
