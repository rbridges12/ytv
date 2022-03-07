import cv2
from sys import argv

print(argv[1])
video = cv2.VideoCapture(argv[1])
frame_num = 0

while True:
    success, frame = video.read()
    print(success)
    #print(list(frame))
    break
    if success:
        cv2.imwrite(f"{argv[2]}/frames/{frame_num}.jpg", frame)
    else:
        break
    frame_num += 1

video.release()

