from time import sleep
from PIL import Image


import cv2
import pytesseract

# img = cv2.imread('qqqq.png')

# text = pytesseract.image_to_string(img)

# print(text)
from pynput.mouse import Button , Controller
from pynput.keyboard import Key, Controller as KeyboardController
import pynput
#
mouse = Controller()
keyboard = KeyboardController()

def copyResult() :
    mouse.position = (0, 0)
    mouse.move(500, 880)
    mouse.click(Button.left, 3)
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)



def switch():
    mouse.position = (100, 100)
    # keyboard.press(Key.alt)
    # keyboard.release(Key.alt)
    # keyboard.press(Key.esc)
    # keyboard.release(Key.esc)
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)

def switch1():
    mouse.position = (100, 100)
    # keyboard.press(Key.alt)
    # keyboard.release(Key.alt)
    # keyboard.press(Key.esc)
    # keyboard.release(Key.esc)
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(2)
    keyboard.release(Key.alt)

def deleteRecentResult():
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)


def pasteResult():
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)

def saveFile():
    keyboard.press(Key.ctrl)
    keyboard.press('s')
    keyboard.release('s')
    keyboard.release(Key.ctrl)

def readFile():
    f = open("text.txt", "r")
    result=f.read()
    # print(result)
    f.close()
    return result

def start():
    copyResult()
    sleep(0.5)
    switch()
    sleep(0.5)
    deleteRecentResult()
    sleep(0.5)
    pasteResult()
    sleep(0.5)
    saveFile()
    sleep(0.5)
    switch1()
    sleep(0.5)
    readFile()

# start()

str=[]
str=readFile()
# print(str)
# print(str.split(","))
value=0
signe = ""


def getValueResNeutre():
    for i in range(len(str)):
        if str[i]=='R':
            break
    return str[i-3]

def getSigneResNeutre():
    signe=""
    for i in range(len(str)):
        if str[i] == 'R':
            if str[i-4]=="-":
                signe="negative"
                break
            else:
                signe="positive"
                break
    return signe

def getValueSasa():
    for i in range(len(str)):
        if str[i]=='S':
            break
    return str[i-2]
def getSigneSasa():
    signe=""
    for i in range(len(str)):
        if str[i] == 'S':
            if str[i-3]=="-":
                signe="negative"
                break
            else:
                signe="positive"
                break

    return signe



def AddOneSasa():
    mouse.position = (0, 0)
    mouse.move(1070, 360)
    mouse.click(Button.left, 2)
    mouse.position = (0, 0)
    mouse.move(1070, 260)
    mouse.click(Button.left,2)


def AddThreeSasa():
    mouse.position = (0, 0)
    mouse.move(1130, 360)
    mouse.click(Button.left, 2)
    mouse.position = (0, 0)
    mouse.move(1070, 260)
    mouse.click(Button.left,2)


def AddOneRNeutre():
    mouse.position = (0, 0)
    mouse.move(1070, 400)
    mouse.click(Button.left, 2)
    mouse.position = (0, 0)
    mouse.move(1070, 260)
    mouse.click(Button.left, 2)

def AddThreeRNeutre():
    mouse.position = (0, 0)
    mouse.move(1130, 400)
    mouse.click(Button.left, 2)
    mouse.position = (0, 0)
    mouse.move(1070, 260)
    mouse.click(Button.left, 2)


value =0

def main():
    sasa = 33
    res_neutre = 0
    # while(res_neutre <= 5):
    #     sleep(2)
    #     AddOneRNeutre()
    #     sleep(2)
    #     start()
    #     sleep(2)
    #     # print(getSigneResNeutre())
    #     # print(getValueResNeutre())
    #     if getSigneResNeutre() == "positive":
    #         res_neutre =res_neutre +int(getValueResNeutre())
    #     if getSigneResNeutre() == "negative":
    #         res_neutre = res_neutre-int(getValueResNeutre())
    #
    #     print(res_neutre)
    while( sasa <= 34):
        if sasa < 33 :
            AddThreeSasa()
            sleep(2)
            start()
            sleep(2)
            if getSigneSasa() == "positive":
                sasa = sasa + int(getValueSasa())
                print(getValueSasa())

            if getSigneSasa() == "negative":
                print(getValueSasa())
                sasa = sasa - int(getValueSasa())
        else:
            AddOneSasa()
            sleep(3)
            start()
            sleep(3)
            if getSigneSasa() == "positive":
                sasa = sasa + int(getValueSasa())
            if getSigneSasa() == "negative":
                sasa = sasa - int(getValueSasa())
        print(sasa)
        print("Sagesse : "+getValueSasa()+" and is "+getSigneSasa())


main()




def augmSasa(sasa):
    AddThreeSasa()
    sleep(2)
    start()
    sleep(2)
    if getSigneSasa() == "positive":
        sasa= +int(getValueSasa())

    if getSigneSasa() == "negative":
        sasa = -int(getValueSasa())
    else:
        AddOneRNeutre()
        sleep(3)
        start()
        sleep(3)
        if getSigneSasa() == "positive":
            sasa = +int(getValueSasa())
        if getSigneSasa() == "negative":
            sasa = -int(getValueSasa())


def augmRNeutre():
    res_neutre=value
    AddOneRNeutre()
    sleep(2)
    start()
    sleep(2)
    if getSigneResNeutre() == "positive":
        res_neutre = +int(getValueResNeutre())
    if getSigneResNeutre() == "negative":
        res_neutre = -int(getValueResNeutre())

    return res_neutre


# print("Sagesse : "+getValueSasa()+" and is "+getSigneSasa())
# print("Résistance Neutre : "+getValueResNeutre()+" and is "+getSigneResNeutre())




