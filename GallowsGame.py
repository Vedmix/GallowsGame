from turtle import *
from random import *
from tkinter import *
from pygame import *

init()

mixer.music.load("music.mp3")
mixer.music.play()
mixer.music.set_volume(0.02)

window1=Tk()
window1.geometry("1000x730")
window1.resizable(width=False, height=False)
window1.title('GallowsGame')
window1["bg"]='#E3E3E3'


canvas = ScrolledCanvas(window1)
canvas.config(width=900, height=500)
canvas.place(x=50,y=50)

gallows=RawTurtle(canvas)
gallows.hideturtle()

text=RawTurtle(canvas)
text.hideturtle()

text_error=RawTurtle(canvas)
text_error.hideturtle()

text_hint=RawTurtle(canvas)
text_hint.hideturtle()

text_wrong_letter=RawTurtle(canvas)
text_wrong_letter.hideturtle()

text_error_letter=RawTurtle(canvas)
text_error_letter.hideturtle()

error_letter=RawTurtle(canvas)
error_letter.hideturtle()

gallows_x=320
gallows_y=160

words=[]
click=0
error=0

with open('words.txt', encoding='utf-8') as file:
    for line in file:
        sublist = [element for element in line.strip()[1:-1].split(",")]
        words.append(sublist)

colors1 =[
    "#000000", "#FFFFFF", "#FF0000", "#00FF00", "#0000FF",
    "#FFFF00", "#FF00FF", "#00FFFF", "#800000", "#008000",
    "#000080", "#808000", "#800080", "#008080", "#808080",
    "#C0C0C0", "#FF8080", "#80FF80", "#8080FF", "#FFFF80",
    "#FF80FF", "#80FFFF", "#FF0000", "#00FF00", "#0000FF",
    "#FFFF00", "#FF00FF", "#00FFFF", "#800000", "#008000",
    "#000080", "#808000", "#800080", "#008080", "#808080",
    "#C0C0C0", "#FF8080", "#80FF80"]
colors2 = [
    '#000000', '#191970', '#000080', '#00008B', '#0000CD',
    '#0000FF', '#006400', '#008000', '#008080', '#008B8B',
    '#00BFFF', '#00CED1', '#00FA9A', '#00FF00', '#00FF7F',
    '#00FFFF', '#0D98BA', '#191972', '#1E90FF', '#20B2AA',
    '#228B22', '#2E8B57', '#2F4F4F', '#32CD32', '#3CB371',
    '#40E0D0', '#4169E1', '#4682B4', '#483D8B', '#4B0082',
    '#556B2F', '#5F9EA0', '#6495ED', '#663399', '#696969',
    '#708090'
]
wrong_letter=[]
letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
"х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
words_i=randrange(0,29)

word=list(words[words_i][0])

word__=[words[words_i][0][0],'_','_','_','_','_','_',words[words_i][0][7]]




def input_color_active(event):
    event.widget.config(bg='#BBBBBB', activebackground='#7CFC00')
def input_color_passive(event):
    event.widget.config(bg='#E3E3E3')
def close_color_active(event):
    event.widget.config(bg='#BBBBBB', activebackground='red')
def close_color_passive(event):
    event.widget.config(bg='#E3E3E3')
def stop_color_active(event):
    global click
    click += 1
    if click % 2 !=0:
        event.widget.config(bg='#BBBBBB', activebackground='red')
    elif click % 2 == 0:
        event.widget.config(bg='#BBBBBB', activebackground='#7CFC00')

def stop_color_passive(event):
    event.widget.config(bg='#E3E3E3')
def only_one(a):
    entry1.delete ('0',END)
def stop_music():
    if click% 2 !=0:
        mixer.music.stop()
    elif click % 2 == 0:
        mixer.music.play()



def enter_press(event):
    clear()



def clear():
    global error
    global wrong_letter
    letter=entry1.get()
    letter=letter.lower()
    entry1.delete(0)
    btm_done.config(state="disabled")
    entry1.config(state="readonly")
    text_error_letter.clear()

    if letter in letters:
        if (letter in word__) or (letter == words[words_i][0][0]) or (letter == words[words_i][0][7]):
            text_error_letter.penup()
            text_error_letter.goto(325-gallows_x, 230-gallows_y)
            text_error_letter.pendown()
            text_error_letter.color('red')

            error_letter.clear()
            text_error_letter.write('Буква уже введена!', font=('Arial', 20))
            btm_done.config(state="normal")
            entry1.config(state="normal")
        if letter in word:
            count = word.count(letter)
            if count == 1:
                index = word.index(letter)
                if (index != words[words_i][0][0]) and (index != words[words_i][0][7]):
                    word__[index] = letter
                    text.penup()
                    text.goto(325-gallows_x, 265-gallows_y)
                    text.pendown()
                    text.clear()
                    text.color('black')
                    text.write(
                        f'Загаданное слово: {word__[0]+" "+ word__[1] +" "+ word__[2] +" "+ word__[3] +" "+ word__[4] + " "+word__[5] +" "+ word__[6] +" "+ word__[7]}',
                        font=('Arial', 20))
            if count >1:
                if letter == words[words_i][0][0]:
                    index = word.index(letter,word.index(letter)+1)
                elif letter == words[words_i][0][7]:
                    index = word.index(letter)
                elif (letter != words[words_i][0][0]) and (letter != words[words_i][0][7]):
                    index = word.index(letter)
                    word__[index] = letter
                    index = word.index(letter, word.index(letter) + 1)
                    word__[index] = letter

                word__[index] = letter
                text.penup()
                text.goto(325-gallows_x, 265-gallows_y)
                text.pendown()
                text.clear()
                text.color('black')
                text.write(
                    f'Загаданное слово: {word__[0] + " " + word__[1] + " " + word__[2] + " " + word__[3] + " " + word__[4] + " " + word__[5] + " " + word__[6] + " " + word__[7]}',
                    font=('Arial', 20))

            btm_done.config(state="normal")
            entry1.config(state="normal")


        if letter not in word:
            if letter in wrong_letter:

                text_error_letter.penup()
                text_error_letter.goto(325-gallows_x, 230-gallows_y)
                text_error_letter.pendown()
                text_error_letter.color('red')

                error_letter.clear()
                text_error_letter.write('Буква уже введена!', font=('Arial', 20))
                btm_done.config(state="normal")
                entry1.config(state="normal")
            else:
                error += 1
                wrong_letter.append(letter)
                text_error_letter.clear()
                if error == 1:
                    # ВЕРЕВКА

                    btm_done.config(state="disabled")
                    gallows.begin_fill()
                    gallows.color('#bb7733')
                    gallows.goto(225-gallows_x, 250-gallows_y)
                    gallows.goto(220-gallows_x, 250-gallows_y)
                    gallows.goto(220-gallows_x, 325-gallows_y)
                    gallows.end_fill()
                    gallows.penup()
                    gallows.goto(225-gallows_x, 325-gallows_y)
                    gallows.pendown()
                    gallows.color('black')
                    gallows.goto(225-gallows_x, 250-gallows_y)
                    gallows.goto(220-gallows_x, 250-gallows_y)
                    gallows.goto(220-gallows_x, 325-gallows_y)
                    error_letter.penup()
                    error_letter.goto(325-gallows_x, 230-gallows_y)
                    error_letter.pendown()
                    error_letter.color('red')
                    error_letter.write('Этой буквы в слове нет!',font=('Arial', 20))
                    entry1.delete(0)
                    entry1.config(state="normal")
                    btm_done.config(state="normal")

                elif error == 2:
                    # ГОЛОВА

                    btm_done.config(state="disabled")
                    gallows.penup()
                    gallows.goto(225-gallows_x, 250-gallows_y)
                    gallows.pendown()
                    gallows.begin_fill()
                    gallows.color('#ffdfc4')
                    gallows.right(180)
                    gallows.circle(25)
                    gallows.end_fill()
                    gallows.color('black')
                    gallows.penup()
                    gallows.goto(225-gallows_x, 250-gallows_y)
                    gallows.pendown()
                    gallows.circle(25)
                    gallows.penup()
                    gallows.goto(225-gallows_x, 200-gallows_y)
                    gallows.pendown()
                    error_letter.penup()
                    error_letter.goto(325-gallows_x, 230-gallows_y)
                    error_letter.pendown()
                    error_letter.color('red')
                    error_letter.write('Этой буквы в слове нет!', font=('Arial', 20))
                    entry1.delete(0)
                    entry1.config(state="normal")
                    btm_done.config(state="normal")


                elif error == 3:
                    # РУКИ

                    btm_done.config(state="disabled")
                    gallows.begin_fill()
                    gallows.color('#ffdfc4')
                    gallows.goto(285-gallows_x, 200-gallows_y)
                    gallows.goto(165-gallows_x, 200-gallows_y)
                    gallows.goto(165-gallows_x, 190-gallows_y)
                    gallows.goto(285-gallows_x, 190-gallows_y)
                    gallows.goto(285-gallows_x, 200-gallows_y)
                    gallows.end_fill()
                    gallows.color('black')
                    gallows.goto(195-gallows_x, 200-gallows_y)
                    gallows.goto(195-gallows_x, 190-gallows_y)
                    gallows.penup()
                    gallows.goto(225-gallows_x, 200-gallows_y)
                    gallows.pendown()
                    gallows.begin_fill()
                    gallows.color('#1ed013')
                    gallows.goto(255-gallows_x, 200-gallows_y)
                    gallows.goto(195-gallows_x, 200-gallows_y)
                    gallows.goto(195-gallows_x, 190-gallows_y)
                    gallows.goto(255-gallows_x, 190-gallows_y)
                    gallows.goto(255-gallows_x, 200-gallows_y)
                    gallows.end_fill()
                    gallows.color('black')
                    gallows.goto(195-gallows_x, 200-gallows_y)
                    gallows.goto(195-gallows_x, 190-gallows_y)
                    gallows.goto(195-gallows_x, 200-gallows_y)
                    gallows.goto(255-gallows_x, 200-gallows_y)
                    gallows.goto(255-gallows_x, 190-gallows_y)
                    gallows.goto(285-gallows_x, 190-gallows_y)
                    gallows.goto(285-gallows_x, 200-gallows_y)
                    gallows.goto(165-gallows_x, 200-gallows_y)
                    gallows.goto(165-gallows_x, 190-gallows_y)
                    gallows.goto(195-gallows_x, 190-gallows_y)
                    gallows.goto(205-gallows_x, 190-gallows_y)
                    gallows.penup()
                    gallows.goto(245-gallows_x, 190-gallows_y)
                    gallows.pendown()
                    gallows.goto(285-gallows_x, 190-gallows_y)
                    gallows.penup()
                    gallows.goto(245-gallows_x, 190-gallows_y)
                    gallows.pendown()
                    error_letter.penup()
                    error_letter.goto(325-gallows_x, 230-gallows_y)
                    error_letter.pendown()
                    error_letter.color('red')
                    error_letter.write('Этой буквы в слове нет!', font=('Arial', 20))
                    if (words_i!=0) and (words_i!=4) and (words_i!= 9) and (words_i!= 13) and (words_i!=17) and (words_i!=18) and (words_i != 25):
                        text_hint.penup()
                        text_hint.goto(325 - gallows_x, 200 - gallows_y)
                        text_hint.pendown()
                        text_hint.write(f'Подсказка: {words[words_i][1]}', font=('Arial', 20))
                        text_hint.penup()
                        text_hint.goto(325 - gallows_x, 165 - gallows_y)
                        text_hint.pendown()
                        text_hint.write(f' {words[words_i][2]}', font=('Arial', 20))
                    else:
                        text_hint.penup()
                        text_hint.goto(325 - gallows_x, 200 - gallows_y)
                        text_hint.pendown()
                        text_hint.write(f'Подсказка: {words[words_i][1]}', font=('Arial', 20))

                    entry1.delete(0)
                    entry1.config(state="normal")
                    btm_done.config(state="normal")

                elif error == 4:
                    # ТЕЛО

                    btm_done.config(state="disabled")
                    gallows.begin_fill()
                    gallows.color('#1ed013')
                    gallows.goto(245-gallows_x, 190-gallows_y)
                    gallows.goto(245-gallows_x, 150-gallows_y)
                    gallows.goto(205-gallows_x, 150-gallows_y)
                    gallows.goto(205-gallows_x, 190-gallows_y)
                    gallows.end_fill()
                    gallows.color('black')
                    gallows.goto(205-gallows_x, 190-gallows_y)
                    gallows.goto(205-gallows_x, 150-gallows_y)
                    gallows.goto(245-gallows_x, 150-gallows_y)
                    gallows.goto(245-gallows_x, 190-gallows_y)
                    error_letter.penup()
                    error_letter.goto(325-gallows_x, 230-gallows_y)
                    error_letter.pendown()
                    error_letter.color('red')
                    error_letter.write('Этой буквы в слове нет!', font=('Arial', 20))
                    entry1.delete(0)
                    entry1.config(state="normal")
                    btm_done.config(state="normal")


                elif error == 5:
                    # НОГИ

                    btm_done.config(state="disabled")
                    gallows.penup()
                    gallows.goto(245-gallows_x, 150-gallows_y)
                    gallows.pendown()
                    gallows.begin_fill()
                    gallows.color('#ffdfc4')
                    gallows.goto(245-gallows_x, 90-gallows_y)
                    gallows.goto(235-gallows_x, 90-gallows_y)
                    gallows.goto(235-gallows_x, 140-gallows_y)
                    gallows.goto(215-gallows_x, 140-gallows_y)
                    gallows.goto(215-gallows_x, 90-gallows_y)
                    gallows.goto(205-gallows_x, 90-gallows_y)
                    gallows.goto(205-gallows_x, 150-gallows_y)
                    gallows.end_fill()
                    gallows.begin_fill()
                    gallows.color('#1ed013')
                    gallows.goto(245-gallows_x, 150-gallows_y)
                    gallows.goto(245-gallows_x, 120-gallows_y)
                    gallows.goto(235-gallows_x, 120-gallows_y)
                    gallows.goto(235-gallows_x, 140-gallows_y)
                    gallows.goto(215-gallows_x, 140-gallows_y)
                    gallows.goto(215-gallows_x, 120-gallows_y)
                    gallows.goto(205-gallows_x, 120-gallows_y)
                    gallows.goto(205-gallows_x, 150-gallows_y)
                    gallows.end_fill()
                    gallows.color('black')
                    gallows.penup()
                    gallows.goto(245-gallows_x, 90-gallows_y)
                    gallows.pendown()
                    gallows.goto(235-gallows_x, 90-gallows_y)
                    gallows.goto(235-gallows_x, 140-gallows_y)
                    gallows.goto(215-gallows_x, 140-gallows_y)
                    gallows.goto(215-gallows_x, 90-gallows_y)
                    gallows.goto(205-gallows_x, 90-gallows_y)
                    gallows.goto(205-gallows_x, 150-gallows_y)
                    gallows.goto(245-gallows_x, 150-gallows_y)
                    gallows.goto(245-gallows_x, 120-gallows_y)
                    gallows.goto(235-gallows_x, 120-gallows_y)
                    gallows.goto(235-gallows_x, 140-gallows_y)
                    gallows.goto(215-gallows_x, 140-gallows_y)
                    gallows.goto(215-gallows_x, 120-gallows_y)
                    gallows.goto(205-gallows_x, 120-gallows_y)
                    gallows.goto(205-gallows_x, 150-gallows_y)
                    gallows.goto(245-gallows_x, 150-gallows_y)
                    gallows.goto(245-gallows_x, 90-gallows_y)
                    error_letter.penup()
                    error_letter.goto(325-gallows_x, 230-gallows_y)
                    error_letter.pendown()
                    text_error.clear()
                    text.penup()
                    text.goto(-445, 50)
                    text.pendown()
                    text.clear()
                    text_hint.clear()
                    text_error.clear()
                    text.color('black')
                    error_letter.clear()
                    text_wrong_letter.clear()
                    gallows.clear()
                    while True:
                        text.color(colors2[randint(0, 35)])
                        text.write('💀ВЫ ПРОИГРАЛИ💀', font=('Arial', 70))
                        entry1.config(state="readonly")
                        btm_done.config(state="disabled")


                if error != 5 :
                    text_error.penup()
                    text_error.goto(325-gallows_x, 300-gallows_y)
                    text_error.pendown()
                    text_error.clear()
                    text_error.color('black')
                    text_error.write(f'Ошибки: {error} из 5', font=('Arial', 20))

                    text_wrong_letter.penup()
                    text_wrong_letter.goto(325-gallows_x, 100-gallows_y)
                    text_wrong_letter.pendown()
                    text_wrong_letter.clear()
                    text_wrong_letter.color('black')
                    text_wrong_letter.write(f'Введенные буквы: {wrong_letter}', font=('Arial', 20))


                else:
                    text_error.clear()


        if word__ == word:
            text_error.clear()
            text.penup()
            text.goto(-420,50)
            text.pendown()
            text.clear()
            text_hint.clear()
            text_error.clear()
            text.color('black')
            error_letter.clear()
            text_wrong_letter.clear()
            gallows.clear()
            while True:
                text.color(colors1[randint(0, 35)])
                text.write('🎆ВЫ ПОБЕДИЛИ🎆', font=('Arial', 70))
                entry1.config(state="readonly")
                btm_done.config(state="disabled")
    else:
        text_error_letter.penup()
        text_error_letter.goto(325-gallows_x, 230-gallows_y)
        text_error_letter.pendown()
        text_error_letter.color('red')

        error_letter.clear()
        text_error_letter.write('Введена некорректная буква!', font=('Arial', 20))
        btm_done.config(state="normal")
        entry1.config(state="normal")









lbl1=Label(window1, text='Привет! Я загадал слово из восьми букв, попробуй его отгадать.', bg='#E3E3E3', font=('Arial', 16))
lbl1.place(x=185,y=570)
lbl2=Label(window1,text='Буква:', bg='#E3E3E3', font=('Arial', 16))
lbl2.place(x=295,y=600)
entry1=Entry(window1, font=('Arial',16))
entry1.place(x=367,y=600)
btm_done=Button(window1,text='Ввести букву', bg='#E3E3E3', font=('Arial', 16), command=clear)
btm_done.place(x=300,y=640)
btm_close=Button(window1,text='Закрыть', bg='#E3E3E3', font=('Arial', 16), command=window1.destroy)
btm_close.place(x=455,y=640)
btm_stop=Button(window1,text='⬛', bg='#E3E3E3', font=('Arial', 16), command=stop_music)
btm_stop.place(x=565,y=640)

btm_done.bind('<Enter>', input_color_active)
btm_done.bind('<Leave>', input_color_passive)
btm_close.bind('<Enter>', close_color_active)
btm_close.bind('<Leave>', close_color_passive)
btm_stop.bind('<Enter>', stop_color_active)
btm_stop.bind('<Leave>', stop_color_passive)
entry1.bind('<KeyPress>',only_one)
entry1.bind('<Return>', enter_press)

entry1.config(state="readonly")
btm_done.config(state="disabled")

gallows.penup()
gallows.goto(0-gallows_x,0-gallows_y)
gallows.pendown()

gallows.speed(10)
gallows.begin_fill()
gallows.color('#F5D033')
gallows.goto(300-gallows_x,0-gallows_y)
gallows.goto(300-gallows_x,25-gallows_y)
gallows.goto(-25-gallows_x,25-gallows_y)
gallows.goto(-25-gallows_x,0-gallows_y)
gallows.goto(0-gallows_x,0-gallows_y)
gallows.end_fill()

gallows.begin_fill()
gallows.goto(0-gallows_x,350-gallows_y)
gallows.goto(25-gallows_x,350-gallows_y)
gallows.goto(25-gallows_x,0-gallows_y)
gallows.end_fill()

gallows.goto(0-gallows_x,325-gallows_y)

gallows.begin_fill()
gallows.goto(225-gallows_x,325-gallows_y)
gallows.goto(225-gallows_x,350-gallows_y)
gallows.goto(0-gallows_x,350-gallows_y)
gallows.end_fill()

gallows.begin_fill()
gallows.goto(75-gallows_x,325-gallows_y)
gallows.goto(25-gallows_x,275-gallows_y)
gallows.goto(25-gallows_x,250-gallows_y)
gallows.goto(100-gallows_x,325-gallows_y)
gallows.end_fill()

gallows.penup()
gallows.goto(0-gallows_x,0-gallows_y)
gallows.pendown()

gallows.pensize(3)
gallows.color('black')
gallows.goto(300-gallows_x,0-gallows_y)
gallows.goto(300-gallows_x,25-gallows_y)
gallows.goto(-25-gallows_x,25-gallows_y)
gallows.goto(-25-gallows_x,0-gallows_y)
gallows.goto(0-gallows_x,0-gallows_y)
gallows.penup()
gallows.goto(0-gallows_x,25-gallows_y)
gallows.pendown()
gallows.goto(0-gallows_x,350-gallows_y)
gallows.goto(25-gallows_x,350-gallows_y)
gallows.goto(25-gallows_x,25-gallows_y)
gallows.penup()
gallows.goto(25-gallows_x,325-gallows_y)
gallows.pendown()
gallows.goto(225-gallows_x,325-gallows_y)
gallows.goto(225-gallows_x,350-gallows_y)
gallows.goto(25-gallows_x,350-gallows_y)
gallows.penup()
gallows.goto(75-gallows_x,325-gallows_y)
gallows.pendown()
gallows.goto(75-gallows_x,325-gallows_y)
gallows.goto(25-gallows_x,275-gallows_y)
gallows.goto(25-gallows_x,250-gallows_y)
gallows.goto(100-gallows_x,325-gallows_y)
gallows.speed(2)

gallows.penup()
gallows.goto(225-gallows_x,325-gallows_y)
gallows.pendown()
gallows.speed(2)

text.penup()
text.goto(325-gallows_x, 265-gallows_y)
text.pendown()
text.clear()
text.write(
    f'Загаданное слово: {word__[0]+" "+ word__[1] +" "+ word__[2] +" "+ word__[3] +" "+ word__[4] + " "+word__[5] +" "+ word__[6] +" "+ word__[7]}',
    font=('Arial', 17))
btm_done.config(state="normal")
entry1.config(state="normal")

window1.mainloop()