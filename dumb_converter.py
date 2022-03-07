import cv2
import numpy as np
from sys import argv
from shutil import get_terminal_size
from time import sleep


# render image in grayscale ascii based only on character brightness
def dumb_convert(term_size, frame, char_pixels):
    
    # convert image to grayscale and scale it to the terminal size
    # TODO: add option to downsize while maintaining scale  
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, term_size)
    
    # map grayscale brightness to ascii characters
    ascii_range = len(char_pixels) - 1
    char_ids = np.rint((frame / 256) * ascii_range).astype(int)
    char_array = np.array(list(char_pixels))
    chars = char_array[char_ids]
    
    # combine 2D char array into a single string with newlines after each row
    return "".join("".join(row) + "\n" for row in chars)

def calculate_dims(term_size, img_size, preserve_scale):
    if preserve_scale:
        pass
    
    else:
        return term_size  


def main():
    video = cv2.VideoCapture(argv[1])
    term_size = tuple(get_terminal_size())
    char_pixels = ".',/>aABH@#"
    ascii_frames = []

    while True:
        success, frame = video.read()
        if not success:
            break

        ascii_frames.append(dumb_convert(term_size, frame, char_pixels))

    for frame in ascii_frames:
        print(frame)
        sleep(0.05)

if __name__ == "__main__":
    main()

