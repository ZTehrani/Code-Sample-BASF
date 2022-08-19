"""
Parse a web page, print anagrams
and palindromes in the page
"""
import argparse
# pylint: disable=import-error
from parse_page import parse_web_page
from anagram_in_page import find_anagrams
from palyndrom_in_page import find_palyndrom

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-l','--link', type=str, required=True,
        help='Link to web page')

    argument = parser.parse_args()

    text_in_page = parse_web_page(argument.link)
    anagrams = find_anagrams(text_in_page)
    palindromes = find_palyndrom(text_in_page)
    print('####################')
    print('List of anagrams: ', anagrams)
    print('####################')
    print('List of palindromes: ', palindromes)
