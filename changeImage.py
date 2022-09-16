#!/usr/bin/env python3

"""from PIL import Image
from os import listdir
import re

src = "supplier-data/images/"

img_files = [ f for f in listdir(src) if ".tiff" in f ]

for file in img_files:
    src_img = Image.open(src + file)
    new_img = src_img.resize((600,400)).convert("RGB")
    new_file = re.sub(".tiff", ".jpeg", file)
    new_img.save(src + new_file, "JPEG")
"""

from PIL import Image
import os

path = "./supplier-data/images/"
for f in os.listdir("./supplier-data/images"):
    if f.endswith(".tiff"):
        split_f = f.split(".")
        name = split_f[0] + ".jpeg"
        im = Image.open(path + f).convert("RGB")
        im.resize((600, 400)).save("./supplier-data/images/" + name, "JPEG")
