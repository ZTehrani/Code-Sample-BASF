"""
find palindromes
"""
def find_palyndrom(words):
    """
    find palindromes from the list of words
    """
    palindromes_in_page = []
    for _, word in enumerate(words):
        if len(word) > 1:
            word_list = list(str(word))
            word_list_rev = word_list[::-1]
            if word_list_rev == word_list:
                if word not in palindromes_in_page:
                    palindromes_in_page.append(word)
    return palindromes_in_page
