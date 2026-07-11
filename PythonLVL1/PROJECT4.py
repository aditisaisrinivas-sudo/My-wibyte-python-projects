#introduction

print("So, I heard you're looking for the professor huh?")
print("I am his great assistant...I'm sure you've heard of me right!?")
print();

#Quick question

answer = input("Answer yes now! Who hasn't heard of the professors great, awesome, amazing, and extremely talented assistant?")

if answer.lower() == "yes":
    print("I like your answer! I truly am amazing and talented.")
else:
    print("Geez man..ig I'm not that famous afterall...")
print()    
print("Anyway now, let's get started with the quiz. Pass it, and we will get you an appoinment with the professor")
print()

#quiz starts

answer = input("Your first question - what is (4.7)^2")

if answer() == "22.09":
    print("That was an easy question. I'd be shocked if you got it wrong!!")
else:
    print("How could one get that wrong! I am quite disapointed.")
print()


answer = input("Give me a 6 letter word with 2 vowels")
if len(answer) == 6:
    print("Your word has 6 letters. Good...")
    count_a = answer.count('a')
    count_e = answer.count('e')
    count_i = answer.count('i')
    count_o = answer.count('o')
    count_u = answer.count('u')

    count_vowels = count_a+count_e+count_i+count_o+count_u
    if count_vowels > 2:
        print("I said 2 vowels..not how ever many are in that word of yours")
        print("You are wasting my time")
    elif count_vowels < 2:
        print("You can't count to 2 huh? That's less than 2 vowels in your word. ")
        print("What a waste of time..You make me want to retire")
    else:
        print("Why only 2 vowels though.....I expect more from you next time")
else:
    print("What a disaster. The word vowels itself fits the criteria..")
    print("Just listening to you makes my IQ go down.")

print()

sentence = input("Now, tell me a question ending in 'wise assistant' (no question please)\n")
#sentence would end in wise assistant

if sentence.endswith('wise assistant'):
    print("Where's the punctuation??...It seems like you don't know english at all!")
elif sentence.endswith('wise assistant.'):
    len_first = sentence.find('')
    if len_first < 67:
        print('The first word is too short') 
else:
    print("The professor is going to be VERY furious")

print()

sentence = input("Last question - Why should I give you an appoinment with the Professor")

if answer.lower() == "okay":
    print("Wow! What a smart answer...You might be wiser than the professor")
else:
    print("Okay...good to know.")

print()
print("Let's get an appoinment set up for you now. Select your preferred time.")
print("A. 45 minutes past midnight","B. Right now", sep='\t');
print("C. 4 am in the morning", "D. 3 pm in the afternoon", sep='\t')
appointment = input('Select your slot (A/B/C/D)\n')

if appointment == 'A':
    print("oof..bad timing. The professor might not show up")
elif appointment == 'B':
    print("The professor is busy right now! You chose the wrong time!!")
    print("Looks like you're not getting to meet the professor!")
elif appointment == 'C':
    print("The professor will see you then!")
else:
    print("You chose a good time. The professor might be a little sleepy though.")

print()
print("Good luck in your appointment! Bye bye.")





