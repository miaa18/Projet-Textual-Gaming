
label start:
    #this starts the game 
    #intro
    #chapter1
    #chapter2
    #chapter3
    #end
    "this is start of the game"

    
label screensplash:
    pause 2.0
    scene bg screensplash with dissolve
    pause 3.0
    hide bg screensplash with fade
    pause 1.0

define h =Character("Hacker", color="#bd1313")
define m =Character("Me", color="#1613bd")
define s =Character("Student", color="#cd6012")
define st =Character("Stranger", color="#28aadd")
define r =Character("Receptionist", color="#117428")
define f =Character("Mr. Charles", color="#a22d5f")
define mi =Character("Mina", color="#e63abe")
define am =Character("Amber", color="#620c5d")



label start:
   
    h "Oh (username) i liked how obedient you were ! You have now successfully completed your first task.Now, it's the time to announce you the second task !"
    h "Since you're intelligent, you'll understand that the level of this task will be higher than the previous one. I'm counting on you not to leave any trace behind if you want to stay safe."
    scene bg link
    menu:       
            "A link is shared."
            "What's this?":
                jump whats_this
            "Let's see":
                jump lets_see

label whats_this:
    h "Are you scared? Idiot.This link won't redirect you to another hacker, the problems that have fallen on your head are scary enough to fall into the same trap again, hahaha!"
    jump lets_see

label lets_see:
    "The link leads to the location of Saint Jack University in the neighboring city."
    h "We will play a game with the money you stole, what do you think?"
    h "A young beautiful girl will benefit from them."
    h "She's a petite girl, with green eyes, red-haired, and wears glasses. She's truly distinctive,the most beautiful girl in the university. You'll recognize her instantly."
    h 'You must convince this beautiful girl to accompany you. For a simple reason,you have to torture her so that she may suffer a little, but be careful not to kill her, she wasn\'t guilty.'
    h 'Then send to her family:"your daughter passed away", I would like to see her sad, all wounded face and the proof that her family believed her death.'
    h "I know you didn't understand. How to convince them that she is dead while she isn't? That's the game we're going to play with the stolen money!"
    menu:
        h "as for the large sum of money, you will give it to her so that she leaves the village and goes as far away as possible, never to return"
        "I got your point":
            jump got_point

label got_point:
    h "And be sure, she must never come back!"
    "Well, you see that things are getting worse and worse. What a sick hacker and what a crazier request! you still can't see what drives him to do this. Either he has scores to settle or he's insane, picking people to see them suffer."
    m "Let's recap his demands: to torture a college girl and make her family believe she's dead with proof of it, the money is for her to leave. He really insists she must not come back so they believe her death. Oh, he also said she wasn't guilty..."
    m "Then who is guilty?"

    "Next day...\n
    DAY -- OF ADVENTURE."
    menu:
        "It's time to head over there and embark on an adventure crazier than the first.You took your way to the university. Upon arrival, you found on your right, the university gate, on your left, a group of students who have already left. Where do you want to go?"
        "Right":
            jump right
        "Left":
            jump left

label right:
    menu:
        "You waited outside the university for a long time, not knowing what time she would come out. You caught sight of her from afar, you believe it's her. She started running towards a bus.What do you want to do?"
        "Chase after the bus":
            jump Chase
        "I prefer to ask students about her":
            jump left

label left:
    menu:
        "You just have to ask this group of students a few questions intelligently to gather some information about this girl."
        "Come up with a story so they won't suspect anything":
            jump story
        "Be honest and tell them that you need some information about her":
            jump honest

label Chase:
    "You begin to chase after this bus. It stops at the edge of the city, and the girl waits in a square. You think she's waiting for another bus or someone who is supposed to pick her up."
    "A very classy black car comes to pick her up, an elderly man wearing a white apron is driving, you think that he's her dad. She gets in, and takes a very bumpy road, it may be the road to the village."
    "After ten minutes, the car takes a small turn and parks right next to it. You continue on, trying not to look like you're following them. From a distance, you observe a very beautiful house."
    m "But who is that one !!!"
    'Suddenly, an elderly man stops right above me.'
    menu:
        st "Hey you, do you need something?"
        "Oh yes, yes. My mother sent me to the redheard's mother":
            jump Yes
        "Run away without giving any answer":
            jump run

label Yes:
    st "The mother of a redhead? I think you're mistaken! The redhead you're talking about has been living alone with her father in that villa across the street for years. I don't know who you're talking about."
    m "Ahhh sorry I must have made a mistake. Thank you !!"
    m "So, this girl's only family is her father! And he's likely a doctor."
    m "I believe I simply need to find out more about this man; his expertise might be beneficial to me!"
    "You go back home.."
    menu:
        "What are your plans for the next day?"
        "Go to the hospital to talk to her father":
            jump talk_right
        "Go to the hospital to inquire about her father":
            jump inquire_right   

label run:
    "You quickly start the car, truly afraid of leaving any trace of pursuit, and you head back home. "
    m "Hmm... The man i saw might be her father and he's a doctor."
    m "I believe I simply need to find out more about this man; his expertise might be beneficial to me!"
    menu:
        "What are your plans for the next day?"
        "Go to the hospital to talk to her father":
            jump talk_right
        "Go to the hospital to inquire about her father":
            jump inquire_right   


label story:
    m "Um, hey guys, hi. I'm looking for the prettiest girl around here. They told me to contact her."
    s"Yeah, I think the most beautiful girl, who everyone in the university thinks is the most beautiful, is Mina."
    m "Mina?"
    s "Yeah, that little redhead. If you want more info about her, she lives in the small village nearby. She's a medical student because her father, who is a forensic doctor, really wanted her to be a doctor like him, and she is a big fan of making short films she's popular here"
    m "And what time does she finish her classes?"
    s "She finishes everyday around 4:30 pm"
    m "Thank you for your help!"
    m "Hmm, Mina, a medical student, lives in the village nearby. Her father is a forensic doctor..."
    m "I believe I simply need to find out more about this man; his expertise might be beneficial to me!"
    "You go back home.."
    menu:
        "What do you want to do for the next day?"
        "Go to the hospital to talk to her father":
            jump talk_left
        "Go to the hospital to inquire about her father":
            jump inquire_left

label honest:
    m "Hey guys, do you know a little redhead around here?"
    s "Yes, why? What do you want from her?"
    "You tell them that you need to gather some information about her... \n Everyone looks at you strangely.."
    s "Mina, the forensic doctor's daughter, the big fan of making short films hahaha! She gets out at 4:30 PM, you can ask her directly."
    "You realize that you won't earn any information about her from them"
    m "Daamn! that wasn't the better choice"
    m "Hmm, so her name is Mina and her father is a forensic doctor."
    m "I believe I simply need to find out more about this man; his expertise might be beneficial to me!"
    "You go back home.."
    menu:
        "What are your plans for the next day?"
        "Go to the hospital to talk to her father":
            jump talk_left
        "Go to the hospital to inquire about her father":
            jump inquire_left

label inquire_left:
    "Next day..."
    "You're heading straight to the hospital of the neighboring city to inquire about the forensic doctor."
    r "How may i help you?"
    m "Ohh.. Hello, who is your forensic doctor here?"
    r "Mr Charles, our forensic doctor, who has extensive experience and is well-known in our city and even the neighboring towns due to the shortage of doctors, so he often travels."
    m "He's the father of the beautiful redhead, right!"
    r "Exactly, after losing his wife, his daughter is his only hope in life. She's everything in his eyes. Anyway, what do you need?"
    m "You mentioned that he travels a lot, so his work schedule is consistently busy?"
    r "Exactly, sometimes he's away from the hospital for several days to treat cases outside the city.He handles almost all the cases from several cities."
    r "Oh, there he is, going to his office. You can talk to him."
    "You turned around to see him, since he won't be available here for the next few days..."
    m "Thank you for your help i must go now i will come back another time."
    "You step out the hospital door with your heart pounding and begin to connect the dots"
    m "Charles, our forensic doctor, is popular in his city and the neighboring towns because of the shortage of doctors requiring him to travel. Consequently, Mina is left alone for days since he's all she has."
    m "Could this information help me? If Mina is not guilty, could her father be involved? If yes, what's the connection between our forensic doctor and our insane hacker? He wants to target his daughter because she's all he has left, and he absolutely wants him to believe she's dead and never return."
    m " I'm losing my mind; I don't think I'll be able to gather more information on them. It's time to tackle something else."
    m "Mr. Charles won't be available tomorrow, so I think I'll be able to work peacefully."
    menu:
        "So, how would you go about completing this task ?"
        "Invent a story to make the hacker believe that I've executed his requests":
            jump Invent
        "Execute what I've been asked to do from the hacker, there is no risk for me":
            jump execute

label inquire_right:
    "Next day..."
    "You're heading straight to the hospital of the neighboring city to inquire about Mina's father"
    r "How may i help you?"
    m "Ohh.. Hello, i'm looking for the redhead's father,he's a doctor here"
    r "Ahh you mean Mr Charles, our forensic doctor, who has extensive experience and is well-known in our city and even the neighboring towns due to the shortage of doctors, so he often travels."
    r "Exactly, he's the father of the popular redhead, after losing his wife, his daughter is his only hope in life. She's everything in his eyes. Anyway, what do you need?"
    m "You mentioned that he travels a lot, so his work schedule is consistently busy?"
    r "Exactly, sometimes he's away from the hospital for several days to treat cases outside the city.He handles almost all the cases from several cities."
    r "Oh, there he is, going to his office. You can talk to him."
    "You turned around to see him, since he won't be available here for the next few days..."
    m "Thank you for your help i must go now i will come back another time."
    "You step out the hospital door with your heart pounding and begin to connect the dots"
    m "Charles, our forensic doctor, is popular in his city and the neighboring towns because of the shortage of doctors requiring him to travel. Consequently, Mina is left alone for days since he's all she has."
    m "Could this information help me? If Mina is not guilty, could her father be involved? If yes, what's the connection between our forensic doctor and our insane hacker? He wants to target his daughter because she's all he has left, and he absolutely wants him to believe she's dead and never return."
    m " I'm losing my mind; I don't think I'll be able to gather more information on them. It's time to tackle something else."
    m "Mr. Charles won't be available tomorrow, so I think I'll be able to work peacefully."
    menu:
        "So, how would you go about completing this task ?"
        "Invent a story to make the hacker believe that I've executed his requests":
            jump Invent
        "Execute what I've been asked to do from the hacker, there is no risk for me":
            jump execute


label talk_left: 
    "Next day..."
    "You're heading straight to the hospital of the neighboring city to inquire about the forensic doctor."
    r "How may i help you?"
    m "Ohh.. Hello, who is your forensic doctor here?"
    r "Mr Charles, our forensic doctor, who has extensive experience and is well-known in our city and even the neighboring towns due to the shortage of doctors, so he often travels."
    m "He's the father of the beautiful redhead, right!"
    r "Exactly, after losing his wife, his daughter is his only hope in life. She's everything in his eyes. Anyway, what do you need?"
    m "I need to talk to him please"
    r "Of course, you'll find his office on the first floor, first door on the left."
    "You make your way up the stairs, feeling the adrenaline coursing through you as you rehearse your words. Standing before his office door, you tap gently, and it swings open to reveal him, inviting you in with a warm smile."
    f "How can i assist you?"
    "Disturbed, you try to invent a story to interact with him"
    "In reality, I have a relative who passed away yesterday in the neighboring town, and they still haven't found a forensic doctor to handle his case. I heard about you, so I didn't hesitate to come here and ask for your help."
    f "I see. Who was the doctor who was handling his case before his passing?"
    m "I don't have any idea"
    f "one second please.."
    "He picked up his phone and stats a call."
    f "Heyy man, umm i have a quick question, did u work yesterday? no? Alright I thought you might have forgotten to inform me."
    'He hung up, and suddenly the office became quiet. He wrote something on a piece of paper and handed it to you: "Here, this forensic doctor can help you; he\'s very competent."'
    "You find this behavior very peculiar, yet you calmly exit the office."
    m "But who was that on the phone? Surely, he isa doctor and he works only with him"
    "You step out the hospital door with your heart pounding and begin to connect the dots"
    m "Charles, our forensic doctor, is popular in his city and the neighboring towns because of the shortage of doctors requiring him to travel. Consequently, Mina is left alone for days since he's all she has, he works with one and only doctor"
    m "Could this information help me? Why he works with one and only doctor? And if Mina is not guilty, could her father be involved? If yes, what's the connection between our forensic doctor and our insane hacker? He wants to target his daughter because she's all he has left, and he absolutely wants him to believe she's dead and never return."
    m " I'm losing my mind; I don't think I'll be able to gather more information on them. It's time to tackle something else."
    menu:
        "So, how would you go about completing this task ?"
        "Invent a story to make the hacker believe that I've executed his requests":
            jump Invent
        "Execute what I've been asked to do from the hacker, there is no risk for me":
            jump execute
        
label talk_right:
    "Next day..."
    "You're heading straight to the hospital of the neighboring city to inquire about Mina's father"
    r "How may i help you?"
    m "Ohh.. Hello, i'm looking for the redhead's father,he's a doctor here"
    r "Ahh you mean Mr Charles, our forensic doctor, who has extensive experience and is well-known in our city and even the neighboring towns due to the shortage of doctors, so he often travels."
    r "Exactly, he's the father of the popular redhead, after losing his wife, his daughter is his only hope in life. She's everything in his eyes. Anyway, what do you need?"
    m "I need to talk to him please"
    r "Of course, you'll find his office on the first floor, first door on the left."
    "You make your way up the stairs, feeling the adrenaline coursing through you as you rehearse your words. Standing before his office door, you tap gently, and it swings open to reveal him, inviting you in with a warm smile."
    f "How can i assist you?"
    "Disturbed, you try to invent a story to interact with him"
    "In reality, I have a relative who passed away yesterday in the neighboring town, and they still haven't found a forensic doctor to handle his case. I heard about you, so I didn't hesitate to come here and ask for your help."
    f "I see. Who was the doctor who was handling his case before his passing?"
    m "I don't have any idea"
    f "one second please.."
    "He picked up his phone and stats a call."
    f "Heyy man, umm i have a quick question, did u work yesterday? no? Alright I thought you might have forgotten to inform me."
    'He hung up, and suddenly the office became quiet. He wrote something on a piece of paper and handed it to you: "Here, this forensic doctor can help you; he\'s very competent."'
    "You find this behavior very peculiar, yet you calmly exit the office."
    m "But who was that on the phone? Surely, he isa doctor and he works only with him"
    "You step out the hospital door with your heart pounding and begin to connect the dots"
    m "Charles, our forensic doctor, is popular in his city and the neighboring towns because of the shortage of doctors requiring him to travel. Consequently, Mina is left alone for days since he's all she has, he works with one and only doctor"
    m "Could this information help me? Why he works with one and only doctor? And if Mina is not guilty, could her father be involved? If yes, what's the connection between our forensic doctor and our insane hacker? He wants to target his daughter because she's all he has left, and he absolutely wants him to believe she's dead and never return."
    m " I'm losing my mind; I don't think I'll be able to gather more information on them. It's time to tackle something else."
    menu:
        "So, how would you go about completing this task ?"
        "Invent a story to make the hacker believe that I've executed his requests":
            jump Invent
        "Execute what I've been asked to do from the hacker, there is no risk for me":
            jump execute
      
label execute:
    m "I come back the next day to wait for her to kidnap her. I don't give a damn about this story."
    "You return home and think about where to hide her to torture her..."
    m" She must not recognize me, and besides, I'll lose money... Well, losing a little money now is better than staying terrified like this.."
    'You go to the kitchen to grab a knife to scare her and convince her to go, otherwise u think that your threats will be enough...'
    "The day after..."
    menu:
        "You park in front of the university and wait. She just came out. What will you do?"
        "Tell her that your father sent me to take you back":
            jump yrfather_sentme
        "Violently kidnap her":
            jump kidnap

    label yrfather_sentme:
        m "Hey Mina, your dad sent me to take you back home to the village."
        mi "Oh really?... "
        m "Yeah, I'm a hospital agent, and he told me he'll be late today take her instead of me."
        mi "Oh, I'm not quite sure. My father has never done anything like this; I should ask him."
        "You must intervene to prevent her actions, and to do so, your only option is to kidnap her."
        jump kidnap

label kidnap:
        "you grab her violently, she starts screaming, people start looking at you, and you quickly flee by taking her in the car."
        "You stop at an isolated place, smash her phone, throwing the sum of money at her face and start screaming on her"
        m "I've already helped you a lot with this money, so you'd better listen to me."
        mi "What's wrong with you !!"
        m "Look, I won't talk too much... You'll take this sum of money and leave this country now. I don't want any trace of you here, your father must believe that from now you're considered DEAD!"
        mi "Who do you think you are! I'm not afraid from you! Take your money back and let me go peacefully"
        m "Well, she is a hard-headed person, talking to her won't work."
        "you start hitting her in the face, and pulled out the knife to make her even more afraid."
        mi "Okay, okay, I'll do whatever you want, just stop please!"
        m "If you go back, believe me you'll find your father dead in the middle of your village."
        m "Hey pretty girl, smile for the camera !!"
        "you take her to another city and throw her there, shouting"
        m "Figure it out!"
        'You go back to her village to leave a note at the door of the house: "Your daughter has left life forever, searching for her won\'t do you any good."'
        "You return home.."
        'Arriving home, you open your PC and find a news circulating on social media: "Mina, the only daughter of Dr. Charles, passed away mysteriously". Suddenly, your screen goes black, and the hacker\'s voice returns...'
        h "Well dooone! you've done an excellent job.Now all that's left is for me to give you your last mission."
        m "Ohhhh god I narrowly escaped..."
        "Suddenly, you hear the sound of police surrounding your house."
        m "Ohh daaaaaamnn!!"
        "The university gate cameras captured everything, you've been located by the police."
        "GAME OVER!"
        "It was dumb to make that choice, wasn't it?"
        "You didn't go to prison for the money you stole, but you'll go for a bad choice, poor (username), you make bad decisions to save your life"
        h "Well, our poor (username) couldn't survive."
        h "No matter, I'll just find another victim, hahahaha."
        return
    
label Invent:
    "You enter a coffee and start contemplating how to take that girl with you satisfied, so her father won't search for her."
    m "Anyway, there's not much time left for the 7 days to pass, so I think it's doable to hide her from the world for a few days."
    "You remember you have a group of friends who enjoy making short films for social media"
    m "Perhaps she'll be interested in this request, especially if we can convince her. I don't think she'll refuse that. And if she does, she'll never turn down that large sum of money."
    "You call up the group leader"
    m "Hey Amber, how about a pretty red-headed girl for acting in a crime,medical short film?"
    am "Of course, but where did you find such a beauty?"
    m "Come along and bring the whole group in front of Saint Jack University tomorrow."
    "Next day..."
    "You explained your situation to them and that you need to take her for a few days."
    "Mina exits the university gate, and Amber heads straight toward her to talk her."
    am "Hey, you're truly beautiful! Would you like to be part of a crime short film with my team? They're over there, you won't regret it. And, of course, you'll be paid for your work. What do you think?"
    " Dazzled by the offer, she accepts immediately and comes with you."
    mi "That's all what i love!"
    mi "But how long will this job take?"
    m "Just a few days, it suits you, right?"
    mi "Yes yes, it's just that I need to inform my father"
    m "Oh, yes, you'd better inform him"
    "Amber start explaining to Mina"
    am "This is the studio where we work. Welcome aboard, you're going to love working with us."
    am "And this room right next door becomes yours."
    "Few moments later,you started the work. Amber applies terrifying makeup on Mina's face. They begin filming crime scenes, where the actor committing the crimes is you."
    "Mission accomplished !"
    "You get permission from the group to leave, since your role is finished"
    "To make the game seem real, you sent a large group of friends to Mr. Charles' house. "
    m "This will make the insane hacker believe that something is amiss there. I know he's watching everything."
    "You go back home and open your computer. You place on your computer desk the video of the torture scene of Mina and you wait for the insane hacker to arrive."
    h "Well our lovely Mina didn't return home, poor Charles.. All the village is sad with him.."
    h "Good job, my brave ex-military. See you for your last task, and then freedom to all !"

    return
