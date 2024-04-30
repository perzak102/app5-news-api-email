import requests

api_key= "81acb547848a4d17b543dfa4144a7daa"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-03-30&sortBy=publishedAt&apiKey=81acb547848a4d17b543dfa4144a7daa"

request = requests.get(url)

content = request.text
print(content)