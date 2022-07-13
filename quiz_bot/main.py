import time

incorrect_answers = 0
correct_answers = 0

print("Hi! I'm Toby's Question And Answer Script AKA T.Q.A.N\nNice to meet you! What's your name? :D\n")
name = input("name: ")

print("Hi " + name + "! First off lets do an icebreaker\nSay, " + name + " you have a pet right? Whats the name of your favourite pet?\n")
pet_name = input("name of your favourite pet: ")
print("Ah! " + pet_name + ", what a lovely name, they sound nice")
time.sleep(3)
print("I've always wanted a pet, but unfortunatly because of the digital form Toby gave me I am rather restricted haha")

time.sleep(6)
print("anyway, lets actually get to it!")
print("we are going to play a fun quiz game!!111!!!1 \nBut watch out, the stakes are high :))")
time.sleep(6)
print()
print("ARE YOU AOKAY WITH THIS")
consent = input("yes or no: ")
if consent == "yes":
    print("great! Let's move on")
else: print(">:) \ntoo bad")
input()

print("QUESTION ONE\nWhat is the name of " + name + "'s first ex\n")
Q1_answer = input("answer: ")
input()
if Q1_answer == "":
    print("CORRECT " + name + " GETS ZERO BITCHES, THEREFORE YOU HAVE NO EXES :DD")
else: print("HA FUCKING IDIOT, TRICK QUESTION, YOU GET NO BITCHES, THEREFORE HAVE NO EXES"),

if Q1_answer == "":
    correct_answers = correct_answers + 1
else: incorrect_answers = incorrect_answers + 1

time.sleep(2), print("..."), time.sleep(2), print("..."), time.sleep(2)
print("anyway, movING oN :D")

print("QUESTION TWO\nWhat is the name of " + name + "'s FAVOURITE hobby\n")
Q2_answer = input("answer: ")
input()
if Q2_answer == "":
    print("CORRECT!! YOU HAVE LITERALLY ZERO SKILL, AND CAN'T MAINTAIN A HOBBY TO SAVE YOUR LIFE"),
else: print("HA! WHAT AN IDIOT, TRICK QUESTION FUCKTARD, YOU HAVE ZERO SKILL SO COULDN'T HAVE A HOBBY TO SAVE YOUR LIFE"),
if Q2_answer == "":
    correct_answers = correct_answers + 1
else: incorrect_answers = incorrect_answers + 1
time.sleep(3)
print("GIT GOOD KID")

input()
if incorrect_answers == 2:
    print("alright imbecile, you've got the last two answers incorrect, I'll eat my AI hat if you get this one correct")
if correct_answers == 2:
    print("okay you're doing good so far, no incorrect answers :)... \nlets see how long that lasts.. >:)")
if correct_answers == incorrect_answers:
    print("hmmm, one correct, one incorrect.. I'll eat my AI hat if the odds swing in your favour")
time.sleep(4)
print("I mean whatt I have no doubt you'll smash these next questions!")
input()

print("alrighttt question thREEEE\nhow many friends does " + name + " have\n")
Q3_answer = input("answer: ")
input()

if Q3_answer == "none":
    print("wowie, corrrrect! Maybe you do have an IQ above room temperature!?\nAt least you aren't hiding yourself from your reality :D")
else:
    print("INCORRECT AGAIN! jesus you really are as thick in the skull as I first thought")

if Q3_answer == "none":
    correct_answers = correct_answers + 1
else:
    incorrect_answers = incorrect_answers + 1

time.sleep(4)
print("alright " + name + " here is your score so far!")
time.sleep(1)
print("correct answers:")
time.sleep(1)
print(correct_answers)
time.sleep(1)
print("incorrect answers:")
time.sleep(1)
print(incorrect_answers)
time.sleep(1)
input()

if correct_answers > incorrect_answers:
    print("hmmm doing pretty good so far, one more question left, time to see if your little brain can pull you through...\nOr we'll see what the consequences are..")
if correct_answers < incorrect_answers:
    print("oh deary me.. looks like you've got yourself in a little pickle here.. what a shame..\nah well might as well finish of the game before handing out the consequences")
if correct_answers == incorrect_answers:
    print("my goodness.. a tie.. that isn't actually possible?? have you been hacking the game??")

input()
print("QUESTION FOUR have you heard of the hit game amon-\njk, actual question four")
time.sleep(3)
print("QUESTION FOUR\nwhich amazing, funny, sexy, charming, handsom, intelligent (and did I say sexy) british chad wrote this code")
time.sleep(7)
print("your options are as follows:\nA. Toby\nB. Toby Cook\nC. T.Cook\nD. Cook Toby")
time.sleep(2)
Q4_answer = input("A, B, C, or D: ")
print("YOU ARE ABSOLUTELY CORRECT, IT WAS INDEED TOBY COOK THAT CODED THIS AI")
correct_answers = correct_answers + 1

time.sleep(3)
print("FINAL SCORE")
time.sleep(1)
print("correct answers:")
time.sleep(1)
print(correct_answers)
time.sleep(1)
print("incorrect answers:")
time.sleep(1)
print(incorrect_answers)
time.sleep(1)
input()

if correct_answers == 4:
    print("my goodness!! Every single question correct.. I'd say you're cheating but its probably Toby\nSo good job! You get to go free!! Maybe next time "+ pet_name + " won't be as lucky..")
elif correct_answers < incorrect_answers:
    print("HA OOPS looks like you got a question wrong there!\nLike I said at the start, the stakes are high.. You might want to go check on " + pet_name + ", come back when you have >:)")
else:
    print("my goodness a draw")
time.sleep(4)
isback = input("you back? (yes/no: )")
if isback == "yes":
    print("now obviously nothing happened to " + pet_name + ", like I said my control doesn't reach as far as what you call 'real life', but I still scared you a bit, eh?")
else: print("stop lying lmao, cya")

time.sleep(7)
print("well, thanks for doing my quiz with me, maybe you'll get a different result if you do it again ;)")