import requests

api_key = "81acb547848a4d17b543dfa4144a7daa"
url = f"https://newsapi.org/v2/everything?q=poland&" \
      f"from=2024-03-30&sortBy=publishedAt&apiKey=" \
      f"{api_key}"

request = requests.get(url)
content = request.json( )
for item in content["articles"]:
      print(item["title"])
      print(item["description"])