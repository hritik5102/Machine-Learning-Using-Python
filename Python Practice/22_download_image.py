import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://cdn-images-1.medium.com/max/1600/1*LEmBCYAttxS6uI6rEyPLMQ.png")