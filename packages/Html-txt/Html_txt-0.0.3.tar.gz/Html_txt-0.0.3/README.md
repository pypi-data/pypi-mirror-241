# pyHtml
```bash

# html_txt Function
The html_txt function fetches HTML content from the specified URL, using optional headers and data for the request.
```bash
from your_module import html_txt

url = 'https://example.com'
headers = {
    'User-Agent': 'Your User Agent',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}
data = {'key': 'value'}  # Optional data for POST requests

parsed_html = html_txt(url, headers=headers, data=data) # data for POST requests 
parsed_html = html_txt(url, headers=headers) #  for Get requests 
print(parsed_html)
