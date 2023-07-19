from turtle import *
from random import *
from tkinter import *
import pygame

pygame.init()

pygame.mixer.music.load("music.mp3")

pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.02)

gallows=Turtle()
text=Turtle()
text_error=Turtle()
text_hint=Turtle()
text_wrong_letter=Turtle()
text_wrong_letter.hideturtle()
text_error_letter=Turtle()
text_error_letter.hideturtle()
error_letter=Turtle()
error_letter.hideturtle()
text_hint.hideturtle()
gallows.hideturtle()
gallows.screen.setup(1600,800)
text.hideturtle()
text_error.hideturtle()

file1=open('words.txt', encoding='utf-8')
words=file1.readlines()
file2=open('hints.txt', encoding='utf-8')
hints=file2.readlines()
colors =[
    "#000000", "#FFFFFF", "#FF0000", "#00FF00", "#0000FF",
    "#FFFF00", "#FF00FF", "#00FFFF", "#800000", "#008000",
    "#000080", "#808000", "#800080", "#008080", "#808080",
    "#C0C0C0", "#FF8080", "#80FF80", "#8080FF", "#FFFF80",
    "#FF80FF", "#80FFFF", "#FF0000", "#00FF00", "#0000FF",
    "#FFFF00", "#FF00FF", "#00FFFF", "#800000", "#008000",
    "#000080", "#808000", "#800080", "#008080", "#808080",
    "#C0C0C0", "#FF8080", "#80FF80"]
wrong_letter=[]
letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
"х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
words_i=randrange(0,29)

word=list(words[words_i][:-1])

word__=[word[0],'_','_','_','_','_','_',word[7]]
error=0
def input_color_active(event):
    event.widget.config(bg='#DCDCDC', activebackground='#7CFC00')
def input_color_passive(event):
    event.widget.config(bg='white')
def close_color_active(event):
    event.widget.config(bg='#DCDCDC', activebackground='red')
def close_color_passive(event):
    event.widget.config(bg='white')
def only_one(a):
    entry1.delete ('0',END)

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
        if (letter in word__) and (letter != word[0]) and (letter != word[7]):
            text_error_letter.penup()
            text_error_letter.goto(325, 230)
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
                if (index != word[0]) and (index != word[7]):
                    word__[index] = letter
                    text.penup()
                    text.goto(325, 265)
                    text.pendown()
                    text.clear()
                    text.color('black')
                    text.write(
                        f'Загаданное слово: {word__[0]+" "+ word__[1] +" "+ word__[2] +" "+ word__[3] +" "+ word__[4] + " "+word__[5] +" "+ word__[6] +" "+ word__[7]}',
                        font=('Arial', 20))
            if count >1:
                if letter == word[0]:
                    index = word.index(letter,word.index(letter)+1)
                elif letter == word[7]:
                    index = word.index(letter)
                elif (letter != word[0]) and (letter != word[7]):
                    index = word.index(letter)
                    word__[index] = letter
                    index = word.index(letter, word.index(letter) + 1)
                    word__[index] = letter

                word__[index] = letter
                text.penup()
                text.goto(325, 265)
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
                text_error_letter.goto(325, 230)
                text_error_letter.pendown()
                text_error_letter.color('red')

                error_letter.clear()
                text_error_letter.write('Буква уже введена!', font=('Arial', 20))
            else:
                error += 1
                wrong_letter.append(letter)
                text_error_letter.clear()
                if error == 1:
                    # ВЕРЕВКА

                    btm_done.config(state="disabled")
                    gallows.begin_fill()
                    gallows.color('#bb7733')
                    gallows.goto(225, 250)
                    gallows.goto(220, 250)
                    gallows.goto(220, 325)
                    gallows.end_fill()
                    gallows.penup()
                    gallows.goto(225, 325)
                    gallows.pendown()
                    gallows.color('black')
                    gallows.goto(225, 250)
                    gallows.goto(220, 250)
                    gallows.goto(220, 325)
                    error_letter.penup()
                    error_letter.goto(325, 230)
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
                    gallows.goto(225, 250)
                    gallows.pendown()
                    gallows.begin_fill()
                    gallows.color('#ffdfc4')
                    gallows.right(180)
                    gallows.circle(25)
                    gallows.end_fill()
                    gallows.color('black')
                    gallows.penup()
                    gallows.goto(225, 250)
                    gallows.pendown()
                    gallows.circle(25)
                    gallows.penup()
                    gallows.goto(225, 200)
                    gallows.pendown()
                    error_letter.penup()
                    error_letter.goto(325, 230)
                    error_letter.pendown()
                    error_letter.color('red')
                    error_letter.write('Этой буквы в слове нет!', font=('Arial', 20))
                    text_hint.penup()
                    text_hint.goto(325, 100)
                    text_hint.pendown()

                    text_hint.write(f'Подсказка: {hints[words_i]}', font=('Arial', 20))
                    entry1.delete(0)
                    entry1.config(state="normal")
                    btm_done.config(state="normal")

                elif error == 3:
                    # РУКИ

                    btm_done.config(state="disabled")
                    gallows.begin_fill()
                    gallows.color('#ffdfc4')
                    gallows.goto(285, 200)
                    gallows.goto(165, 200)
                    gallows.goto(165, 190)
                    gallows.goto(285, 190)
                    gallows.goto(285, 200)
                    gallows.end_fill()
                    gallows.color('black')
                    gallows.goto(195, 200)
                    gallows.goto(195, 190)
                    gallows.penup()
                    gallows.goto(225, 200)
                    gallows.pendown()
                    gallows.begin_fill()
                    gallows.color('#1ed013')
                    gallows.goto(255, 200)
                    gallows.goto(195, 200)
                    gallows.goto(195, 190)
                    gallows.goto(255, 190)
                    gallows.goto(255, 200)
                    gallows.end_fill()
                    gallows.color('black')
                    gallows.goto(195, 200)
                    gallows.goto(195, 190)
                    gallows.goto(195, 200)
                    gallows.goto(255, 200)
                    gallows.goto(255, 190)
                    gallows.goto(285, 190)
                    gallows.goto(285, 200)
                    gallows.goto(165, 200)
                    gallows.goto(165, 190)
                    gallows.goto(195, 190)
                    gallows.goto(205, 190)
                    gallows.penup()
                    gallows.goto(245, 190)
                    gallows.pendown()
                    gallows.goto(285, 190)
                    gallows.penup()
                    gallows.goto(245, 190)
                    gallows.pendown()
                    error_letter.penup()
                    error_letter.goto(325, 230)
                    error_letter.pendown()
                    error_letter.color('red')
                    error_letter.write('Этой буквы в слове нет!', font=('Arial', 20))
                    entry1.delete(0)
                    entry1.config(state="normal")
                    btm_done.config(state="normal")

                elif error == 4:
                    # ТЕЛО

                    btm_done.config(state="disabled")
                    gallows.begin_fill()
                    gallows.color('#1ed013')
                    gallows.goto(245, 190)
                    gallows.goto(245, 150)
                    gallows.goto(205, 150)
                    gallows.goto(205, 190)
                    gallows.end_fill()
                    gallows.color('black')
                    gallows.goto(205, 190)
                    gallows.goto(205, 150)
                    gallows.goto(245, 150)
                    gallows.goto(245, 190)
                    error_letter.penup()
                    error_letter.goto(325, 230)
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
                    gallows.goto(245, 150)
                    gallows.pendown()
                    gallows.begin_fill()
                    gallows.color('#ffdfc4')
                    gallows.goto(245, 90)
                    gallows.goto(235, 90)
                    gallows.goto(235, 140)
                    gallows.goto(215, 140)
                    gallows.goto(215, 90)
                    gallows.goto(205, 90)
                    gallows.goto(205, 150)
                    gallows.end_fill()
                    gallows.begin_fill()
                    gallows.color('#1ed013')
                    gallows.goto(245, 150)
                    gallows.goto(245, 120)
                    gallows.goto(235, 120)
                    gallows.goto(235, 140)
                    gallows.goto(215, 140)
                    gallows.goto(215, 120)
                    gallows.goto(205, 120)
                    gallows.goto(205, 150)
                    gallows.end_fill()
                    gallows.color('black')
                    gallows.penup()
                    gallows.goto(245, 90)
                    gallows.pendown()
                    gallows.goto(235, 90)
                    gallows.goto(235, 140)
                    gallows.goto(215, 140)
                    gallows.goto(215, 90)
                    gallows.goto(205, 90)
                    gallows.goto(205, 150)
                    gallows.goto(245, 150)
                    gallows.goto(245, 120)
                    gallows.goto(235, 120)
                    gallows.goto(235, 140)
                    gallows.goto(215, 140)
                    gallows.goto(215, 120)
                    gallows.goto(205, 120)
                    gallows.goto(205, 150)
                    gallows.goto(245, 150)
                    gallows.goto(245, 90)
                    error_letter.penup()
                    error_letter.goto(325, 230)
                    error_letter.pendown()
                    error_letter.clear()
                    text_wrong_letter.clear()
                    text_hint.clear()
                    text.clear()
                    text.color('black')
                    text.write('💀Ты проиграл💀', font=('Arial', 35))
                    entry1.config(state="readonly")


                if error != 5 :
                    text_error.penup()
                    text_error.goto(325, 300)
                    text_error.pendown()
                    text_error.clear()
                    text_error.color('black')
                    text_error.write(f'Ошибки: {error} из 5', font=('Arial', 20))

                    text_wrong_letter.penup()
                    text_wrong_letter.goto(325, 100)
                    text_wrong_letter.pendown()
                    text_wrong_letter.clear()
                    text_wrong_letter.color('black')
                    text_wrong_letter.write(f'Введенные буквы: {wrong_letter}', font=('Arial', 20))


                else:
                    text_error.clear()


        if word__ == word:
            text_error.clear()
            text.penup()
            text.goto(325, 230)
            text.pendown()
            text.clear()
            text_hint.clear()
            text_error.clear()
            text.color('black')
            error_letter.clear()
            text_wrong_letter.clear()
            while True:
                text.color(colors[randint(0, 35)])
                text.write('🎉Ты победил🎉', font=('Arial', 45))
            entry1.config(state="readonly")
            btm_done.config(state="disabled")
    else:
        text_error_letter.penup()
        text_error_letter.goto(325, 230)
        text_error_letter.pendown()
        text_error_letter.color('red')

        error_letter.clear()
        text_error_letter.write('Введена некорректная буква!', font=('Arial', 20))
        btm_done.config(state="normal")
        entry1.config(state="normal")

gallows.speed(10)
gallows.begin_fill()
gallows.color('#F5D033')
gallows.goto(300,0)
gallows.goto(300,25)
gallows.goto(-25,25)
gallows.goto(-25,0)
gallows.goto(0,0)
gallows.end_fill()
gallows.begin_fill()
gallows.goto(0,350)
gallows.goto(25,350)
gallows.goto(25,0)
gallows.end_fill()
gallows.goto(0,325)
gallows.begin_fill()
gallows.goto(225,325)
gallows.goto(225,350)
gallows.goto(0,350)
gallows.end_fill()
gallows.begin_fill()
gallows.goto(75,325)
gallows.goto(25,275)
gallows.goto(25,250)
gallows.goto(100,325)
gallows.end_fill()
gallows.penup()
gallows.goto(0,0)
gallows.pendown()
gallows.pensize(3)
gallows.color('black')
gallows.goto(300,0)
gallows.goto(300,25)
gallows.goto(-25,25)
gallows.goto(-25,0)
gallows.goto(0,0)
gallows.penup()
gallows.goto(0,25)
gallows.pendown()
gallows.goto(0,350)
gallows.goto(25,350)
gallows.goto(25,25)
gallows.penup()
gallows.goto(25,325)
gallows.pendown()
gallows.goto(225,325)
gallows.goto(225,350)
gallows.goto(25,350)
gallows.penup()
gallows.goto(75,325)
gallows.pendown()
gallows.goto(75,325)
gallows.goto(25,275)
gallows.goto(25,250)
gallows.goto(100,325)
gallows.speed(2)

gallows.penup()
gallows.goto(225,325)
gallows.pendown()
gallows.speed(2)
text.penup()
text.goto(325, 265)
text.pendown()
text.clear()
text.write(
    f'Загаданное слово: {word__[0]+" "+ word__[1] +" "+ word__[2] +" "+ word__[3] +" "+ word__[4] + " "+word__[5] +" "+ word__[6] +" "+ word__[7]}',
    font=('Arial', 20))

window1=Tk()
window1.geometry("680x150")
window1.resizable(width=False, height=False)
lbl1=Label(window1, text='Привет! Я загадал слово из восьми букв, попробуй его отгадать.', font=('Arial', 16))
lbl1.place(x=20,y=20)
lbl2=Label(window1,text='Буква:',font=('Arial', 16))
lbl2.place(x=120,y=50)
entry1=Entry(window1, font=('Arial',16))
entry1.place(x=190,y=50)
btm_done=Button(window1,text='Ввести букву', font=('Arial', 16), command=clear)
btm_done.place(x=150,y=90)
btm_close=Button(window1,text='Закрыть', font=('Arial', 16), command=window1.quit)
btm_close.place(x=310,y=90)


btm_done.bind('<Enter>', input_color_active)
btm_done.bind('<Leave>', input_color_passive)
btm_close.bind('<Enter>', close_color_active)
btm_close.bind('<Leave>', close_color_passive)
entry1.bind('<KeyPress>',only_one)


window1.mainloop()

done()
