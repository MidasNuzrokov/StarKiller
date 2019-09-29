from graph import *
from random import *

windowSize(1200, 700)
canvasSize(1200, 700)


# ФОН
brushColor(50, 50, 100)
polygon([(0, 0), (0, 700), (1200, 700), (1200, 0)])


# РАКЕТА
brushColor(100,100,100)
telo = circle(100, 350, 80)
penSize(30)
penColor(30,30,30)
strip = line(20,350,180,350)
penColor(0,0,0)
penSize(5)
brushColor(200,0,0)
gun = circle(150,350,20)
penSize(1)

# ПОЯВЛЕИЕ ЗВЁЗД
KOLVO = 20
count = 0
starMas = [line(0,0,0,0)]*KOLVO

def starLaunch():
    if count2 == 100:
        close()
    ran = random()
    brushColor(100 + int(100 * ran), 100 + int(100 * ran), 60)
    global count
    a = 0.9 * ran + 0.1
    y = 700 * random()
    deleteObject(starMas[count % KOLVO])
    starMas[count % KOLVO] = polygon([(1200 + 50 * a, y + 0 * a), (1200 + 60 * a, y + 40 * a), (1200 + 100 * a, y + 50 * a), (1200 + 60 * a, y + 60 * a), (1200 + 50 * a, y + 100 * a), (1200 + 40 * a, y + 60 * a), (1200 + 0 * a, y + 50 * a), (1200 + 40 * a, y + 40 * a)])
    count += 1

onTimer(starLaunch, 500 )


# ДВИЖЕНИЕ
def starPush():
    for i in range(KOLVO):
        moveObjectBy(starMas[i], -2-count2 // 4, 0)

onTimer(starPush, 10)

# КОНТРОЛЬ
count2 = 0
def control(event):
    global shot, count2
    # ДВИЖЕНИЕ РАКЕТЫ
    if event.keycode == VK_UP:
        moveObjectBy(telo, 0, -14)
        moveObjectBy(strip, 0, -14)
        moveObjectBy(gun, 0, -14)
    if event.keycode == VK_DOWN:
        moveObjectBy(telo, 0, 14)
        moveObjectBy(strip, 0, 14)
        moveObjectBy(gun, 0, 14)
    # СТРЕЛЬБА
    if event.keycode == VK_SPACE:
        penSize(30)
        penColor(220,0,0)
        shot = line(150,yCoord(gun)+22,1200,yCoord(gun)+22)
        penColor(0, 0, 0)
        penSize(1)
        for i in range(KOLVO):
            if yCoord(gun)+15 > coords(starMas[i])[1] and yCoord(gun)+15 < coords(starMas[i])[3] :
                deleteObject(starMas[i])
                starMas[i] = line(0,0,0,0)
                count2 +=1


shot = line(0,0,0,0)
onKey(control)

# ЗАДЕРЖКА УДАЛЕНИЯ
def zaderahka():
    global shot
    deleteObject(shot)

onTimer(zaderahka,120)


run()
