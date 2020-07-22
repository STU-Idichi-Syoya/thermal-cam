import cv2,numpy as np

CAS_PATH="weights/haarcascade_frontalface_default.xml"
CAS_minNeighbors=10
wait_video_path="weights\SOUL'd OUT　『COZMIC TRAVEL』-ZZIur_FcAOw.mkv"
SCREEN_BUF=100
WARN_TEMP=37.5
RESULT_SHOW_TIME=3
MAIN_SCREEN_FPS=30

WARN_IMG_PATH=""
OK_IMG_PATH=""

WARN_IMG_MAT=cv2.imread(WARN_IMG_PATH)
OK_IMG_MAT=cv2.imread(OK_IMG_PATH)

class face_rec:
    def __init__(self) -> None:
        self.face_rec=cv2.CascadeClassifier(casfile)

    def rec(self,F)->[()]:
        face=self.face_rec.detectMultiScale(F,minNeighbors=CAS_minNeighbors)

        return face
import threading

class Pi_CAM:
    def __init__(self) -> None:
        pass
    def read(self)->np.ndarray:
        # return 

class thrmal_cam(threading.Thread):
    # サーマルカメラ初期設定
    def __init__(self) -> None:
        super(threading.Thread).__init__()

    #サーマル　測定開始
    def run(self):
        # self.result=に格納
        pass
    ## 8x8 行列
    def get_result(self)-> np.ndarray:
        return self.result


class show_server(threading.Thread):
    def __init__(self,Queue=None,wait_video_path=wait_video_path,FPS=MAIN_SCREEN_FPS) -> None:
        super(threading.Thread).__init__()
        self.wait_v=cv2.VideoCapture(wait_video_path)
        self.queue=Queue

        self.FPS=FPS
        self.FPS_1_int=int((1/FPS)*10**3)
        self.cv2_screen_name="screen"

        cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)



    def run(self):
        while True:
            if self.queue.empty():
                _,F=self.wait_v.read()
                if not _ :
                    self.wait_v.set(cv2.CAP_PROP_POS_FRAMES, 0)
                cv2.imshow(self.cv2_screen_name,F)
                ## FPSの秒換算 wait
                cv2.waitKey(self.FPS_1_int)
            else:
                F,t=self.queue.get()
                if t==0:
                    cv2.imshow(self.cv2_screen_name,F)
                    ## FPSの秒換算 wait
                    cv2.waitKey(self.FPS_1_int)

                for _ in range(int(t)):

                    cv2.imshow(self.cv2_screen_name,F)
                    ## FPSの秒換算 wait
                    cv2.waitKey(self.FPS_1_int)

class screen:
    def __init__(self) -> None:
        self._SCQueue=queue.Queue(maxsize=SCREEN_BUF)
        self._screen=show_server(self._SCQueue,)
        self._screen.start()
    def show_any_IMG(F:np.ndarray,sec=RESULT_SHOW_TIME):

        self._SCQueue.put([F,sec])

    def show_wait_video():
        pass

## 体温を8x8行列から検出
import random
def process(thraml_F)->float:
    
    r=random.random(0,1)
    if r>=0.5:return WARN_TEMP
    else: return 36.0


import queue   
def main_state():
    print("main_state_start")
    face_cls=face_rec()
    thermal_c=thrmal_cam()
    sc=screen()
    pi_cam=Pi_CAM()
    while True:
        sc.show_wait_video()

        F=pi_cam.read()
        while len(face_cls.rec(F))==0: 
              F=pi_cam.read()
       

        #　サーマルカメラ温度検出開始
        th_mat=thermal_c.start()
        while thermal_c.is_alive():
            F=pi_cam.read()
            sc.show_any_IMG(F,sec=0)

        
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
    


