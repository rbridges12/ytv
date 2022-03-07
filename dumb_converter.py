from PIL import Image 
from sys import argv

ascii_pixels = ".',/>aABH@#"

def dumb_convert(term_size, img_path):
    try:
        img = Image.open(img_path)
    except FileNotFoundError:
        print("error: image could not be found")
        return

    out_size = calculate_dims(term_size, img.size, preserve_scale=False) 
    img = img.resize(out_size)
    img = img.convert("L")
    img.show()
 
    pixels = img.getdata()
    

def calculate_dims(term_size, img_size, preserve_scale):
    if preserve_scale:
        pass
    
    else:
        return term_size  

dumb_convert((300, 200), argv[1])
