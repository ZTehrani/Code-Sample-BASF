"""
parsing web page
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

def parse_web_page(link):
    """
    parse the link
    extract text
    return list of words which are serparetd by space
    """
    # open web page
    # pylint: disable=consider-using-with
    web_page = urlopen(link)
    # decode
    page_bytes = web_page.read()
    page_decode = page_bytes.decode("utf-8")
    # create object
    soup_object = BeautifulSoup(page_decode, "html.parser")
    # extract text
    text = soup_object.get_text()
    # replace some characters
    text_edited = text.replace('\n'," ")
    text_edited = text_edited.replace(','," ")
    text_edited = text_edited.replace(':'," ")
    text_edited = text_edited.replace('.'," ")
    text_edited = text_edited.replace('!'," ")
    text_edited = text_edited.replace('?'," ")
    text_edited = text_edited.replace('"',"")
    text_words_list = text_edited.split()
    return text_words_list
