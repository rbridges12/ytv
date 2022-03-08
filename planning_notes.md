# Image to Ascii Converter

## Dumb Converter
- find limiting dimension of output
- downscale image to limiting resolution of output
- have a list of ascii characters in order from least bright to most bright
- for each pixel in the downscaled image, map the brightness to an index in the character list, and either assign the color to the color of the pixel or to a brighter/purer version of the pixel (?)

## Brute Force Converter
- calculate the pixel resolution of a box the size of a character layed over the image
- kernel "convolution" over the image: split up the image into tiles of the calculated character box size and iterate through them
- for every tile, try every possible character (in one color?) and run an image similarity algorithm to find the character that produces the most similar output to the original image
- image similarity algorithm could be some kind of weighted pixel brightness difference
- probably way way too slow for video streaming


## Evaluating Character Brightness
We could do this manually for ascii characters, but it might be a little unclear just looking at different characters by eye and ranking them. If we want to expand to unicode characters, this would become pretty infeasible to do by hand.

Instead, we can write a script to render each character as an image, then we can rank those images in order of average brightness (maybe just take the sum of all rgb values in each image).


# Downloading Videos
  - `youtube-dl` to download videos
  - openCV to split videos into frame images

# Video to Ascii Pipeline
### Option 1
- run a separate python program that uses openCV to split the video into frames and save each individual frame with the frame number in the file name
- have the ascii converter sort through all the file names in order of their frame number and convert them to ascii art one by one

### Option 2
- use openCV to save one frame at a time, then convert it to ascii, then delete it

### Option 3
- figure out how to get a raw pixel array straight from openCV and do the ascii conversion straight from the openCV frame without having to save anything

# TODO
- separate conversion functions into their own file
- implement colored dumb conversion
- find optimal character brightness order
- look into video streaming instead of just downloading
- incorporate bold text
- add option in executable script to play already downloaded video
- add option to save ascii video to a file and playback the file

# Links
- [youtube-dl docs](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme)
- [tiktok-scraper](https://github.com/drawrowfly/tiktok-scraper)
