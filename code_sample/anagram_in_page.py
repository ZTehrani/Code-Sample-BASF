"""
find anagrams
"""
# pylint: disable=import-error
from process_string import Anagram

cl_anagram = Anagram()

def find_anagrams(words):
    """
    find anagrams in a list of words
    """
    anagrams_in_page = []
    for _, word in enumerate(words):
        # create anagrams of each string
        anagrams_list = cl_anagram.create_anagrams(word)
        # check what items from anagrams of the string are in the
        #   input list
        similar = set(anagrams_list).intersection(set(words))
        similar_list = list(similar)
        # if the similar items are not already added, add them
        #   if there is a word with repeated letters, it would appear as
        #   anagram because each repeat has it's own identity
        if similar_list not in anagrams_in_page and len(similar_list) != 0:
            anagrams_in_page.append(similar_list)
    return anagrams_in_page
