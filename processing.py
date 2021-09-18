from PIL import Image, ImageColor, UnidentifiedImageError
import numpy as np
import re

def count_pixels(data, hex_code=None):
    if data:
        try:
            img = Image.open(data)
        except UnidentifiedImageError:
            return {'error_message':'Файл не является фотографией'}
        array = np.array(img)
        black = np.sum(array==[0, 0, 0])
        white = np.sum(array==[255,255,255])
        if hex_code:
            if check_hex_color(hex_code):
                r,g,b = check_hex_color(hex_code)
                return {'black' : black, 'white' : white, 'res':np.sum(array==[r,g,b]), 'hex_code' : hex_code}
            return {'black' : black, 'white' : white, 'error_message':'Некорректный HEX код'}
        return {'black' : black, 'white' : white}
    return {'error_message':'Файл не может быть пустым'}

def check_hex_color(hex_code):
    hex_code = "#" + hex_code.lstrip()
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_code)
    if match:
        return ImageColor.getcolor(hex_code, "RGB")
