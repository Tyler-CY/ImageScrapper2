"""
For scrapping page source
"""
import urllib.request


def download_web_source(filename, url_address) -> None:
    """
    Download the source file of the webpage

    :param url_address: string of url
    :param filename: string of filename
    """
    # urllib.request.urlretrieve(url, str(url));

    # Copy from StackOverflow
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    request_ = urllib.request.Request(url_address, None, headers)  # The assembled request
    response = urllib.request.urlopen(request_)  # store the response
    # create a new file and write the image
    f = open(filename, 'wb')
    f.write(response.read())
    f.close()
