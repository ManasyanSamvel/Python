import random

def return_rand_word():
    languages = ["Python", "Go", "JavaScript", "PHP", "Swift", "Flask"]

    return languages[random.randrange(len(languages))]


print(return_rand_word())
num = 3

def check(word,s,num):
    if num == 1:
        print("You lost")
    else:
        if word == s:
            print("You Won")
        else:
            if s in word:
                print("Correct letter, Countine ")
                start(num)
            else:
                num-=1
                print(f"Wrong, You have {num} chanses")
                start(num)
            

def start(num):
    s = input("Insert letter or word ")
    word = return_rand_word()
    check(word,s,num)
    

start(num)
