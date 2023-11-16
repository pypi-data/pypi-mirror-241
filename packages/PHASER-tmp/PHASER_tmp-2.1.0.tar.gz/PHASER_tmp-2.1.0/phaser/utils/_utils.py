import os
from PIL import Image
import numpy as np

class ImageLoader():
    def __init__(self, path:str):
        # do not use path.name since it depends on the path being WindowsPath etc.
        # instead, convert the path to a string value
        self.path = str(path)
        self.filename = os.path.basename(self.path)
        
        # load the image from the provided path
        self.image = Image.open(path)
        
        # get image dimensions
        self.width = self.image.size[0]
        self.height = self.image.size[1]

def bool2binstring(hash):
    # Ensure the array is numpy of ints
    hash = np.array(hash, dtype=int)
    return "".join(str(b) for b in hash)