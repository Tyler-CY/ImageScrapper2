"""
The main program.
"""

import urllib.request
from Page_Source_Downloader import download_web_source
from Regex_Extractor import extract_regex
from Image_Downloader import download_image
import pathlib
import re
import urllib.error

# TODO
HIDDEN = ''


def url_full_download(url: str, i: int) -> None:
    """
    Main

    :url: string of URL to be downloaded
    """
    # filename for source
    filename = str(i) + '_source.txt'

    # Make directory if sources is not available
    pathlib.Path('Sources').mkdir(parents=True, exist_ok=True)
    filename = 'Sources/' + filename  # reformat

    # Download the source file
    download_web_source(filename, url)
    # Extract the jpg files URL/Links
    result = extract_regex(filename)

    # Add photos
    parent_dir = ''  # we want this variable to exist after for loop to create title file
    i = 1
    for jpg in result:
        # Check if directory exists, if not, create parent directories
        parent_dir = jpg[:11]
        pathlib.Path(parent_dir).mkdir(parents=True, exist_ok=True)

        # Image URL and name of the image
        image_url = HIDDEN
        image_name = jpg

        print("Downloading {} out of {} ({}%)".format(i, len(result), (100 * i) // len(result)))
        print("Image URL: " + image_url)
        print("Image Name: " + image_name)

        # Download the image from image_url and rename it to image_name
        try:
            download_image(image_name, image_url)
        except urllib.error.HTTPError:
            print("HTTP Error")

        i += 1

    # Add file description for images
    title = []
    f = open(filename, 'r')
    # Search for matching regex
    for line in f:
        # Regex: <h1 class="pageHeading_noStyle"> TITLE HERE WITHOUT SPACE IN FRONT AND BEHIND </h1>
        wanted = re.findall(r'<h1 class="pageHeading_noStyle">.+</h1>', line)
        title += wanted

    if len(result) != 0:  # only make a title if there are photos
        # Getting the Title from the Source Code
        title = str(title[0])
        title = title.strip('<h1 class="pageHeading_noStyle">')
        title = title.strip('</h1>')

        print("Title of event: " + title)
        print("Title File: " + parent_dir + 'Title')

        g = open(parent_dir + 'Title', "w+")
        g.write(title)
        g.close()

    f.close()
