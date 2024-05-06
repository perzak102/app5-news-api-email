import requests
from send_email import send_email

api_key = "81acb547848a4d17b543dfa4144a7daa"
topic = "cars"
url = f"https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      f"&from=2024-04-29" \
      f"&sortBy=publishedAt&apiKey=" \
      f"{api_key}" \
      f"&language=en"

request = requests.get(url)
content = request.json( )
raw_message = ""
for item in content["articles"][:20]:
    if item["title"] is not None and item["description"] is not None:
        raw_message += "Title: " + item["title"] + "\n" + "Description: " + item["description"] + \
                       "\n" + item["url"] + "\n\n"

message: str = f"""\
Subject: New email from python news app about {topic}

{raw_message}
"""

send_email(message.encode("utf-8"))