
#!/usr/bin/env python3
"""Retrieve and print words from an URL.(DOCSTRINGS)
   
Usage:

    from Hello_Python import main
    main(URL)
"""
import sys
from urllib.request import urlopen

def fetch_words(url):
    """ fetch a list of words from a URL. 
    args:
        url of a UTF-8 text document.

    Returns:
        A listy of strings containing the word
    """
    with urlopen("http://sixty-north.com/c/t.txt") as story:
        story_words=[]
        for line in story:
            line_words=line.decode("utf-8").split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line.

    Args:
        An iterable series of items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL.

    Args:
        URL: The URL of UTF_8 text document.
    """
    url=sys.argv[1]#The 0th arg is the module filename
    story_words = fetch_words(url)
    print_items(story_words)


if __name__=="__main__":
    main(sys.argv[1])