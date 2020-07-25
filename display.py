import multiprocessing as mlp
import queue
import threading

import numpy as np

from main import logger, WAIT_VIDEO_PATH, RESULT_SHOW_TIME


def show_f(v_path, q: mlp.Queue, FPS=30):
    import cv2, time
    v = cv2.VideoCapture(v_path)

    cv2.namedWindow('w', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('w', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    fps = FPS
    fps_1 = int((1 / fps) * 10 ** 3)
    logger.info("display is initialized")
    print("id->", id(show_f))

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
    THREAD_MODE = "THREAD-MODE"
    MULTI_PROCESS_MODE = "MULTI_PROCESS-MODE"

    def __init__(self, wait_video_path=WAIT_VIDEO_PATH, THRED_MODE="THREAD-MODE") -> None:
        if THRED_MODE == "THREAD-MODE":
            self._SCQueue = queue.Queue(maxsize=30)
            self.sc = threading.Thread(target=show_f, args=(wait_video_path, self._SCQueue))

        else:
            self._SCQueue = mlp.Queue(maxsize=30)
            self.sc = mlp.Process(target=show_f, args=(wait_video_path, self._SCQueue))

        self.sc.start()

    def show_any_IMG(self, F: np.ndarray, sec=RESULT_SHOW_TIME):

        self._SCQueue.put([F, sec])

    def show_wait_video(self):
        pass
