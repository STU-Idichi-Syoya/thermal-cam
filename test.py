import cv2

v1=cv2.VideoCapture("weights\SOUL'd OUT　『COZMIC TRAVEL』-ZZIur_FcAOw.mkv")


cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

_,f=v1.read()
while _:
    cv2.imshow("screen",f)
    cv2.waitKey(1)
    _,f=v1.read()





