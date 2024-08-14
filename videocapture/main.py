from time import sleep
import cv2

from zephyr import Stream


def get_cap(fpath):
    cap = cv2.VideoCapture(fpath)
    ret, frame = cap.read()
    if not ret:
        # Get first frame to check if file is valid
        print(f"ERROR: unable to open {fpath}")
        exit()
    return cap


if __name__ == "__main__":
    fpath = "2024-08-14_09-55-05.mkv"
    cap = get_cap(fpath)
    ret, frame = cap.read()
    # h, w  to create rtsp stream
    h, w = frame.shape[:2]

    fps = 20
    print("Creating stream...")
    stream = Stream(
        url="rtsp://localhost:8554/mystream", resolution=(w, h), fps=20, bitrate="2M"
    )
    print("Created stream.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Reached file end. Starting from the begining...")
            cap = get_cap(fpath)
            ret, frame = cap.read()
        sleep(1 / fps)
        stream.send(frame)
