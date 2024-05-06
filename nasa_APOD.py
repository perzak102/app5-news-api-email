import requests
import streamlit as st

api_key = "b7BHZ97Tvckd5zuMJee6kyZPalrUepxBW1ytSje3"

url = f"https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

request = requests.get(url)
content = request.json()

title = content["title"]
explanation = content["explanation"]
image_url = content["url"]
media_type = content["media_type"]
image_raw = requests.get(image_url).content

with open("image.jpg", "wb") as file:
      file.write(image_raw)

st.title(title)
match media_type:
    case "video":
        st.video(image_url)
    case "image":
        st.image("image.jpg")
st.write(explanation)
