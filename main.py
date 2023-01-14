import pyautogui as pg
from ahk import AHK
ahk = AHK()
import time

col1 = pg.screenshot('target1.png', region=(1019, 60, 1, 1))
pixel = (236, 187, 6)

col2 = pg.screenshot('target2.png', region=(1101, 60, 1, 1))
pixel2 = (60, 63, 65)

screenFirst = pg.screenshot('target3.png', region=(1019, 60, 1, 1))
screenFirst2 = pg.screenshot('target4.png', region=(1101, 60, 1, 1))

while True:

    if col1 == screenFirst  \
            or col2 == screenFirst2:
        print("1 условие")
        time.sleep(0.5)
        ahk.mouse_move(200, 500, speed=15)
        time.sleep(1)

    if 1 in (col1 == screenFirst, col2 == screenFirst2):
        print('2 условие и вождение мышки после с 1-го')
        time.sleep(0.5)
        ahk.mouse_move(800, 300, speed=15)


    else:
        print("вывод")






