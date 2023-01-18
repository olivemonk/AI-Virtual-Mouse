import cv2
from threading import Thread

class ThreadedCamera(object):
    def __init__(self, source = 0):

        self.capture = cv2.VideoCapture(source)

        self.thread = Thread(target = self.update, args = ())
        self.thread.daemon = True
        self.thread.start()

        self.status = False
        self.frame  = None

    def update(self):
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()

    def grab_frame(self):
        if self.status:
            return self.frame
        return None
if __name__ == '__main__':
    stream_link = "https://videos3.earthcam.com/fecnetwork/9974.flv/chunklist_w1421640637.m3u8"
    streamer = ThreadedCamera(stream_link)

    while True:
        frame = streamer.grab_frame()
        if frame is not None:
            cv2.imshow("Context", frame)
        cv2.waitKey(1) 