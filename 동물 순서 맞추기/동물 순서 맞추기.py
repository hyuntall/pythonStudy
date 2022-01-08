from tkinter import *
import threading
import random
import os
from PIL import Image, ImageTk
import time

gameCount = 0
gamePoint = 0
gameState = False

def gameStart():

    # 게임 시작 시 0~15의 숫자를 섞어 해당 숫자에 해당하는 동물 텍스트 표시
    random.shuffle(animalList)
    startButton.config(state=DISABLED)
    def textChange():
        global gameState
        for animal in animalList:
            textLabel.config(text = animal)
            print(animal)
            time.sleep(1)
        textLabel.config(text=f"점수: {gamePoint}")
        gameState = not gameState
    # 반복문 실행 시 GUI 응답없음 문제를 해결하기 위한 스레딩
    th = threading.Thread(target=textChange)
    th.start()


def click(animal):
    #전역변수에 접근하기 위해 선언
    global gameCount
    global gamePoint
    global gameState

    if not gameState:
        return
    if animal == animalList[gameCount]:
        print('정답입니다')
        gameCount += 1
        gamePoint += 50
        if len(ent1.get())>0:
            textLabel.config(text=f"{ent1.get()}님의 점수: {gamePoint}")
        else:
            textLabel.config(text=f"플레이어의 점수: {gamePoint}")
        if gameCount == 16:
            textLabel.config(text=f"GameClear!!!")
            gamePoint = 0
            gameCount = 0
            startButton.config(state=NORMAL)
            gameState = not gameState
    else:
        print("틀렸습니다!")
        gameCount = 0
        gamePoint = 0
        textLabel.config(text=f"GameOver 점수: {gamePoint}")
        startButton.config(state=NORMAL)
        gameState = not gameState

window = Tk()
window.title("동물 순서 맞추기")

animalList = ['거북이','원숭이','호랑이','판다','병아리','뱀','참새','용','고래','여우',
              '쥐','사자','강아지','닭','돼지','토끼']

#반복문으로 버튼을 생성한다.
i = 0
for animal in animalList:
    cmd = lambda x=animal: click(x)

    image = Image.open(f'./동물/동물{i}.png')
    resized_img = image.resize((100, 100))
    globals()[f"img{i}"] = ImageTk.PhotoImage(resized_img)
    but = Button(window, text=animal, width=100, height=100, relief='ridge', command=cmd, image=globals()[f"img{i}"])
    but.grid(row=i//4, column=i%4)
    i += 1

ent1 = Entry(window)
ent1.grid(row = 0, column = 4)

#titleLabel = Label(window, text='동물 순서 맞추기', width=15, height=4)
#titleLabel.grid(row = 0, column = 4)
# 게임 진행 상태 표시 레이블
textLabel = Label(window, text='', width=15, height=4)
textLabel.grid(row = 2, column = 4)
# 시작 버튼
startButton = Button(window,text='Start', width=16, height=5, command=gameStart)
startButton.grid(row=1, column=4)
# 프로그램 종료 버튼
exitButton = Button(window,text='Exit', width=16, height=5, command=lambda :window.destroy())
exitButton.grid(row=3, column=4)

window.mainloop()
