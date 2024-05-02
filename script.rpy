﻿
    #this starts the game 
    #intro
    #chapter1
    #chapter2
    #chapter3
    #end

#HERE WE DEFINE THE CHARACTERS

define user=Character("[username]",color="#1613bd")

#CHARACTERS OF SECOND CHAPTER
define h =Character("Unknown", color="#bd1313")
define s =Character("Student", color="#cd6012")
define st =Character("Stranger", color="#28aadd")
define r =Character("Nurse", color="#117428")
define f =Character("Mr. Charles", color="#a22d5f")
define mi =Character("Mina", color="#e63abe")
define am =Character("Amber", color="#620c5d")


#GLITSH EFFECT

image glitshed:
    At("bg eyes", glitch)
    pause 0.2
    At("bg eyes", glitch)
    pause 0.1
    At("bg eyes", glitch)
    pause 0.3
    repeat


image glitshed2:
    At("bg eyes2", glitch)
    pause 0.2
    At("bg eyes2", glitch)
    pause 0.1
    At("bg eyes2", glitch)
    pause 0.3
    repeat


#SPLASHSCREEN

label splashscreen:
    scene black
    pause 2.0
    scene bg splash1 with dissolve
    pause 3.0
    scene black with fade
    return

#START OF THE GAME

label start:
    scene black with fade
    pause 1.0
    #$ renpy.movie_cutscene("kidnapscene",delay=5,loops=0,stop_music=True)
    "Welcome to a world where every choice molds your fate,where excitement beckons at every corner!"
    "Prepare yourself for a majestic journey unlike any other.."
    "one you never imagined would be yours to live. And who's to say it couldn't happen to you one day!"
    "Whoever doubts... You'll be prepared to confront it by this game.."
    "But before that let’s get to know you brave user..."
    $ username=renpy.input("What's your name?",length=32)
    $ username=username.strip()
    $ username= username.capitalize()

    if not username:
        "Hmmm it seems you won't tell us your name"
        menu:
            "Alright what's your gender?"
            "Female":
                jump Female
            "Male":
                jump Male
        label Female:
        "Hmm let's call you Lina "
        $ username="Lina"
        jump next
        label Male:
        "Hmm let's call you Leo "
        $ username="Leo"

    label next:
    "Welcome, dear [username] ! May the clarity of your mind guide your steps, for your choices design your life.."
    

    window hide
   
    scene black with dissolve
    pause 2.0
    scene bg years with dissolve
    pause 4.0
    scene black with dissolve
    pause 2.0
    scene bg kidhospital  #with hpunch
    pause 1.5
    scene black
    pause 1.0
    scene bg cryingroom
    pause 1.5
    scene black
    pause 1.0

    scene bg flowers
    pause 1.5
    scene black
    pause 1.0
    scene bg boy
    pause 1.5
    scene black
    pause 0.8
    
    scene bg flowers
    pause 1.0
    scene black
    pause 0.8
    scene bg boy
    pause 0.8
    scene black
    pause 0.5

    scene bg flowers
    pause 0.2
    scene black
    pause 0.1
    scene bg boy
    pause 0.2
    scene black
    pause 0.1

    scene bg flowers
    pause 0.2
    scene black
    pause 0.1
    scene bg boy
    pause 0.2
    scene black
    pause 0.1

    scene bg flowers
    pause 0.2
    scene black
    pause 0.1
    scene bg boy
    pause 0.2
    scene black
    pause 0.1

    scene bg flowers
    pause 0.2
    scene black
    pause 0.1
    scene bg boy
    pause 0.2
    scene black
    pause 0.1

    scene bg flowers
    pause 0.2
    scene black
    pause 0.1
    scene bg boy
    pause 0.2
    scene black
    pause 3.0

    scene bg depressed with dissolve
    pause 5.0
    scene black with dissolve
    pause 1.5
    scene bg trust with dissolve
    pause 4.0
    scene black with dissolve
    pause 3.0



    #SECOND CHAPTER

    scene glitshed
    h "Oh [username] i liked how obedient you were ! You have now successfully completed your first task."
    h "Now, it's the time to announce you the second one !"
    h "Since you're intelligent, you'll understand that the level of this task will be higher than the previous one."
    h "I'm counting on you not to leave any trace behind if you want to stay safe."
    scene black with dissolve
    centered "https://maps.app.goo.gl/ZA9nnregckawGs1m9"
    menu:  
        "A link is shared."     
        "What's this?":
            jump whats_this
        "Let's see":
            jump lets_see

label whats_this:
    scene glitshed with dissolve
    h "Are you scared? Idiot.This link won't redirect you to another hacker.."
    scene glitshed2 with dissolve
    h "the problems that have fallen on your head are scary enough to fall into the same trap again, hahaha!"
    jump lets_see

label lets_see:
    scene black with dissolve
    pause 1.0
    scene bg univ with dissolve
    "The link leads to the location of Saint Jack University in the neighboring city."
    scene glitshed with dissolve
    h "We will play a game with the money you stole, what do you think?"
    h "A young beautiful girl will benefit from them."
    h "She's a petite girl, with green eyes, red-haired, and wears glasses."
    h "She's truly distinctive,the most beautiful girl in the university. You'll recognize her instantly."
    h 'You must convince this beautiful girl to accompany you. For a simple reason,you have to torture her so that she may suffer a little'
    h "but be careful not to kill her, she wasn\'t guilty."
    h 'Let her family trust that "their daughter passed away"'
    h "I would like to see her sad, all wounded face."
    h "I know you didn't understand. How to convince them that she is dead while she isn't? That's the game we're going to play with the stolen money!"
    h "as for the large sum of money, you will give it to her so that she leaves the village and goes as far away as possible, never to return"
    menu:
        "I got your point":
            jump got_point

label got_point:
    h "And be sure, she must never come back!"
    scene black with dissolve
    pause 0.5
    scene bg myroom with dissolve
    "Well, you see that things are getting worse and worse..."
    "What a sick hacker and what a crazier request! you still can't see what drives him to do this."
    "Either he has scores to settle or he's insane, picking people to see them suffer."
    user "Let's recap his demands..."
    user "To torture a college girl and make her family believe she's dead with proof of it, the money is for her to leave."
    user "He really insists she must not come back so they believe her death. Oh, he also said she wasn't guilty..."
    user "Then who is guilty?"

    scene black with dissolve
    "Next day...\n
    DAY -- OF ADVENTURE."

    scene bg run with dissolve
    "It's time to head over there and embark on an adventure crazier than the first."
    scene bg waytown with dissolve
    "You took your way to the university."
    scene bg gate with dissolve
    "Upon arrival, you found on your right, the university gate"
    scene bg studentsgate with dissolve
    "on your left, a group of students who have already left."
    scene black with dissolve
    menu:
        "Where do you want to go?"
        "Right":
            jump right
        "Left":
            jump left

label right:
    scene bg gate with dissolve
    "You waited outside the university for a long time, not knowing what time she would come out."
    scene bg running with dissolve
    "You caught sight of her from afar, you believe it's her. She started running towards a bus."
    menu:
        "What will you do?"
        "Chase after the bus":
            jump Chase
        "I prefer to ask students about her":
            jump left

label left:
    scene bg studentsgate with dissolve
    "You just have to ask this group of students a few questions intelligently to gather some information about this girl."
    menu:
        "What will you do?"
        "Come up with a story so they won't suspect anything":
            jump story
        "Be honest and tell them that you need some information about her":
            jump honest

label Chase:
    scene bg villagewaybus with dissolve
    "You begin to chase after this bus. It stops at the edge of the city"
    scene black with dissolve
    pause 0.5
    scene bg carwait with dissolve
    "and the girl waits in a square. You think she's waiting for another bus or someone who is supposed to pick her up."
    "A very classy black car comes to pick her up, an elderly man wearing a white apron is driving, you think that he's her dad. She gets in"
    scene bg chaseblackcar with dissolve
    "They took a very bumpy road, it may be the road to the village."
    scene black with dissolve
    pause 0.5
    scene bg housevillage with dissolve
    "After ten minutes, the car takes a small turn and parks right next to it."
    "You continue on, trying not to look like you're following them. From a distance, you observe a very beautiful house."
    scene black with dissolve
    user "But who is that one !!!"
    scene bg oldman with dissolve
    'Suddenly, an elderly man stops right above me.'
    menu:
        st "Hey you, do you need something?"
        "Oh yes, yes. My mother sent me to the redheard's mother":
            jump Yes
        "Run away without giving any answer":
            jump run

label Yes:
    scene bg oldman
    st "The mother of a redhead? I think you're mistaken!"
    st "The redhead you're talking about has been living alone with her father in that villa across the street for years..."
    st "I don't know who you're talking about."
    user "Ahhh sorry I must have made a mistake. Thank you !!"
    scene black with dissolve
    pause 0.5
    scene bg village with dissolve
    user "So, this girl's only family is her father! And he's likely a doctor."
    user "I believe I simply need to find out more about this man; his expertise might be beneficial to me!"
    scene black with dissolve
    "You go back home.."
    menu:
        "What are your plans for the next day?"
        "Go to the hospital to talk to her father":
            jump talk_right
        "Go to the hospital to inquire about her father":
            jump inquire_right   

label run:
    scene black with dissolve
    pause 1.0
    scene bg village with dissolve
    "You quickly start the car, truly afraid of leaving any trace of pursuit, and you head back home. "
    user "Hmm... The man i saw might be her father and he's a doctor."
    user "I believe I simply need to find out more about this man; his expertise might be beneficial to me!"
    scene black with dissolve
    "You go back home.."
    menu:
        "What are your plans for the next day?"
        "Go to the hospital to talk to her father":
            jump talk_right
        "Go to the hospital to inquire about her father":
            jump inquire_right   


label story:
    scene bg studentsgate with dissolve
    user "Um, hey guys, hi. I'm looking for the prettiest girl around here. They told me to contact her."
    s"Yeah, I think the most beautiful girl, who everyone in the university thinks is the most beautiful, is Mina."
    user "Mina?"
    s "Yeah, that little redhead.She lives in the small village nearby."
    s "She's a medical student because her father, who is a forensic doctor, really wanted her to be a doctor like him"
    s "And she is a big fan of making short films she's popular here"
    user "And what time does she finish her classes?"
    s "She finishes everyday around 4:30 pm"
    user "Thank you for your help!"
    scene black with dissolve
    pause 0.5
    scene bg waytown with dissolve
    user "Hmm, Mina, a medical student, lives in the village nearby. Her father is a forensic doctor..."
    user "I believe I simply need to find out more about this man; his expertise might be beneficial to me!"
    scene black with dissolve
    "You go back home.."
    menu:
        "What do you want to do for the next day?"
        "Go to the hospital to talk to her father":
            jump talk_left
        "Go to the hospital to inquire about her father":
            jump inquire_left

label honest:
    scene bg studentsgate with dissolve
    user "Hey guys, do you know a little redhead around here?"
    s "Yes, why? What do you want from her?"
    "You tell them that you need to gather some information about her... \n Everyone looks at you strangely.."
    s "Mina, the forensic doctor's daughter, the big fan of making short films hahaha! She gets out at 4:30 PM, you can ask her directly."
    "You realize that you won't earn any information about her from them"
    user "Daamn! that wasn't the better choice"
    scene black with dissolve
    pause 0.5
    scene black with dissolve
    pause 1.0
    scene bg waytown with dissolve
    "You're in your way to return home.."
    user "Hmm, so her name is Mina and her father is a forensic doctor."
    user "I believe I simply need to find out more about this man; his expertise might be beneficial to me!"
    scene black with dissolve
    menu:
        "What are your plans for the next day?"
        "Go to the hospital to talk to her father":
            jump talk_left
        "Go to the hospital to inquire about her father":
            jump inquire_left

label inquire_left:
    scene black with dissolve
    "Next day..."
    scene bg hospitalgate with dissolve
    "You're heading straight to the hospital of the neighboring city to inquire about the forensic doctor."
    scene bg infirmiere with dissolve
    r "How may i help you?"
    user "Ohh.. Hello, who is your forensic doctor here?"
    r "Mr Charles, our forensic doctor, who has extensive experience"
    r "And is well-known in our city and even the neighboring towns due to the shortage of doctors, so he often travels."
    user "He's the father of the beautiful redhead, right!"
    r "Exactly, after losing his wife, his daughter is his only hope in life. She's everything in his eyes. Anyway, what do you need?"
    user "You mentioned that he travels a lot, so his work schedule is consistently busy?"
    r "Exactly, sometimes he's away from the hospital for several days to treat cases outside the city."
    r "He handles almost all the cases from several cities."
    r "Oh, there he is, going to his office. You can talk to him."
    scene bg turnsee with dissolve
    "You turned around to see him, since he won't be available here for the next few days..."
    scene bg infirmiere with dissolve
    user "Thank you for your help i must go now i will come back another time."
    scene black with dissolve
    pause 0.5
    scene bg gateinside with dissolve
    "You step out the hospital door with your heart pounding and begin to connect the dots"
    user "Charles, our forensic doctor, is popular in his city and the neighboring towns because of the shortage of doctors requiring him to travel."
    user "Consequently, Mina is left alone for days since he's all she has."
    user "Could this information help me?"
    user "If Mina is not guilty, could her father be involved?"
    user "If yes, what's the connection between our forensic doctor and our insane hacker?"
    user "He wants to target his daughter because she's all he has left, and he absolutely wants him to believe she's dead and never return."
    user " I'm losing my mind.. I don't think I'll be able to gather more information on them. It's time to tackle something else."
    user "Mr. Charles won't be available tomorrow, so I think I'll be able to work peacefully."
    scene black with dissolve
    menu:
        "So, how would you go about completing this task ?"
        "Invent a story to make the hacker believe that I've executed his requests":
            jump Invent
        "Execute what I've been asked to do from the hacker, there is no risk for me":
            jump execute

label inquire_right:
    scene black with dissolve
    "Next day..."
    scene bg hospitalgate with dissolve
    "You're heading straight to the hospital of the neighboring city to inquire about Mina's father"
    scene bg infirmiere with dissolve
    r "How may i help you?"
    user "Ohh.. Hello, i'm looking for the redhead's father,he's a doctor here"
    r "Ahh you mean Mr Charles, our forensic doctor, who has extensive experience"
    r "And is well-known in our city and even the neighboring towns due to the shortage of doctors, so he often travels."
    r "Exactly, he's the father of the popular redhead, after losing his wife, his daughter is his only hope in life. She's everything in his eyes."
    r "Anyway, what do you need?"
    user "You mentioned that he travels a lot, so his work schedule is consistently busy?"
    r "Exactly, sometimes he's away from the hospital for several days to treat cases outside the city."
    r "He handles almost all the cases from several cities."
    r "Oh, there he is, going to his office. You can talk to him."
    scene bg turnsee with dissolve
    "You turned around to see him.."
    scene bg infirmiere with dissolve
    user "Thank you for your help i must go now i will come back another time."
    scene black with dissolve
    pause 0.5
    scene bg gateinside with dissolve
    "You step out the hospital door with your heart pounding and begin to connect the dots"
    user "Charles, our forensic doctor, is popular in his city and the neighboring towns because of the shortage of doctors requiring him to travel."
    user "Consequently, Mina is left alone for days since he's all she has."
    user "Could this information help me?"
    user "If Mina is not guilty, could her father be involved?"
    user "If yes, what's the connection between our forensic doctor and our insane hacker?"
    user "He wants to target his daughter because she's all he has left, and he absolutely wants him to believe she's dead and never return."
    user " I'm losing my mind, I don't think I'll be able to gather more information on them. It's time to tackle something else."
    user "Mr. Charles won't be available tomorrow, so I think I'll be able to work peacefully."
    scene black with dissolve
    menu:
        "So, how would you go about completing this task ?"
        "Invent a story to make the hacker believe that I've executed his requests":
            jump Invent
        "Execute what I've been asked to do from the hacker, there is no risk for me":
            jump execute


label talk_left: 
    scene black with dissolve
    "Next day..."
    scene bg hospitalgate with dissolve
    "You're heading straight to the hospital of the neighboring city to inquire about the forensic doctor."
    scene bg infirmiere with dissolve
    r "How may i help you?"
    user "Ohh.. Hello, who is your forensic doctor here?"
    r "Mr Charles, our forensic doctor, who has extensive experience"
    r "And is well-known in our city and even the neighboring towns due to the shortage of doctors, so he often travels."
    user "He's the father of the beautiful redhead, right!"
    r "Exactly, after losing his wife, his daughter is his only hope in life. She's everything in his eyes."
    r "Anyway, what do you need?"
    user "I need to talk to him please"
    r "Of course, you'll find his office on the first floor, first door on the left."
    scene bg stairs with dissolve
    "You make your way up the stairs, feeling the adrenaline coursing through you as you rehearse your words..."
    scene bg hallway with dissolve
    "Standing before his office door, you tap gently.."
    scene bg forensic with dissolve
    "It swings open to reveal him, inviting you in with a warm smile."
    f "How can i assist you?"
    "Disturbed, you try to invent a story to interact with him"
    user "In reality, I have a relative who passed away yesterday in the neighboring town"
    user "And they still haven't found a forensic doctor to handle his case."
    user "I heard about you, so I didn't hesitate to come here and ask for your help."
    f "I see. Who was the doctor who was handling his case before his passing?"
    user "I don't have any idea"
    f "one second please.."
    scene black with dissolve
    "He picked up his phone and stats a call."
    f "Heyy man, umm i have a quick question, did u work yesterday? no? Alright I thought you might have forgotten to inform me."
    'He hung up, and suddenly the office became quiet.'
    scene bg forensic with dissolve
    f 'Dr khalid, this forensic doctor can help you, he\'s very competent, ask the nurse for his address'
    scene bg hallway with dissolve
    "You find this behavior very peculiar, yet you calmly exit the office."
    user "But who was that on the phone? Surely, he isa doctor and he works only with him"
    scene black with dissolve
    pause 0.5
    scene bg gateinside with dissolve
    "You step out the hospital door with your heart pounding and begin to connect the dots"
    user "Charles, our forensic doctor, is popular in his city and the neighboring towns because of the shortage of doctors requiring him to travel."
    user "Consequently, Mina is left alone for days since he's all she has, he works with one and only doctor"
    user "Could this information help me?"
    user "Why he works with one and only doctor?"
    user "And if Mina is not guilty, could her father be involved?"
    user "If yes, what's the connection between our forensic doctor and our insane hacker?"
    user "He wants to target his daughter because she's all he has left, and he absolutely wants him to believe she's dead and never return."
    user " I'm losing my mind.. I don't think I'll be able to gather more information on them. It's time to tackle something else."
    scene black with dissolve
    menu:
        "How would you go about completing this task ?"
        "Invent a story to make the hacker believe that I've executed his requests":
            jump Invent
        "Execute what I've been asked to do from the hacker, there is no risk for me":
            jump execute
        
label talk_right:
    scene black with dissolve
    "Next day..."
    scene bg hospitalgate with dissolve
    "You're heading straight to the hospital of the neighboring city to inquire about Mina's father"
    scene bg infirmiere with dissolve
    r "How may i help you?"
    user "Ohh.. Hello, i'm looking for the redhead's father,he's a doctor here"
    r "Ahh you mean Mr Charles, our forensic doctor"
    r "He has extensive experience and is well-known in our city and even the neighboring towns due to the shortage of doctors, so he often travels."
    r "Exactly, he's the father of the popular redhead, after losing his wife, his daughter is his only hope in life. She's everything in his eyes."
    r "Anyway, what do you need?"
    user "I need to talk to him please"
    r "Of course, you'll find his office on the first floor, first door on the left."
    scene bg stairs with dissolve
    "You make your way up the stairs, feeling the adrenaline coursing through you as you rehearse your words."
    scene bg hallway with dissolve
    "Standing before his office door, you tap gently, and it swings open to reveal him, inviting you in with a warm smile."
    scene bg forensic with dissolve
    f "How can i assist you?"
    "Disturbed, you try to invent a story to interact with him"
    user "In reality, I have a relative who passed away yesterday in the neighboring town"
    user "And they still haven't found a forensic doctor to handle his case."
    user "I heard about you, so I didn't hesitate to come here and ask for your help."
    f "I see. Who was the doctor who was handling his case before his passing?"
    user "I don't have any idea"
    f "one second please.."
    scene black with dissolve
    "He picked up his phone and stats a call."
    f "Heyy man, umm i have a quick question, did u work yesterday? no? Alright I thought you might have forgotten to inform me."
    "He hung up, and suddenly the office became quiet."
    scene bg forensic with dissolve
    'He wrote something on a piece of paper and handed it to you: "Here, this forensic doctor can help you; he\'s very competent."'
    scene black with dissolve
    pause 1.0
    scene bg hallway with dissolve
    "You find this behavior very peculiar, yet you calmly exit the office."
    user "But who was that on the phone? Surely, he isa doctor and he works only with him"
    scene black with dissolve
    pause 0.5
    scene bg gateinside with dissolve
    "You step out the hospital door with your heart pounding and begin to connect the dots"
    user "Charles, our forensic doctor, is popular in his city and the neighboring towns because of the shortage of doctors requiring him to travel."
    user "Consequently, Mina is left alone for days since he's all she has, he works with one and only doctor"
    user "Could this information help me? Why he works with one and only doctor?"
    user "And if Mina is not guilty, could her father be involved?"
    user "If yes, what's the connection between our forensic doctor and our insane hacker?"
    user "He wants to target his daughter because she's all he has left, and he absolutely wants him to believe she's dead and never return."
    scene black with dissolve
    user " I'm losing my mind ! I don't think I'll be able to gather more information on them. It's time to tackle something else."
    menu:
        "So, how would you go about completing this task ?"
        "Invent a story to make the hacker believe that I've executed his requests":
            jump Invent
        "Execute what I've been asked to do from the hacker, there is no risk for me":
            jump execute
      
label execute:
    scene black with dissolve
    user "I come back the next day to wait for her to kidnap her. I don't give a damn about this story."
    scene bg waytown with dissolve
    "You return home and think about where to hide her to torture her..."
    user " She must not recognize me, and besides, I'll lose money..."
    user "Well, losing a little money now is better than staying terrified like this.."
    scene black with dissolve
    "The day after..."
    scene bg minagate with dissolve
    "You park in front of the university and wait. She just came out."
    menu:
        "What will you do?"
        "Tell her that your father sent me to take you back":
            jump yrfather_sentme
        "Violently kidnap her":
            jump kidnap

    label yrfather_sentme:
        scene bg minagate with dissolve
        user "Hey Mina, your dad sent me to take you back home to the village."
        mi "Oh really?... "
        user "Yeah, I'm a hospital agent, and he told me he'll be late today take her instead of me."
        mi "Oh, I'm not quite sure. My father has never done anything like this; I should ask him."
        "You must intervene to prevent her actions, and to do so, your only option is to kidnap her."
        jump kidnap

label kidnap:
        scene black with hpunch
        pause 1.0
        "you grab her violently, she starts screaming, people start looking at you, and you quickly flee by taking her in the car."
        scene black with dissolve
        pause 1.0
        scene bg village with dissolve
        "You stop at an isolated place"
        scene black with dissolve
        "smash her phone, throwing the sum of money at her face and start screaming on her"
        scene bg redheadcar with dissolve
        user "I've already helped you a lot with this money, so you'd better listen to me."
        mi "What's wrong with you !!"
        user "Look, I won't talk too much... You'll take this sum of money and leave this country now."
        user "I don't want any trace of you here, your father must believe that from now you're considered DEAD!"
        mi "Who do you think you are! I'm not afraid from you! Take your money back and let me go peacefully"
        user "Well, she is a hard-headed person, talking to her won't work."
        scene black with dissolve
        "you start hitting her in the face"
        scene bg hit1 with hpunch
        pause 2.0
        scene black with dissolve
        pause 1.0
        scene bg hit2 with hpunch
        pause 2.0
        scene black with dissolve
        pause 2.0
        scene bg hit2 with dissolve
        mi "Okay, okay, I'll do whatever you want, just stop please!"
        user "If you go back, believe me you'll find your father dead in the middle of your village."
        scene black with dissolve
        user "Hey pretty girl, smile for the camera !!"
        scene bg hitpic with dissolve
        pause 3.0
        scene black with dissolve
        pause 1.0
        scene bg bluecar with dissolve
        "you take her to another city and throw her there, shouting"
        scene bg hit2 with dissolve
        user "Figure it out!"
        scene black with dissolve
        "You return home.."
        'Arriving home, you open your PC and find a news circulating on social media..'
        "Mina, the only daughter of Dr. Charles, passed away mysteriously"
        'Suddenly, your screen goes black, and the hacker\'s voice returns...'
        scene black with dissolve
        pause 1.0
        scene glitshed with dissolve
        h "Well dooone! you've done an excellent job my ex-military"
        scene glitshed2
        h "What a pleasure to see people suffering !"
        h "Now all that's left is for me to give you your last mission."
        scene black with dissolve
        user "Ohhhh god I narrowly escaped..."
        scene black with dissolve
        "Suddenly, you hear the sound of police surrounding your house."
        scene bg police with dissolve
        user "DAMNN!!"
        "The university gate cameras captured everything, you've been located by the police."
        scene black with dissolve
        centered "GAME OVER!"
        "Wait a minute..."
        scene black with dissolve
        pause 1.0
        scene glitshed with dissolve
        "It was dumb to make that choice, wasn't it?"
        "You didn't go to prison for the money you stole, but you'll go for a bad choice, poor [username], you make bad decisions to save your life"
        h "Well, our poor [username] couldn't survive."
        scene glitshed2
        h "No matter, I'll just find another victim, hahahaha."
        scene black with dissolve
        pause 1.0
        scene bg splash1 with dissolve
        pause 1.0
        return
    
label Invent:
    scene black with dissolve
    pause 1.0
    scene bg cafeteria with dissolve
    "You enter a coffee and start contemplating how to take that girl with you satisfied, so her father won't search for her."
    user "Anyway, there's not much time left for the 7 days to pass, so I think it's doable to hide her from the world for a few days."
    "You remember you have a group of friends who enjoy making short films for social media"
    user "Perhaps she'll be interested in this request, especially if we can convince her."
    user "I don't think she'll refuse that. And if she does, she'll never turn down that large sum of money."
    "You send to the group leader"
    scene black with dissolve
    pause 1.0
    scene bg phone1 with dissolve
    pause 3.0
    scene bg phone2
    pause 3.0
    scene bg phone3
    pause 3.0
    scene bg phone4
    pause 3.0
    scene bg phone5
    pause 5.0
    scene black with dissolve
    "Next day..."
    "You explained your situation to them and that you need to take her for a few days."
    scene bg minagate with dissolve
    "Mina exits the university gate, and Amber heads straight toward her to talk her."
    scene bg amber
    am "Hey, you're truly beautiful! Would you like to be part of a crime short film with my team?"
    am "They're over there, you won't regret it. And, of course, you'll be paid for your work. What do you think?"
    scene bg minagate
    " Dazzled by the offer..."
    mi "That's all what i love!"
    mi "But how long will this job take?"
    scene bg amber
    am "Just a few days, it suits you, right?"
    scene bg minagate
    mi "Yes yes, it's just that I need to inform my father"
    scene bg amber
    am "Oh, yes, you'd better inform him"
    scene black with dissolve
    pause 1.0
    scene bg friendsroom with dissolve
    am "Well Mina, this is the studio where we work. Welcome aboard, you're going to love working with us."
    scene bg happyfilm with dissolve
    "Mina were so happy.."
    scene black with dissolve
    "Few moments later,you started the work..."
    scene bg scenered with dissolve
    "Amber applies terrifying makeup on Mina's face and some fake bloods everywhere"
    "They begin filming crime scenes, where the actor committing the crimes is you.."
    scene black with dissolve
    "Let's have that scene.."
    scene bg smilemina with dissolve
    pause 5.0
    scene black with dissolve
    "Mission accomplished !"
    "You get permission from the group to leave, since your role is finished"
    "You go back home.."
    scene bg sendpic with dissolve
    user "This will make the insane hacker believe that  I tortured her.."
    user "And for sure after all that torture, he thinks that she definitely won't come back here."
    user "She'll be scared for herself and for her father too."
    user "Well, let's not forget that she won't be missed back in her town since she's here with us."
    scene black with dissolve
    "You place on your computer desk the video of the torture scene of Mina and you wait for the insane hacker to arrive."
    scene black with dissolve
    "After few moments.."
    scene glitshed with dissolve
    h "It turns out that our little one has suffered more than she deserves."
    h "but it's okay, the most important thing is that our Charles is far from his little one who doesn't even know where she is."
    scene glitshed2
    h "Good job, my brave ex-military. See you for your last task, and then freedom to all !"


return
