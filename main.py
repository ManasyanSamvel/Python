# num1 = int(input("first number"))
# num2 = int(input("second number"))

# if num1.isdigit() and num2.isdigit():
#     num1 = int(num1)
#     num2 = int(num2)
# print(num1*num2)


# x = "Hello world, test, test"
# print(x.replace(',','.' ,1))#copy e anum x-@ ,-i poxaren dnum e .  , poxum e 1 gtac ,


# ! -not
# &&-and
# || - or


# i = 0
# while i<10:
#     i+=1
#     print(i)

# chka i-- kam i++


# "hello"-chpopoxvox masiv

# for i in 'hello':
#     print(i) #tpelu e hertov hello-i tarery tak tak
#for in -y  ashxatum e miayn masivneri het


# x = 'hello'
# for i in range(len(x)):
#     print(i) #tpum e hello-i tarery hertov tak tak index-nerov


# for i in range(2, 5): 
#     print(i) #tpum e 2ic 5(voc neraryal) tvery


# print(len('hello')) # veradarcnum e length-y


# l = [23, 45]
# l1 = ["hello" , 23, True, [45, "hello"], False]

# for i in range(len(l1)):
#     if i==3:
#         for x in l1 [i]:
#             print('----',x)
#     else:
#         print(l1[i])


# poxel masivi andamy mek ayl andamov
# l = ["hello" , 23,  False]
# l[0] = "test"
# l.append(55)

# x = "hello"
# print(l)


# x = 23 
# print(type(x))

# y = str(x)
# print(type(y))


# x = range(10)
# y = list(x)
# print(y)


# l = [33, "hello", True, 12]

# el = l.pop() #hanum e verjin elementy ev veradarcnum stanum enq masiv aranc 12-i
# print(el)

# el1 = l.pop(1)
# print(el1)
# print(l)


# l = [33,12,44,1,99,0]
# l.sort() # sortavorum e yst ajman kargi
# l.sort(reverse=True) #yst nvazman kargi
# print(l)


# def test(name, age):
#     s = f"Name: {name}, Age: {age}" #f"Name"..... - formatavorvox e  #data = "Name: {}, Age: {}".format(name, age) - formatavorum
#     return s


# a = test("John", 30) #karox enq grel nayev  a = test (age = 30, name = "John")
# print(a)


# l = ["hello", "alo", "ab", "test", "esim"]
# l.sort()
# print(l)


#sortavorum yst length-i
# def test(el):
#     return len(el)


# l = ["hello", "alo", "ab", "test", "esim"]
# l.sort(key = test) #sortavorum yst length-i
# print(l)


# sortavorum yst length-i
# l = ["hello", "alo", "ab", "test", "esim"]
# l.sort(key = len) #sortavorum yst length-i
# print(l)


#masivy popoxakani veragreluc masivi linkn e poxvum e popoxutyun aneluc popoxvum e nayev masivy
# l = ["hello", "alo", "ab", "test", "esim"]
# test = l

# test[0] = 12
# print(test)
# print(l)


#chi popoxum skzbnakany aly copy e anum nor poxum
# l = ["hello", "alo", "ab", "test", "esim"]
# test = l.copy()

# test[0] = 12
# print(test)
# print(l)



# l = []
# i = 0;
# while i<5:
#     i+=1
#     x = input("Insert name surname: ")
#     x = x.replace('.', ' ')
#     l.append(x)


# for i in range(len(l)):
#         print(i, l[i])



# l = [12, 34, 45, 56, 43]
# print(l[2:5]) #tpum e 2ic micev 5rd(voch nerarlay) andamy nor masivi mej

# l = [12, 34, 45, 56, 43]
# print(l[2:]) #tpum e 2ic verji andamy nor masivi mej

# l = [12, 34, 45, 56, 43]
# print(l[:5]) #tpum e skzbizic micev 5rd(voch nerarlay) andamy nor masivi mej

# l = [12, 34, 45, 56, 43]
# print(l[2:5]) #tpum e 2ic micev 5rd(voch nerarlay) andamy nor masivi mej

# l = [12, 34, 45, 56, 43]
# print(l[:]) #tpum e bolor arjeqnery nor masivi mej



# l = [12, 34, 45, 56, 43]
# print(67 in l) #stugum e ardyoq ka 67tivy masivi mej veradarcnum e true kam false



# l1 = [2,4,5,1,6,11]
# l2 = [el ** 2 for el in l1]
# print(l2)



# l1 = [2,3,4,5,1,6,11]
# l2 = [el** 2 for el in l1 if el>2]
# print(l2)



# i = 0
# l = []
# while i<4:
#     x = int(input("Insert number"))
#     l.append(x)
#     i+=1

# def input1 (x,j = 0):
    
#     if j< len(x):
#         print(x[j])
#         j+=1
#         input1(x,j)
    

# input1(l)


#--------swap----------
# a = 12
# b = 34
# a,b = b,a # = (a,b) = (b,a)  chi poxum arjeqy ayl tarber havasar tuple-ner en
# print(a,b)

# t = (3,7,9) #chpopoxvox masiv, uni nuyn masivi hnaravorutyunnery, bayc chi popoxvum arjeqnery
# print(t)


#----set----
# s = {44,5,6,23,56,2,44} #uni nuyn masivi hnaravorutyunnery, khane krknvox tvyalnery,  u kdasavore ajman kargov
# print(s)


# l = [2,5,2,8,5,3,2]
# l = list(set(l));
# print(l)



#-----dicitonaries-----
# d = {
#     "name": "John", 
#     "age": 23
# }
# print(d["name"])
# print(d["hello"]) #error
# print(d.get("hello" , "Guest")) #None, ete chka hello-n kvercne Guest arjeq
# print("name" in d)#true, ka name key-ov arjeq
# for i in d.items():
#     print(i) #amen mi arjeqy kdarna tuple

# for key, val in d.items():
#     print(key, val) #tpum e key value

# print(d.values()) #kveradardzne miayn value-nery masivov
# print(d.keys()) #kveradardzne miayn key-ery masivov



# hello = {
#     "hy":"Barev",
#     "en":"Hello",
#     "ru":"Privet",
#     "default":"Unknown language code"
# }
# lang_code = input("Input language code: ")
# print(hello.get(lang_code, hello["default"]))




# def test (*params): #cankacac qanaki argument kvercne yev tuple-ov
#     print(params)


# test(123, 3,45)
# test(12,34,4,5,53,2)



# def test(**params): #vorpes dicitonaries
#     print(params)


# test(age = 23, name = "John")



# def test(age):
#     '''
#     :type: (int)->int            # keyword-er en, type naxatecvace nshelu hamar stacvox arjeqneri type-y
#     :param: age: user age        # keyword-er en, nshum e parametreri anunner
#     :return: user age            # keyword-er en, return-i arjeqy
#     ''' #avelacnum e function -i hamar dakumentacia
#     return age *2


# test(23)
# help(test) #help-ov stanum enq function-i dakumentacia



# print(12,23, end="-----------")
# print(23)

#tnayin grel print function


# import hello.lib
# def test3(s):
#     s = hello.lib.replace_str(s)
#     s = hello.lib.add_symbol(s)

#     print(s)


# test3("Hello, World!")

# print(__name__)


# import math 
# print(dir(math)) #veradarcnum e math - i bolor functionnery


# import numpy as np

# r = np.product([4,4,5])
# print(r)

# languages = ["Python", "Go", "JavaScript", "PHP", "Swift", "Flask"]
# chanse = 3
# name = input("Insert your name ")
# print("You have 3 chanse")
# x = input("Insert word or letter ")
# for i in range(len(languages)):
#     for j in range(len(languages[i])):
#         if x == j:
#             print("Yes")
#             x = input("Countine")
#             if x == i :
#                 print("You win")
#         else:
#             print("Not found, you have -1 chanses")
#             chanse-=1
#             break
#     break
    
# if chanse == 0:
#     print("You Lose")

import random


def return_rand_word():
    languages = ["Python", "Go", "JavaScript", "PHP", "Swift", "Flask"]

    return languages[random.randrange(len(languages))].lower()


print(return_rand_word())

def check(word,s):
    if word == s:
        print("You Won")
    else:
        if s in word:
            pass
        else:
            pass



def start():
    num = 3
    word = return_rand_word()
    print(f"You have {num} chanses")
    s = input("Insert letter or word ").lower()
    check(word,s)



start()