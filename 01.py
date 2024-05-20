import turtle
import random
import time

        




def draw_gallows():
    t.penup()
    t.setpos(20, -100)
    t.pendown()
    t.forward(100)
    t.backward(50)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.backward(20)
    t.left(90)
    t.forward(20)


def draw_head():
    t.penup()
    t.setpos(-30, 60)
    t.pendown()
    t.circle(20)


def draw_body():
    t.penup()
    t.setpos(-10, 40)
    t.pendown()
    t.forward(40)


def draw_left_arm():
    t.penup()
    t.setpos(-10, 40)
    t.pendown()
    t.left(45)
    t.forward(20)


def draw_right_arm():
    t.penup()
    t.setpos(-10, 40)
    t.pendown()
    t.right(90)
    t.forward(20)


def draw_left_leg():
    t.penup()
    t.setpos(-10, 0)
    t.pendown()
    t.left(45)
    t.forward(20)


def draw_right_leg():
    t.penup()
    t.setpos(-10, 0)
    t.pendown()
    t.right(-45)
    t.forward(20)


def choose_word():
    words = [
        "автомобиль",
        "банан",
        "карандаш",
        "скрипка",
        "компьютер",
        "пельмени",
        
    ]
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter

        else:
            display += " [_] "
    return display


def hangman_visual():
    word_to_guess = choose_word()
    guessed = False
    guessed_letters = []
    tries = 6
    tt.penup()
    tt.setpos(0,-200)
    tt.pendown()
    tt.write("Давай поиграем в 'Виселицу'!")
    tt.penup()
    tt.setpos(0,-220)
    tt.pendown()
    tt.write(display_word(word_to_guess, guessed_letters))
    timing = time.time()
    while True:
        if time.time() - timing > 1.0:
            timing = time.time()
            tt.clear()
            break
            
            
    
    while not guessed and tries > 0:
        guess = turtle.textinput("Угадай букву", " и введи слово целиком")

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                tt.penup()
                
                tt.setpos(0,-280)
                tt.pendown()
                tt.write("Ты уже угадал эту букву:", guess)
                while True:
                  if time.time() - timing > 8.0:
                      timing = time.time()
                      tt.clear()
                      break

            elif guess not in word_to_guess:
                tt.penup()
                
                tt.setpos(0,-280)
                tt.pendown()
                tt.write((guess, "нет в слове."))
                while True:
                  if time.time() - timing > 8.0:
                      timing = time.time()
                      tt.clear()
                      break
                print
                tries -= 1
                guessed_letters.append(guess)
                if tries == 5:
                    draw_gallows()
                elif tries == 4:
                    draw_head()
                elif tries == 3:
                    draw_body()
                elif tries == 2:
                    draw_left_arm()
                elif tries == 1:
                    draw_right_arm()
                elif tries == 0:
                    draw_left_leg()
                    draw_right_leg()
            else:
                tt.penup()
                
                tt.setpos(0,-200)
                tt.pendown()
                tt.write("Отлично, " + guess + " есть в слове!  ")
                tt.penup()
                
                tt.setpos(10,-220)

                
                
                
                
               
                tt.pendown()
                tt.write(display_word(word_to_guess, guessed_letters))
                
                
                guessed_letters.append(guess)

            print(display_word(word_to_guess, guessed_letters))

        elif len(guess) == len(word_to_guess) and guess.isalpha():
            if guess == word_to_guess:
                guessed = True
            else:
                tries = 0

        else:
            print("Некорректный ввод.")

    if guessed:
        
        tt.penup()
        tt.setpos(-10,-230)
        tt.pendown()
        tt.write('победа слово было  ',move=True)
        tt.write(word_to_guess)
        
            
        
    else:
        tt.penup()
        tt.setpos(-10,-250)
        tt.pendown()
        tt.write('поражение слово было  ',move=True)
        tt.write(word_to_guess)
        

tt = turtle.Turtle()
t = turtle.Turtle()
hangman_visual()
turtle.mainloop()
