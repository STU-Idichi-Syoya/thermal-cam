import multiprocessing as mlp
from multiprocessing import Queue

import cv2
import numpy as np

#
# v1=cv2.VideoCapture("weights\SOUL'd OUT　『COZMIC TRAVEL』-ZZIur_FcAOw.mkv")
# #

# cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
# cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# #
#
#
#
# _,f=v1.read()
# while _:
#     cv2.imshow("screen",f)
#     cv2.waitKey(1)
#     _,f=v1.read()

wait_video_path = "weights\short.mp4"
MAIN_SCREEN_FPS = 30
cv2.setNumThreads(0)
v = cv2.VideoCapture(wait_video_path)


def show_f(v_path, q: Queue):
    import cv2, time
    v = cv2.VideoCapture(v_path)

    # cv2.namedWindow('w', cv2.WINDOW_NORMAL)
    # cv2.setWindowProperty('w', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    fps = 35
    fps_1 = int((1 / fps) * 10 ** 3)

    def show(f):

        cv2.imshow("w", f)
        s = time.time()
        cv2.waitKey(fps_1)
        print(f"\rfps={1 / (time.time() - s)}", end="")

    while True:
        if q.empty():
            _, f = v.read()
            if not _:
                v.set(cv2.CAP_PROP_POS_MSEC, 0)
                _, f = v.read()
            show(f)
        else:
            f, t = q.get()
            # print(type(f),type(t))
            for i in range(fps * t):
                show(f)


class screen:
    def __init__(self) -> None:
        self._SCQueue = Queue(maxsize=30)

        self.sc = mlp.Process(target=show_f, args=(wait_video_path, self._SCQueue))
        self.sc.start()

    def show_any_IMG(self, F: np.ndarray, sec=1):
        self._SCQueue.put([F, sec])

    def show_wait_video(self):
        pass


if __name__ == '__main__':

    import time, cv2

    sc = screen()
    v2 = cv2.VideoCapture("vlc-record-2018-07-12-17h19m03s-Converting rtsp___192.168.0.4_11-.mp4")
    while True:
        time.sleep(5)
        _, f = v2.read()
        if not _:
            v2.set(cv2.CAP_PROP_POS_MSEC, 0)
            _, f = v2.read()
        sc.show_any_IMG(f)
    # sc.say_state()
