import tkinter 
import random

def exit_dice():
    root.quit()

def display_dice_images(one,two, three,four,five,six,seven,eight,nine,ten,eleven,twelve):
    display_image(f"dice{one}.png", image_label1)
    display_image(f"dice{two}.png", image_label1)
    display_image(f"dice{three}.png", image_label1)
    display_image(f"dice{four}.png", image_label1)
    display_image(f"dice{five}.png", image_label1)
    display_image(f"dice{six}.png", image_label1)
    display_image(f"dice{seven}.png", image_label1)
    display_image(f"dice{eight}.png", image_label1)
    display_image(f"dice{nine}.png", image_label1)
    display_image(f"dice{ten}.png", image_label1)
    display_image(f"dice{eleven}.png", image_label1)
    display_image(f"dice{twelve}.png", image_label1)
    


def restart_btn():
    global win, total, lose_count, hearts
    image_label1.place_forget()
    result_label.config(text='')
    canvas.pack_forget()
    win = 0
    total = 0
    lose_count = 0
    hearts = 3
    canvas.pack(fill=tkinter.BOTH, expand=True)
    update_hearts()
    stats_label.config(text='')
    odd_button.place(x=1040, y=800)
    even_button.place(x=150, y=800)
    update_stats()

def start_game():

    odd_button.place(x=10, y=500)
    even_button.place(x=800, y=500)

def display_image(image_path, label):
    image = tkinter.PhotoImage(file=image_path)
    label.config(image=image)
    label.image = image
    label.place(x=409,y=280)

def randomdice():
    return random.randint(1, 12)

def compareoddeven(a, b):
    return a % 2 == b % 2

def winrate(win, total):
    return win / total * 100

def update_stats():
    stats_label.config(text=f'승률: {winrate(win, total):.2f}% ({win} 승 / {total} 전)')

def update_hearts():
    hearts_label.config(text=f'하트: {"❤" * hearts}',bg="black")

def click_btn(guess):
    global win, lose_count, total, hearts
    rdice = randomdice()
    total += 1
    if rdice == 1:
        display_image(f"one.png", image_label1)
    elif rdice == 2:
        display_image(f"two.png", image_label1)
    elif rdice == 3:
        display_image(f"three.png", image_label1)
    elif rdice == 4:
        display_image(f"four.png", image_label1)
    elif rdice == 5:
        display_image(f"five.png", image_label1)
    elif rdice == 6:
        display_image(f"six.png", image_label1)
    elif rdice == 7:
        display_image(f"seven.png", image_label1)
    elif rdice == 8:
        display_image(f"eight.png", image_label1)
    elif rdice == 9:
        display_image(f"nine.png", image_label1)
    elif rdice == 10:
        display_image(f"ten.png", image_label1)
    elif rdice == 11:
        display_image(f"eleven.png", image_label1)
    else:
        display_image(f"twelve.png", image_label1)

    if compareoddeven(rdice, guess):
        win += 1
        result_label.config(text=f' 성공! (주사위 숫자: {rdice})')
   
    else:
        lose_count += 1
        result_label.config(text=f' 실패! (주사위 숫자: {rdice})')
        hearts -= 1
        update_hearts()
        if hearts == 0:
            result_label.config(text=' 게임 종료! 하트가 모두 소진되었습니다.',bg="black")
            result_label.place(x=960, y=180)
            odd_button.place_forget()
            even_button.place_forget()
            update_stats()
            return

    
    update_stats()

#배경 이미지
root = tkinter.Tk()
root.title("홀수 짝수 맞추기")
root.resizable(True, True)
canvas = tkinter.Canvas(root, width=1349, height=899, bg="black")
background_image = tkinter.PhotoImage(file="csbg1.png")
canvas.create_image(675, 450, anchor=tkinter.CENTER, image=background_image)
canvas.pack(fill=tkinter.BOTH, expand=True)

#제목
main_label = tkinter.Label(root, text="CASINO 홀짝 게임", font=("Corbel Light",30,"bold italic"),bg="black", fg="gold")
main_label.place(x=559, y=50)

# Label 위젯 추가
result_label = tkinter.Label(root, text="", font=("Arial", 16,"bold"),fg="white", bg="black")
result_label.place(x=559, y=180)


# 승률 표시를 위한 Label 위젯 추가
stats_label = tkinter.Label(root, text='', font=("Arial",18,"italic"),fg="gold",bg="black")
stats_label.place(x=559, y=120)

# 하트 표시를 위한 Label 위젯 추가
hearts_label = tkinter.Label(root, text='', font=("Arial",15,"bold"),fg="red",bg="black")
hearts_label.place(x=1129, y=150)

# 주사위 홀수 버튼 추가
odd_button = tkinter.Button(root, text="홀수", font=("Corbel Light",20,"bold"),bg="orange",command=lambda: click_btn(1))
odd_button.place(x=1060, y=800)  

#주사위 짝수 버튼 추가 
even_button = tkinter.Button(root, text="짝수", font=("Corbel Light",20,"bold"),bg="orange",command=lambda: click_btn(2))
even_button.place(x=180, y=800)

#주사위 다시하기 버튼 추가
restart_button = tkinter.Button(root, text="다시하기",font=("Corbel Light",20,"bold"),bg="grey",command=restart_btn)
restart_button.place(x=610, y=800)

dice_exit_btn=tkinter.Button(root,text="X",font=("Times New Roman",30),command=exit_dice)
dice_exit_btn.place(x=30,y=30)

# 초기화
win = 0
total = 0
lose_count = 0
hearts = 3

# 이미지 표시를 위한 Label 위젯 추가
image_label1 = tkinter.Label(root)

root.mainloop()