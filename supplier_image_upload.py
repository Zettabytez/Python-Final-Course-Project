#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
for f in os.listdir("./supplier-data/images"):
    if ".jpeg" in f:
        with open('./supplier-data/images/' + f, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
