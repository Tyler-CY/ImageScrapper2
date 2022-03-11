"""
Extract texts to a list from a textfile
"""
import re


def extract_regex(filename: str) -> list:
    """
    Extract texts to a list from a textfile
    :param filename: string of filename
    :return: a list of matching strings
    """
    # result is the list of image URLs/links
    result = []

    # Open the source file
    f = open(filename, 'r')

    # Search for matching regex
    for line in f:
        # Might have error since website uses JPG or jpg or etc.
        wanted = re.findall(r'Photo/[0-9-/]+\.[A-Za-z]{3}', line)

        result += wanted

    # Print result
    print(result)

    f.close()

    return result
