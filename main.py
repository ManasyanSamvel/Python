import random

def return_rand_word():
    languages = ["Python", "Go", "JavaScript", "PHP", "Swift", "Flask"]

    return languages[random.randrange(len(languages))].lower()


print(return_rand_word())

num = 3

def check(word,s):
    if word == s:
        print("You Won")
    else:
        if s in word:
            print("Correct letter, Countine ")
            check(word,s)
        else:
            print(f"Wrong, you have {num} chanses")
            
        



def start():
    word = return_rand_word()
    print(f"You have {num} chanses")
    s = input("Insert letter or word ").lower()
    check(word,s)



start()
