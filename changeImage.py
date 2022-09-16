#!/usr/bin/env python3

from PIL import Image
from os import listdir
import re

src = "supplier-data/images/"

img_files = [ f for f in listdir(src) if ".tiff" in f ]

for file in img_files:
    src_img = Image.open(src + file)
    new_img = src_img.resize((600,400)).convert("RGB").save(src + re.sub(".tiff", ".jpeg", file), "JPEG")
