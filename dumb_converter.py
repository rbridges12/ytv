from PIL import Image 
from sys import argv
from shutil import get_terminal_size
from os import listdir
from time import sleep

char_pixels = ".',/>aABH@#"
#char_pixels = ".,'\":-=+*#%@"

def dumb_convert(term_size, img_path):
    try:
        img = Image.open(img_path)
    except FileNotFoundError:
        print("error: image could not be found")
        return

    out_size = calculate_dims(term_size, img.size, preserve_scale=False) 
    img = img.resize(out_size)
    img = img.convert("L")
#    img.show()
 
    pixels = img.getdata()
    chars = []
    for p in pixels:
        index = round((p / 256) * (len(char_pixels) - 1))
        #print(index)
        chars.append(char_pixels[index])
    
    return print_char_img(chars, term_size) 

def calculate_dims(term_size, img_size, preserve_scale):
    if preserve_scale:
        pass
    
    else:
        return term_size  

def print_char_img(chars, term_size):
    output = []
    width, height = term_size
    for i, c in enumerate(chars):
       output.append(c)
       if i % width == 0:
          output.append("\n") 
    #print("".join(output))
    return "".join(output)

#dumb_convert(tuple(get_terminal_size()), argv[1])
#img_filenames = [(int(f.replace(".jpg", "")), f) for f in listdir("frames")]
ascii_frames = []
term_size = tuple(get_terminal_size())
for filename in sorted(listdir("frames"), key=lambda x: int(x.replace(".jpg", ""))):
    #print(filename)
    frame = dumb_convert(term_size, f"frames/{filename}")
    ascii_frames.append(frame)

for frame in ascii_frames:
    print(frame)
    sleep(0.05)
