import os

#------[model]---------
try:
     import requests
except:
     os.system('pip install requests')

try:
    import urllib3
except:
     os.system('pip install urllib3')

try:
    from bs4 import BeautifulSoup as bs
except:
     os.system('pip install bs4')
try:
    import mahdix,random
except:
     os.system('pip install mahdix')

html_Session=requests.Session()
def send_req(link):
    http = urllib3.PoolManager()
    response = http.request('GET', link)
    data=response.data.decode('utf-8')
    return str(data)
def W_ueragnt():
        chrome_version = random.randint(80, 99)
        webkit_version = random.randint(500, 599)
        safari_version = random.randint(400, 499)
        windows_version = random.randint(8, 10)
        is_win64 = random.choice([True, False])
        user_agent = f"Mozilla/5.0 (Windows NT {windows_version}.{is_win64 and 'WOW64;' or ''}Win64; x64) AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0"
        return user_agent
def html_txt(Url,Cookie=None,Headers=None, Data=None):
    """
    Make an HTTP request to the specified URL with optional headers and data.

    Parameters:
    - url (str): The URL to send the HTTP request.
    - headers (dict, optional): Custom headers for the request.
    - data (dict, optional): Data to be sent in the request (for POST requests).

    Returns:
    - BeautifulSoup: Parsed HTML content using BeautifulSoup.
    """
    if Headers is None:
        Headers = {
            'User-Agent': W_ueragnt(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }
    if Cookie is None:
        Cookie={}
    if Data is None:
        response = requests.get(Url, headers=Headers,cookies=Cookie)
    else:
        response = requests.post(Url, headers=Headers, data=Data,cookies=Cookie)
    soup = bs(response.text, 'html.parser')
    return soup
