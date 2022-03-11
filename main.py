"""
The main file for scrapping images from an URL.
"""
import urllib.request
from Page_Source_Downloader import download_web_source
from Regex_Extractor import extract_regex
from Image_Downloader import download_image
from URL_Downloader import url_full_download
import pathlib
import re

# TODO
url = ''


def main() -> None:
    """
    Main
    """
    using = 1
    while using > 0:
        print("Enter first number (inclusive): ")
        x = input()
        print("x is: " + x)
        print("Enter second number (inclusive): ")
        y = input()
        print("y is: " + y)

        print("X is " + x + " and Y is " + y + ". Confirm? (Y/N) or abort (X)")
        z = input()
        if z == 'Y' or z == 'y':
            for i in range(int(x), int(y) + 1):
                print("URL:" + url)
                url_full_download(url, i)
        elif z == 'X' or z == 'x':
            print("Thank you.")
            return
        else:
            print("Try Again.")


if __name__ == "__main__":
    main()
