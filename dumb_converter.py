import cv2
import numpy as np
from sys import argv
from shutil import get_terminal_size
from time import time, sleep


# render image in grayscale ascii based only on character brightness
def dumb_convert(term_size, frame, ascii_brightness_map, preserve_scale=False):
    
    # convert image to grayscale and scale it to the terminal size  
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out_dims = calculate_dims(term_size, frame.shape, preserve_scale)
    frame = cv2.resize(frame, out_dims)
    
    # map grayscale brightness to ascii characters
    ascii_range = len(ascii_brightness_map) - 1
    char_ids = np.rint((frame / 256) * ascii_range).astype(int)
    char_array = np.array(list(ascii_brightness_map))
    chars = char_array[char_ids]
    
    # combine 2D char array into a single string with newlines after each row
    return "".join("".join(row) + "\n" for row in chars)

# TODO: incorporate font aspect ratio to make scale preservation more accurate
# TODO: center scale preserved image in terminal
def calculate_dims(term_size, img_size, preserve_scale):
    if preserve_scale:
        w_in, h_in = img_size
        w_out, h_out = term_size
        w_scale = w_out / w_in
        h_scale = h_out / h_in
        limiting_scale = min(w_scale, h_scale)
        return (round(limiting_scale * w_in), round(limiting_scale * h_in))
    
    return term_size  


def main():
    video = cv2.VideoCapture(argv[1])
    framerate = video.get(cv2.CAP_PROP_FPS)
    frame_delay = 1 / framerate

    term_size = tuple(get_terminal_size())
    char_pixels = " .',/>aABH@#"
    char_pixels_all = " `.\'_-,:\"^;~+*><!/|)i?rcl]}jLJCY%1tvzxnufoahqpdbwkmZIX&8UO$@Q0W#MB"
    char_pixels10 = " .:-=+*#%@"

    while True:
        success, frame = video.read()
        if not success:
            break

        # see how long it takes to render the frame, then sleep for the remainder of the frame delay
        start_time = time()
        print(dumb_convert(term_size, frame, char_pixels, preserve_scale=False))
        render_time = time() - start_time
        sleep(max(0, frame_delay - render_time))


if __name__ == "__main__":
    main()

