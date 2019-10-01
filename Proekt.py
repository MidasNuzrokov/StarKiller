from graph import *
from random import *

#---------------------------------
windowSize(1200, 700)
canvasSize(1200, 700)


# ФОН
brushColor(0, 0, 0)
polygon([(0, 0), (0, 700), (1200, 700), (1200, 0)])


# БАЗА СТАРКИЛЛЕР
penSize(5)
penColor('SkyBlue')
brushColor('LightSlateGray')
telo = circle(100, 350, 80)
penSize(30)
penColor(100,100,100)
strip1 = line(25,350,180,350)
penColor(0,0,0)
penSize(10)
strip2 = line(22,350,180,350)
penColor(0,0,0)
penSize(5)
brushColor(200,0,0)
gun = circle(170,350,20)
penSize(1)

# ПОЯВЛЕИЕ ЗВЁЗД
starAmount = 20
count = 0
starMas = [line(0,0,0,0)]*starAmount

def starLaunch():
    if count2 == 100:
        close()
    ran = random()
    brushColor(255, 100 + int(150* ran), 0)
    global count
    a = 0.9 * ran + 0.1
    y = 700 * random()
    deleteObject(starMas[count % starAmount])
    starMas[count % starAmount] = polygon([(1200 + 0 * a, y - 16 * a), (1200 - 25 * a, y - 34 * a), (1200 - 15 * a, y - 5 * a),
    (1200 - 40 * a, y + 13 * a), (1200 - 9 * a, y + 13 * a), (1200 + 0 * a, y + 40 * a), (1200 + 9 * a, y + 13 * a), (1200 + 40 * a, y + 13 * a),
    (1200 + 15 * a, y - 5 * a), (1200 + 25 * a, y - 34 * a)])
    count += 1

onTimer(starLaunch, 500 )#долет до звезд


# ДВИЖЕНИЕ
def starPush():
    for i in range(starAmount):
        moveObjectBy(starMas[i], -2-count2 // 4, 0)

onTimer(starPush, 10)

# КОНТРОЛЬ
count2 = 0
def control(event):
    global shot, count2
    # ДВИЖЕНИЕ Старкиллера
    if event.keycode == VK_UP:
        moveObjectBy(telo, 0, -20)
        moveObjectBy(strip1, 0, -20)
        moveObjectBy(strip2, 0, -20)
        moveObjectBy(gun, 0, -20)
    if event.keycode == VK_DOWN:
        moveObjectBy(telo, 0, 20)
        moveObjectBy(strip1, 0, 20)
        moveObjectBy(strip2, 0, 20)
        moveObjectBy(gun, 0, 20)
    if event.keycode == VK_LEFT:
        moveObjectBy(telo, -5, 0)
        moveObjectBy(strip1, -5, 0)
        moveObjectBy(strip2, -5, 0)
        moveObjectBy(gun, -5, 0)
    if event.keycode == VK_RIGHT:
        moveObjectBy(telo, 5, 0)
        moveObjectBy(strip1, 5, 0)
        moveObjectBy(strip2, 5, 0)
        moveObjectBy(gun, 5, 0)
    # СТРЕЛЬБА
    if event.keycode == VK_SPACE:
        penSize(10)
        penColor(220,0,0)
        shot = line(150,yCoord(gun)+22,1200,yCoord(gun)+22)
        penColor(0, 0, 0)
        penSize(1)
        for i in range(starAmount):
            if yCoord(gun)+15 > coords(starMas[i])[1] and yCoord(gun)+15 < coords(starMas[i])[3] :
                deleteObject(starMas[i])
                starMas[i] = line(0,0,0,0)
                count2 +=1

onKey(control)
shot = line(0,0,0,0)


# ЗАДЕРЖКА УДАЛЕНИЯ
def zaderahka():
    global shot
    deleteObject(shot)

onTimer(zaderahka,50)


run()
