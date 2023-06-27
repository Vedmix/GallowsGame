from turtle import *
from random import randrange
from tkinter import *

gallows=Turtle()
text=Turtle()
text_error=Turtle()
words=['Аномалия','Броневик','Вагончик','Гусеница','Двоиться','Египтяне','Жадность','Заложник','Избежать','Красивый']
hints=['Отклонение от нормы.',"Машина с толстой броней.",'Часть поезда.','Насекомое, которое любит листья.','Казаться двойным, как бы удваиваться',
       'Жители пирамид)','Один из семи грехов.','Похищенный человек.','Не знаю, как поддсказать)','Привлекательный.']
words_i=randrange(0,10)
word=list(words[words_i])
word__=[word[0],'_','_','_','_','_','_',word[7]]
error=0
def clear():
    global error
    letter=entry1.get()
    entry1.delete(0)
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

    if letter not in word:
        error += 1
        text.color('red')
        if error == 1:
            # ВЕРЕВКА
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
            text.penup()
            text.goto(325, 230)
            text.pendown()
            text.color('red')
            text.write('Этой буквы в слове нет!',font=('Arial', 20))
            entry1.delete(0)

        elif error == 2:
            # ГОЛОВА
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
            text.penup()
            text.goto(325, 230)
            text.pendown()

            text.write('Этой буквы в слове нет!', font=('Arial', 20))
            text.penup()
            text.goto(325, 195)
            text.pendown()

            text.write(f'Подсказка: {hints[words_i]}', font=('Arial', 20))
            entry1.delete(0)

        elif error == 3:
            # РУКИ
            gallows.begin_fill()
            gallows.color('#ffdfc4')
            gallows.goto(285, 200)
            gallows.goto(165, 200)
            gallows.goto(165, 190)
            gallows.goto(285, 190)
            gallows.goto(285, 200)
            gallows.end_fill()
            gallows.penup()
            gallows.goto(225, 200)
            gallows.pendown()
            gallows.begin_fill()
            gallows.color('#002F55')
            gallows.goto(255, 200)
            gallows.goto(195, 200)
            gallows.goto(195, 190)
            gallows.goto(255, 190)
            gallows.goto(255, 200)
            gallows.end_fill()
            gallows.color('black')
            gallows.goto(285, 200)
            gallows.goto(165, 200)
            gallows.goto(165, 190)
            gallows.goto(285, 190)
            gallows.goto(285, 200)
            text.penup()
            text.goto(325, 230)
            text.pendown()

            text.write('Этой буквы в слове нет!', font=('Arial', 20))
            entry1.delete(0)

        elif error == 4:
            # ТЕЛО
            gallows.penup()
            gallows.goto(225, 193)
            gallows.pendown()
            gallows.begin_fill()
            gallows.color('#002F55')
            gallows.goto(245, 193)
            gallows.goto(245, 143)
            gallows.goto(205, 143)
            gallows.goto(205, 193)
            gallows.end_fill()
            gallows.color('black')
            gallows.goto(245, 193)
            gallows.goto(245, 143)
            gallows.goto(205, 143)
            gallows.goto(205, 193)
            gallows.penup()
            gallows.goto(245, 143)
            gallows.pendown()
            text.penup()
            text.goto(325, 230)
            text.pendown()

            text.write('Этой буквы в слове нет!', font=('Arial', 20))
            entry1.delete(0)

        elif error == 5:
            # НОГИ
            gallows.begin_fill()
            gallows.color('#002F55')
            gallows.goto(245, 123)
            gallows.goto(235, 123)
            gallows.goto(235, 143)
            gallows.end_fill()
            gallows.goto(235, 123)
            gallows.begin_fill()
            gallows.color('#ffdfc4')
            gallows.goto(235, 93)
            gallows.goto(245, 93)
            gallows.goto(245, 123)
            gallows.end_fill()
            gallows.color('black')
            gallows.goto(245, 143)
            gallows.goto(245, 93)
            gallows.goto(235, 93)
            gallows.goto(235, 143)
            gallows.goto(215, 143)
            gallows.begin_fill()
            gallows.color('#002F55')
            gallows.goto(215, 123)
            gallows.goto(205, 123)
            gallows.goto(205, 143)
            gallows.end_fill()
            gallows.goto(205, 123)
            gallows.begin_fill()
            gallows.color('#ffdfc4')
            gallows.goto(205, 93)
            gallows.goto(215, 93)
            gallows.goto(215, 123)
            gallows.end_fill()
            gallows.color('black')
            gallows.goto(215, 143)
            gallows.goto(215, 93)
            gallows.goto(205, 93)
            gallows.goto(205, 143)
            text.penup()
            text.goto(325, 230)
            text.pendown()
            text.clear()
            text.color('black')
            text.write('💀Ты проиграл💀', font=('Arial', 35))
        if error != 5:
            text_error.penup()
            text_error.goto(325, 300)
            text_error.pendown()
            text_error.clear()
            text_error.color('black')
            text_error.write(f'Ошибки: {error} из 5', font=('Arial', 20))
        else:
            text_error.clear()

    if word__ == word:
        text.penup()
        text.goto(325, 230)
        text.pendown()
        text.clear()
        text.color('black')
        text.write('🎉Ты победил🎉', font=('Arial', 35))






























window1=Tk()
window1.geometry("600x600")
entry1=Entry(window1, font=('Arial',16))
entry1.place(x=20,y=20)
btm=Button(window1,text='Ввести', command=clear)
btm.place(x=20,y=60)
btm=Button(window1,text='Закрыть', command=window1.quit)
btm.place(x=80,y=60)

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





window1.mainloop()

# speed(5)
# hideturtle()
#
speed(3)







done()
