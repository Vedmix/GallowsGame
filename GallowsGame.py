import turtle as t
from random import randrange
#

t.begin_fill()
t.color('brown')
t.forward(300)
t.right(90)
t.forward(25)
t.right(90)
t.forward(300)
t.right(90)
t.forward(25)
t.end_fill()

t.begin_fill()
t.forward(325)
t.right(90)
t.forward(25)
t.right(90)
t.forward(325)
t.end_fill()

t.begin_fill()
t.right(90)
t.forward(50)
t.left(90)
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()

t.goto(0,325)

t.begin_fill()
t.forward(25)
t.right(90)
t.forward(225)
t.right(90)
t.forward(25)
t.right(90)
t.forward(200)
t.end_fill()

t.begin_fill()
t.goto(75,325)
t.goto(25,275)
t.goto(25,250)
t.goto(100,325)
t.end_fill()

t.penup()
t.goto(0,0)
t.color('black')
t.pensize(3)
t.left(180)
t.pendown()

t.forward(300)
t.right(90)
t.forward(25)
t.right(90)
t.forward(325)
t.right(90)
t.forward(25)
t.right(90)
t.forward(50)

t.left(90)
t.forward(325)
t.left(90)
t.forward(25)
t.left(90)
t.forward(325)

t.goto(0,350)
t.left(90)
t.forward(225)
t.right(90)
t.forward(25)
t.right(90)
t.forward(200)

t.goto(75,325)
t.goto(25,275)
t.goto(25,250)
t.goto(100,325)

#ЧЕЛОВЕК

t.penup()
t.goto(225,325)
t.pendown()

words=['Аномалия','Броневик','Вагончик','Гусеница','Двоиться','Египтяне','Жадность','Заложник','Избежать','Красивый']
hints=['Отклонение от нормы.',"Машина с толстой броней.",'Часть поезда.','Насекомое, которое любит листья.','Казаться двойным, как бы удваиваться',
       'Жители пирамид)','Один из семи грехов.','Похищенный человек.','Не знаю, как поддсказать)','Привлекательный.']
print('Привет, я загадал слово из 8 букв, поробуй его отгадать)')
print('Удачи!')
words_i=randrange(0,10)
word=list(words[words_i])
word__=[word[0],'_','_','_','_','_','_',word[7]]
word_index=[]
# print(word)
print(word__)
error=0
for i in range(0,14):
    letter = input('Введи букву >> ')
    if letter in word:
        count=word.count(letter)
        if count == 1:
            index=word.index(letter)
            if (index != word[0]) and (index != word[7]):
                word__[index]=letter
                print(word__)
    if letter not in word:

        error+=1
        if error == 1:
            #Веревка
            t.begin_fill()
            t.forward(6)
            t.left(90)
            t.forward(75)
            t.left(90)
            t.forward(6)
            t.left(90)
            t.forward(75)
            t.end_fill()
            t.left(180)
            t.forward(75)
            t.right(90)
            print('Этой буквы в слове нет!')

        elif error == 2:
            #ГОлова
            t.pensize(5)
            t.circle(25)
            t.pensize(3)
            print('Этой буквы в слове нет!')
            print(hints[words_i])

        elif error == 3:
            #Руки
            t.penup()
            t.goto(225,200)

            t.pendown()
            t.forward(56)
            t.left(90)
            t.forward(2)
            t.left(90)
            t.forward(112)
            t.left(90)
            t.forward(2)
            t.left(90)
            t.forward(56)
            print('Этой буквы в слове нет!')

        elif error == 4:
            #Тело
            t.pensize(5)
            t.left(180)
            t.forward(20)
            t.right(90)
            t.forward(100)
            t.right(90)
            t.forward(40)
            t.right(90)
            t.forward(100)
            t.left(180)
            t.forward(100)
            print('Этой буквы в слове нет!')

        elif error == 5:
            #Ноги
            t.forward(50)
            t.left(180)
            t.forward(50)
            t.right(90)
            t.forward(40)
            t.right(90)
            t.forward(50)
            print('В следующий раз повезет)')
            break
    if word__==word:
        print('Ты победил!')
        break




t.done()

s=2