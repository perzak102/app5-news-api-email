import requests
from send_email import send_email

api_key = "81acb547848a4d17b543dfa4144a7daa"
url = f"https://newsapi.org/v2/everything?q=poland&" \
      f"from=2024-03-30&sortBy=publishedAt&apiKey=" \
      f"{api_key}"

request = requests.get(url)
content = request.json( )
raw_message = ""
for item in content["articles"]:
      raw_message += "Title: " + item["title"] + "\n" + "Description: " + item["description"] + "\n\n\n"

message: str = f"""\
Subject: New email from python news app

{raw_message}
"""

send_email(message.encode("utf-8"))