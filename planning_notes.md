# Image to Ascii Converter

### Dumb Converter
- find limiting dimension of output
- downscale image to limiting resolution of output
- have a list of ascii characters in order from least bright to most bright
- for each pixel in the downscaled image, map the brightness to an index in the character list

### Brute Force Converter
- calculate the pixel resolution of a box the size of a character layed over the image
- kernel "convolution" over the image: split up the image into tiles of the calculated character box size and iterate through them
- for every tile, try every possible character (in one color?) and run an image similarity algorithm to find the character that produces the most similar output to the original image
- image similarity algorithm could be some kind of weighted pixel brightness difference
- probably way way too slow for video streaming


### Evaluating Character Brightness
We could do this manually for ascii characters, but it might be a little unclear just looking at different characters by eye and ranking them. If we want to expand to unicode characters, this would become pretty infeasible to do by hand.

Instead, we can write a script to render each character as an image, then we can rank those images in order of average brightness (maybe just take the sum of all rgb values in each image).

# Color

### 

# Video to openCV Pipeline
### Option 1
- first run youtube-dl to download the desired video onto the local drive, then load that video file from openCV
- This is easy, but makes watching long videos inconvenient

### Option 2
- find a way to fetch the video frame by frame from youtube-dl and send those frames straight to openCV
- you could instantly stream any video of any length
- wouldn't require any hard drive space
- might require some kind of frame buffer setup and some more timing logic to avoid slowing down playback
- might have to concurrently run youtube-dl to download the next frame while running the ascii converter

# TODO
- separate conversion functions into their own file
- implement colored dumb conversion
- find optimal character brightness order
- incorporate bold text
- add option in executable script to play already downloaded video
- add option to save ascii video to a file and playback the file
- audio playback
- pause
- fast forward/slow down
- skip ahead/go back
- use youtube-dl python interface
- setup youtube-dl streaming

# Links
- [youtube-dl docs](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme)
- [tiktok-scraper](https://github.com/drawrowfly/tiktok-scraper)
- [youtube-dl streaming](https://stackoverflow.com/questions/50876292/capture-youtube-video-for-further-processing-without-downloading-the-video)
- [more streaming](https://stackoverflow.com/questions/43032163/how-to-read-youtube-live-stream-using-opencv-python)
