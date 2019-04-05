import requests

url = 'http://blackfoxs.org/radar/puzzle/'

headers = {
    'User-Agent': '7e7' # This is another valid field
}

response = requests.get(url, headers=headers)
print response.text