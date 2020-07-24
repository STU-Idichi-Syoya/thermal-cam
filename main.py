import threading
import time

import cv2
import numpy as np

import display

CAS_PATH="weights/haarcascade_frontalface_default.xml"
CAS_minNeighbors=10
WAIT_VIDEO_PATH = "weights/wait2_jp_eng.mp4"
SCREEN_BUF=100
WARN_TEMP=37.5
RESULT_SHOW_TIME=3
MAIN_SCREEN_FPS=30

WARN_IMG_PATH=""
OK_IMG_PATH = "OK.png"

WARN_IMG_MAT=cv2.imread(WARN_IMG_PATH)
OK_IMG_MAT=cv2.imread(OK_IMG_PATH)


DEBUG_CAM="http://192.168.0.14:4747/video"


import logging
logger=logging.getLogger("thrmal-cam-project")
logger.setLevel(20)
formatter = logging.Formatter('%(asctime)s:%(lineno)d:%(levelname)s:%(module)s:%(name)s:%(message)s')


sh=logging.StreamHandler()
sh.setFormatter(formatter)
logger.addHandler(sh)

class face_rec:
    def __init__(self,cas_path=CAS_PATH) -> None:
        self.face_rec=cv2.CascadeClassifier(cas_path)
        logger.info("cas_file load ok")
    def rec(self,F)->[()]:
        face=self.face_rec.detectMultiScale(F,minNeighbors=CAS_minNeighbors)

        return face


class Pi_CAM:
    def __init__(self) -> None:
        # self.v=cv2.VideoCapture(DEBUG_CAM)
        self.arr = np.random.rand(500, 500, 3) * 255
    def read(self)->np.ndarray:
        # _,F=self.v.read()
        # if not  _:logger.error("")
        return self.arr

class thrmal_cam(threading.Thread):
    # サーマルカメラ初期設定
    def __init__(self) -> None:
        super(thrmal_cam,self).__init__()

    #サーマル　測定開始
    def run(self):
        # self.result=に格納
        #todo
        self.result=None
        time.sleep(1)
    ## 8x8 行列
    def get_result(self)-> np.ndarray:
        return self.result


## 体温を8x8行列から検出
import random
def process(thraml_F)->float:
    r = random.random()
    if r>=0.5:return WARN_TEMP
    else: return 36.0



def main_state():
    logger.info("main_state_start")
    face_cls=face_rec()
    sc = display.screen()
    pi_cam=Pi_CAM()

    while True:
        sc.show_wait_video()
        thermal_c = thrmal_cam()


        F=pi_cam.read()
        while len(face_cls.rec(F)) == 0:
            # print("pi_cam read")
            F = pi_cam.read()
       

        #　サーマルカメラ温度検出開始
        th_mat=thermal_c.start()
        while thermal_c.is_alive():
            F=pi_cam.read()
            sc.show_any_IMG(F, sec=1)

        
        # サーマル　読み込み完了
        th_mat=thermal_c.get_result()
        temp=process(th_mat)

        # todo cam_F に描画処理
        if temp>=WARN_TEMP:
            sc.show_any_IMG(WARN_IMG_MAT)
        else:
            sc.show_any_IMG(OK_IMG_MAT)
        
        
        

if __name__ == '__main__':

    main_state()
    


