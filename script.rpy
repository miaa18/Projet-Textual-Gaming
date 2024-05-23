
    #this starts the game 
    #intro
    #chapter1
    #chapter2
    #chapter3
    #end

#HERE WE DEFINE THE CHARACTERS

define user=Character("[username]",color="#fb8f8f")

define h =Character("Unknown", color="E9BBBB")
define s =Character("Student", color="E9BBBB")
define st =Character("Stranger", color="E9BBBB")
define r =Character("Nurse", color="E9BBBB")
define f =Character("Mr. Charles", color="E9BBBB")
define mi =Character("Mina", color="E9BBBB")
define am =Character("Amber", color="E9BBBB")
define p =Character("The police officer", color="#3359FF")
define man=Character("The man", color="#4a290a")
define S = Character("Sue",color="#00867f")
define K = Character("Krysa",color="E9BBBB")
define E=Character("Elliot", color="#E9BBBB")
define m=Character("Mark", color="#E9BBBB")

define in_eye = ImageDissolve("eye.png", 0.8)
define out_eye = ImageDissolve("eye.png", 2.0, reverse=True)


#GLITSH EFFECT

image glitshed:
    At("bg eyes", glitch)
    pause 0.2
    At("bg eyes", glitch)
    pause 0.1
    At("bg eyes", glitch)
    pause 0.
    repeat


image glitshed2:
    At("bg eyes2", glitch)
    pause 0.2
    At("bg eyes2", glitch)
    pause 0.1
    At("bg eyes2", glitch)
    pause 0.3
    repeat


image glitshed3:
    At("bg mail2", glitch)
    pause 0.2
    At("bg mail2", glitch)
    pause 0.1
    At("bg mail2", glitch)
    pause 0.3
    repeat

image ended:
    At("bg end", glitch)
    pause 0.2
    At("bg end", glitch)
    pause 0.1
    At("bg end", glitch)
    pause 0.3
    repeat

image glitshed4:
    At("bg ready", glitch)
    pause 0.2
    At("bg ready", glitch)
    pause 0.1
    At("bg ready", glitch)
    pause 0.3
    repeat


image glitshed5:
    At("bg countdown", glitch)
    pause 0.2
    At("bg countdown", glitch)
    pause 0.1
    At("bg countdown", glitch)
    pause 0.3
    repeat


image glitshed6:
    At("bg task1", glitch)
    pause 0.2
    At("bg task1", glitch)
    pause 0.1
    At("bg task1", glitch)
    pause 0.3
    repeat


image glitshed7:
    At("bg task2", glitch)
    pause 0.2
    At("bg task2", glitch)
    pause 0.1
    At("bg task2", glitch)
    pause 0.3
    repeat


image glitshed8:
    At("bg task3", glitch)
    pause 0.2
    At("bg task3", glitch)
    pause 0.1
    At("bg task3", glitch)
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
    stop music 
    play music "gamesound.mp3" loop fadein 1.0
    scene black with dissolve
    pause 1.0
    #$ renpy.movie_cutscene("kidnapscene",delay=5,loops=0,stop_music=True)
    scene black with dissolve
    pause 1.0
    scene bg intro with dissolve
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
        scene black with dissolve
        centered "{cps=25}Welcome, dear [username] ! {/cps}"
        centered" {cps=25}May the clarity of your mind guide your steps \n for your choices design your life..{/cps}"
    
    window hide
    scene black with dissolve
    play sound "intro.mp3"
    pause 0.5
    
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
    stop sound
    play sound "menu.mp3"
    scene bg depressed with dissolve
    pause 5.0
    scene black with dissolve
    pause 1.5
    scene bg trust with dissolve
    pause 4.0
    scene black with dissolve
    pause 3.0
    stop sound
    pause 1.5
    

    #INTRODUCTION
    scene black with dissolve
    scene bg town with dissolve

    "DATE: May 4th, 2024 \nLOCATION: Chicago, USA"
    scene black with dissolve
    pause 1.0
    scene bg car_from_the_drivers_view_the_wheel with dissolve
    "You're heading home from work after a long day"
    scene black with dissolve
    pause 1.0
    scene bg desktop with dissolve
    "as usual, you unwind at your PC, scrolling through social media, checking out what's new."
    "You also take a moment to check your emails.."
    "While you're sifting through your emails, one caught your eyes.."
    scene bg mail with dissolve
    pause 7.0
    scene black with dissolve
    pause 0.5
    scene bg mail2 with dissolve
    "It appeared innocent enough, showcasing the profile photo of an old comrade from your military days"
    "reaching out to catch up and sharing their social media link"
    "Nostalgia swept over you, and without a second thought"
    "You clicked on the link.."
    scene black with dissolve
    pause 0.5
    scene glitshed3 with dissolve
    "However, instead of redirecting you to a familiar social media page"
    "your screen flickered..."
    scene black with dissolve
    pause 1.0
    "an app began downloading automatically..."
    "Cursing under your breath, you realized you had been HACKED !"
    scene black with dissolve
    pause 0.5
    scene glitshed with dissolve
    h "Well, well, well, what do we have here?"
    h  "Seems our ex-military friend has stumbled into quite the situation!"
    h "You are sitting on 200 mil stolen cash in your bank accounts."
    "This wasn't just a random attack.. The hacker knew about your past"
    scene black with dissolve
    pause 1.0
    scene glitshed
    user "How did you find these files?"
    h "Oh, let's just say I have my ways. The important thing is that they're in my possession now."
    user "Who are you, and what do you want from me?"
    h "come on now, no need for introductions"
    h "Let's just say I'm someone who likes a good game."
    scene black with dissolve
    pause 0.5
    scene bg son with dissolve
    pause 3.0
    scene black with dissolve
    pause 0.5
    scene glitshed with dissolve
    h "This is your son right?"
    user "Samy my son !"
    h "You'll want him to stay safe, won't you?"
    h "How about a little deal? I'll send over a list of Tasks for you to take out, just for kicks."
    h "If you nail them, your shady past will be our little secret"
    user "But why? What's the point of all this?"
    h "Ah, where's the fun in explaining?"
    h "Let's just say it is a little experiment of mine."
    h "And oh, by the way, you've got a week to play along. Your countdown starts tomorrow at 7:00 AM sharp!"
    scene black with dissolve
    pause 0.5
    # play music discrepancy_preview loop 
    scene bg desktop with dissolve
    "After enduring the most harrowing nightmare of your life, your computer screen returns to its usual state."
    scene bg myroom with dissolve
    user "I've put my life and my family's in danger because of my carelessness."
    scene black with dissolve
    pause 1.5

    scene glitshed4 with dissolve
    pause 2.0
    scene glitshed4 with dissolve
    pause 2.0
    scene glitshed4 with dissolve
    pause 2.0

    scene black with dissolve
    pause 2.0
    scene black with dissolve
    menu:
        "YES !":
            jump ready
        "No i'm not ready !":
            jump notready

    label ready:
        scene black with dissolve
        pause 2.0
        centered"Your role in this game \n is to find a way to escape safely and uncover the hacker's identity."
        centered"Be careful \n not to leave any trace of malicious activity behind."
        centered"And remember,\n both you and your family are in danger!"
        scene black with dissolve
        jump game

    label notready:
        centered"You're the only one losing here."
        return

label game:
    scene black with dissolve
    scene bg desktop with dissolve
    user "What the hell happened... I never believed this was real."
    menu:    
        "What prudent action will you take next?"
        "Go to the police":
            jump choice1_police
        "Wait for the countdown to start tomorrow at 7:00 pm":
            jump choice2_lawyer



#POLICE (CERINE & SABRINE)

label choice1_police:
    scene black with dissolve
    pause 1.0
    scene bg looking_phone with dissolve
    pause 0.01
    'You\'re inside your car. On you\'re way to the police station, you receive a text message on your phone from an unknown number.' 
    'The message warns: "\'If you set foot in the police station, I\'ll provide them with evidence of the illegal money transfers\".'
    menu:
        'What course of action do you take next?'
        "Ignore the text and keep going":
            jump PoliceStation
        "Text them back":
            jump TextThemBack
        "Take a step back and instead wait for the countdown to start tommorow at 7:00 pm":
            jump choice2_lawyer


label TextThemBack:
    'You stop in the middle of the street, more furious than ever, you enter the chat on your phone with the unknown sender. '
    menu:
        "What message do you type?"
        "You prick ! i\'m not scared of you":
            jump UnavailableSender

        "How do you know where i am??? Are you following me?!":
            jump LookingAround

label UnavailableSender:
    "Your phone alerts you that your text message cannot be sent because the intended recipient does not exist. "
    menu:
        "What would you like to do next?"
        "Take  a setp back and go back home and wait": 
            jump choice2_lawyer
        "Proceed on your way to the police" :
            jump PoliceStation

label LookingAround:
    scene black with dissolve
    scene bg choice_escape1 with dissolve
    pause 0.01
    "You exit your car slamming the door shut and begin to spin around in paranoid circles, scanning for any distant figures that might be observing you."
    menu:
        "Where do you wanna look?"
        "Left":
            jump Left
        "Right":
            jump Right
        'Behind':
            jump Behind1
label Left:
    scene bg street_with_a_few_people_looking_and_a_few_looking with dissolve
    pause 0.01 
    'To the left, the street is hive of activity, with buildings lining either side'
    "their facades varying from sleek modern designs to weathered brick structures."
    'The bustling street is like a lively symphony of motion  with cars, buses and bicycles'
    "weaving through the traffic as pedestrians navigate the sidewalks."
    menu:
        "Nothing seems suspicious."
        'Look in the other directions' :
            jump Directions 
label Right:
    scene bg small_nice_town_houses_aligned with dissolve
    pause 0.01 
    'To your right, you find a gently winding cobblestone path, leading up to a tranquil hillside town.'
    'The path is hugged by vibrant green bushes and the occasional splash of wildflowers that sway gently in the breeze.'
    'Ahead, the town emerges with a warm and inviting aura.'
    'The houses, painted in soft pastels, boast sun-kissed, terra cotta roofs and weathered wooden doors'
    'suggesting years of stories and history within their walls'
    menu:
        'No other choice'
        'Look in the other directions':
            jump Directions 
label Behind1:
    scene black with dissolve
    scene bg black_car_behind with dissolve
    pause 0.2 
    'Behind you, a sleek black car guided by a man appearing to be in his thirties. The pathway is cocooned between two majestic lines of trees.'
    'On either side of the road stand townhouses, each their gardens.' 
    menu:
        "What will you do ?"
        'Look in the other directions':
            jump Directions
        'Go have a talk with the man in the car,he seems suspicious':
            jump TalkingWithCarGuy

label Directions:
    scene bg choice_escape1 with dissolve
    pause 0.01 
    menu:
        'Left':
            jump Left
        'Right':
            jump Right
        'Behind':  
            jump Behind1

label TalkingWithCarGuy:
    scene black with dissolve
    scene bg talking_with_car_guy with dissolve
    pause 0.01 
    'As you approach the car, the man inside rolls down his window.'
    menu:
        "What message do you intend to convey to him?"
        'Are you following me ???':
            jump Question

label Question:
    'The man in the car gazes at you, a confused expression crossing his face'
    man'Following you? I don\'t even know you, man!'
    menu:
        'What will you respond?'
        "Excuse me sir,  i'm just being paranoid !":
            jump BackToCar
        "Stop lying you ugly rat!":
            jump badgeReveal

label badgeReveal:
    scene bg badge_reveal with dissolve
    pause 0.01 
    'The man angrily exits his car, slamming the door shut, and abruptly thrusts a small badge in your face.'
    'To your surprise, it\'s a police officer badge!'
    'He then begins questioning you about your identity.'
    menu:
        "So you will.."
        'Respond to his questions':
            jump Questions
        'Try to escape':
            jump Escaping
label Questions:
    'You choose to respond to the police officer\'s questions.'
    menu:
        " What is your answer?"
        "Officer, I apologize if I\'ve caused any trouble, i thought you were someone else. My name is [username] and i live nearby":
            jump FreeToGo

label FreeToGo:
    scene bg free_to_go with dissolve
    pause 0.01 
    'The police officer gives you a serious warning about unfounded accusations in the future.'
    man 'I noted your name and i will conduct a brief investigation to ensure you\'re not involved in any suspicious activity.'
    menu:
        'Thank him and get back to your car':
            jump BackToCar

label Escaping:
    scene black with dissolve
    scene bg direction with dissolve
    pause 0.01 
    'As you contemplate the best direction to evade the police man'
    menu:
        "Which path do you ultimately choose to take?"
        'Go left':
            jump choiceEscape1
        'Go right': 
            jump choiceEscape2
        'Look around before runing':
            jump Directions1

label choiceEscape1:
    scene bg escape_choice1 with dissolve
    pause 0.01 
    'Choosing to evade the police, you turn left into the bustling city streets, dodging between cars and buses.'
    "The scent of exhaust mixes with the aroma of street food as you disappear into the crowd."
    play sound "police.mp3"
    'Suddenly, after just five minutes of running, the loud wail of police sirens reaches your ears!'
    scene black with dissolve
    scene bg street_with_a_few_people_looking_and_a_few_looking with dissolve
    pause 0.01 
    'Panic sets in as you realize the authorities are closing in.'
    'Desperation drives you to move faster'
    'but in your haste, you collide with pedestrians with every step you take adding to the chaos while drawing more attention to yourself.'
    stop sound
    menu:
        'What is you next move?'
        'Keep running':
            jump KeepRuning 
        'Avoid the public by running towards a secluded rural area':
            jump TheRural

label KeepRuning:
    scene bg keep_running with dissolve
    pause 0.01 
    play sound "police.mp3"
    'As you continue running, a police vehicle approaches from one direction, while another closes in from behind.'
    'The officers step out of their cars shouting:"Stay still, don\'t move!\" \"Put your hands up!!.\".'
    'There seems to be no escape now.'
    stop sound
    menu:
        "What do you wanna do ?" 
        'Keep Trying':
            jump KeepTrying 
        'Give up':
            jump GiveUp
label KeepTrying:
    scene bg keep_trying with dissolve
    pause 0.01 
    'You are surounded and guns are directed at you.'
    menu: 
        "Where do you choose to escape this police Besieged?"
        'You rush into the building to your left':
            jump ArtGallery
        'Run backwords':
            jump RunBack
label ArtGallery:
    scene black with dissolve
    pause 1.0
    scene bg art_gallery with dissolve
    pause 0.01 
    'As you desperately seek refuge, you spot an open door to a nearby building and rush inside.'
    'The dimly lit interior reveals white walls adorned with strange paintings and sculptures, hinting that you\'ve stumbled into an art gallery.'
    scene black with vpunch
    'Before you can take another step, a searing pain shoots through your knee, sending you crashing to the ground.'
    pause 1.0
    scene bg art_gallery with dissolve
    pause 0.5
    play sound "police.mp3"
    'The echo of a gunshot fills the hallway, and you realize with horror that you\'ve been hit.'
    'Darkness envelops you as the harsh reality sinks in: your escape attempt has ended in tragedy.' 
    scene black with dissolve 
    pause 1.0
    stop sound
    jump end
label RunBack:
    scene black with dissolve
    pause 1.0
    scene bg street_people_walk_and_police with dissolve
    pause 0.01 
    play sound "police.mp3"
    'As you frantically run backward, hoping to evade the pursuing officers'
    'You unexpectedly stumble upon a group of additional police officers blocking your path.'
    'Before you can react, one of the officers swiftly grabs your hands, wrenching you off balance and causing you to fall to the ground.'
    'The world spins around you and with one final gasp, you succumb to unconsciousness, the events of the chase fading into oblivion..'
    stop sound
    scene black with dissolve
    pause 1.0
    jump end    



label Directions1:
    scene black with dissolve
    scene bg directions with dissolve
    pause 0.01 
    menu : 
        'Left':
            jump Left1 
        'Right':
            jump Right1

label Left1: 
    scene black with dissolve    
    scene bg street_with_people_walking with dissolve
    pause 0.01 
    'To the left, the street is hive of activity, with buildings lining either side'
    'their facades varying from sleek modern designs to weathered brick structures.'
    'The bustling street is like a lively symphony of motion  with cars, buses, and bicycles'
    'weaving through the traffic as pedestrians navigate the sidewalks. '
    menu:
        'So..'
        'choose to run Left':
            jump choiceEscape1
label Right1:
    scene black with dissolve
    scene bg a_gently_winding_cobblestone_path with dissolve
    pause 0.01 
    'To your right, you find a gently winding cobblestone path, leading up to a tranquil hillside town.'
    'The path is hugged by vibrant green bushes and the occasional splash of wildflowers that sway gently in the breeze.'
    'Ahead, the town emerges with a warm and inviting aura.'
    'The houses, painted in soft pastels, boast sun-kissed, terra cotta roofs and weathered wooden doors'
    'suggesting years of stories and history within their walls'
    menu:
        'So..'
        'choose to run Right' :
            jump choiceEscape2

label BackToCar:
    scene black with dissolve
    scene bg car_from_the_drivers_view_the_wheel with dissolve
    pause 0.01 
    'You compose yourself and get into your car, slamming the door shut.'
    'You pause for a moment before starting the engine, pondering who the hacker could be? and how does he know your location?'
    'You wonder whether you should continue to the police station or wait to see what unfolds tomorrow.'
    menu:
        "What do you think you should do next?"
        'Go to the police station and tell them everything':
            jump PoliceStation
        'Go back home and wait for what tommorow holds':
            jump choice2_lawyer 

label TheRural:
    scene black with dissolve
    pause 1.0
    scene bg the_rural with dissolve
    pause 0.01 
    'You step into the narrow passage between two buildings.'
    'where you find close to you a door that serves as the back entrance to a nearby restaurants.'
    'Trash cans overflow, filling the air with a strong smell.'
    'The alley is dimly lit, with graffiti on the walls and in the distance, a rat runs quickly from one side to the other.'
    menu: 
        'What do you want to do next?'
        'Continue running straight until you reach the end of the alley':
            jump Deadend
        'Hide inside a trash can':
            jump TrashCan
label Deadend:
    scene black with dissolve
    scene bg high_wall with dissolve
    pause 0.01 
    'You keep running with all your energy and than you see a high wall between the two building its the end of the rural it\'s deadend '
    menu :
        'What do you do next?'
        'Look for a Way to Climb Over':
            jump ClimbOver
        'Search for Hidden Exits':
            jump Exit
        
label ClimbOver:
    'You decide to climb the wall. you drag the heavy dumpster into position against the wall, creating a makeshift stepping platform. '
    'You step onto the dumpster, testing its stability. It holds firm under your weight.'
    'Reaching up, you grab a thick vine of ivy and pull yourself up, finding footholds in the uneven brickwork.'
    menu:
        'Hurry Up the Climb':
            jump HurryUpTheClimb
label HurryUpTheClimb:
    'As you scrambled to climb quickly, your foot slipped causing you to lose your balance and tumble to the ground.'
    'The pursuing policeman swiftly closed in, training his gun on you, his voice commanding you not to move!'
    jump GiveUp
label Exit:
    scene black with dissolve
    pause 1.0
    scene bg exitdoor with dissolve
    pause 0.01 
    'You frantically tried to open the doors on both sides'
    scene black with dissolve
    scene bg keep_trying with dissolve
    pause 0.01 
    'Suddenly, the policeman who had been chasing you caught up ans pointed his gun ordering you not to move!'
    jump GiveUp 

label TrashCan:
    scene bg trashcan with dissolve
    pause 0.01 
    'You open the trash cam the smell is atrocious there\'s rotten tomatos baby dapers some brown liquide and a lot of trash bags.'
    'You get inside and you close it'
    'From far you hear police man yelling and talking to each other but their words are not understanble'
    'You patiently waited for the policemen to pass by.'
    'Once their voices faded into the distance, you decided to return home and await the countdown'
    'prepared to comply with the hacker\'s demands.. '
    jump choice2_lawyer

 
    
label choiceEscape2:
    scene black with dissolve
    pause 1.0
    scene bg nearbyhouse with dissolve
    pause 0.01 
    'After hastily finding refuge beside a nearby house, you patiently waited for the policemen to pass by.'
    'Once their voices faded into the distance, you decide to return home and await the countdown'
    'prepared to comply with the hacker\'s demands.. '
    scene black with dissolve

    jump choice2_lawyer


label PoliceStation:
    scene black with dissolve
    pause 1.0
    scene bg twopolices with dissolve
    pause 0.01 
    'You\'ve just stepped into the police station.'
    'To your right, two officers are chatting casually, one of them is holding a cup of steaming coffee.'
    'Ahead of you, a man in a suit briskly walks from the right to the left side of the station. He then ascends the stairs and disappears from view'
    scene black with dissolve
    scene bg lady_sitting_at_her_desk_police with dissolve
    pause 0.01 
    'You walk straight to a lady sitting at her desk, she appears to be conversing on the phone.'
    'You attempt to speak to her but she gestures with her hand indicating for you to wait. "One moment, sir," she mouths, focusing on her call.'  
    menu:
        'Where are you waiting untill she finishes?' 
        'You take a seat on a nearby chair, positioned conveniently by the staircase':
            jump Sitting  
        'You stand near to the exit door and wait'  :
            jump Standing 

label Sitting:
    scene bg nearby_police with dissolve
    pause 0.01
    'You sit on hard plastic chair, trying to blend into the background. The lady hangs up and makes a discreet hand signal to a nearby officer'
    'You watch, your pulse quickening, as they engage in a brief, hushed conversation, occasionally glancing at a computer screen and then back at you'
    scene bg police_walking with dissolve
    pause 0.01 
    'The air feels thick as the officer ends the conversation and starts walking towards you with deliberate steps'
    'While reaching into his back pocket which appears to contain handcuffs, he says'
    p'Hey buddy,  just stay right where you are. I have a few questions for you.'
    menu:
        'What are you doing next?'
        'Stay still':
            jump StayStill
        'Run up the staircases':
            jump Staircases
        'Run to the entry door of the police station where the othe officer is standing':
            jump dashDoor

label StayStill:
    scene black with dissolve
    scene bg policetalk with dissolve
    pause 0.01 
    'You straighten your jacket and sit up tall, maintaining a composed and confident demeanor. You look in the officer\'s eyes, ready to respond to him'
    menu:

        'What do you say to the officer?'
        'Let him ask you the questions without saying anything' :
            jump nothing 
        'Hi sir and tell him why you came here in the fisrt place':   
            jump HiSir
        'Ask him if you are in trouble' :
            jump nothing 

label nothing:
    'He expertly secures the handcuffs around your wrists. While he does this, he begins to question you.'
    'It\'s clear from his pointed questions that he already knows far more about you than you expected.'
    'After confirming your identity, he recites  with a practiced clarity.'
    p 'You have the right to remain silent. Anything you say can and will be used against you in a court of law.'
    'You have the right to consult with a lawyer and have that lawyer present during any questioning.'
    'His voice, steady and authoritative, leaves no room for doubt or negotiation as you process the gravity of the situation.'            
    menu:
        'Why am i being arrested ?':
            jump WhyArrested 
label WhyArrested:
    'He informs you gravely that you have been implicated in an illegal money transfer originating from a military base.'
    'He explains that the station has recently received compelling evidence that links you to the crime.'
    'His voice is stern and the look in his eyes serious as he details the steps that will follow.'
    p'You will be detained at the station, held in custody until a thorough investigation can unravel the truth behind these accusations'
    scene black with dissolve
    scene bg interrogation_room with dissolve
    pause 0.01  
    'You find yourself confined within the stark walls of the interrogation room, the gravity of your situation becoming painfully clear.'
    'With nowhere to escape, you realize you\'ve been caught..'
    'the hacker has not only invaded your life but has exposed your deepest secret, turning your world upside down' 
    scene black with dissolve
    pause 1.0     
    jump end 

label HiSir:
    'You tell him all about the hacker and the messages he sent you'
    p'So, you\'re saying you received this threat'
    menu:
        p 'but you\'ve done nothing illegal to warrant this kind of blackmail?'
        "Exactly":
            jump arrested
        "Tell him the truth and accept your fate":
            jump arrested
label arrested:
    p ' Stand up '
    'As you rise, he expertly secures the handcuffs around your wrists. While he does this, he begins to question you'
    'It\'s clear from his pointed questions that he already knows far more about you than you expected.'
    'After confirming your identity, he recites  with a practiced clarity.'
    p 'You have the right to remain silent. Anything you say can and will be used against you in a court of law.'
    p 'You have the right to consult with a lawyer and have that lawyer present during any questioning.'
    'His voice, steady and authoritative, leaves no room for doubt or negotiation as you process the gravity of the situation.' 
    p 'You will be detained at the station, held in custody until a thorough investigation can unravel the truth behind these accusations'
    jump Continue4  

label Staircases: 
    scene black with dissolve
    scene bg doors_on_each_side with dissolve
    pause 0.01 
    'You are now on the second floor of the station, surrounded by various doors, each leading to a different room.' 
    menu:
        'Which door will you choose?'
        "Conference Room":
            jump Conference
        "Go up another flight of stairs to the roof":
            jump roof
        "Records Room":
            jump Record
label Record:
    scene bg room_where_towering_shelves with dissolve
    pause 0.01 
    'In this room you find yourself surrounded by towering shelves filled with files and various documents.'
    'The room is dimly lit and seems rarely visited, giving you a sense of solitude. '
    menu:
        'What are you doing next?'
        'Secure the door':
            jump securedoor
        'Look for another exit':
            jump exitFound
label securedoor:
    menu:
        'What are you using to secure the door?'
        'An old chair sitting in the corner':
            jump chair
        'Use a shelf that is sparsely filled':
            jump shelf
label exitFound:
    'To your surprise, you discover a hidden door at the far end of the room.' 
    scene black with dissolve
    scene bg officier_back with dissolve 
    pause 0.01
    'You open it and you find yourself in a police officer\'s office.'
    'The officer, who is turned away from you, looks over his shoulder with a puzzled expression.'
    'However, he quickly grasps the situation as he overhears on his talkie-walkie that a man is hiding within the police station.'
    'Swiftly, he reaches for his gun on the nearby desk and points it at you. You are promptly arrested' 
    scene black with dissolve
    pause 1.0
    jump end 
label chair:
    scene black with dissolve
    scene bg police_man_standing_at_the_door with dissolve
    pause 0.01
    'The chair didn\'t come to any use because in a matter of seconds a police man opened bruskly the door.'
    'The policeman handcuffed you with swift precision.'
    jump Continue4
label Continue4:
    scene black with dissolve
    scene bg interrogation_room with dissolve
    pause 0.01
    'You find yourself confined within the stark walls of the interrogation room, the gravity of your situation becoming painfully clear.'
    'With nowhere to escape, you realize you\'ve been caught..'
    'the hacker has not only invaded your life but has exposed your deepest secret, turning your world upside down'
    scene black with dissolve
    pause 1.0
    jump end

label shelf:
    'As you were moving the shelf a noise was made.'
    scene black with dissolve
    scene bg police_man_standing_at_the_door with dissolve
    pause 0.01
    'In a matter of seconds, a policeman burst through the door and handcuffed you so quickly that you had no time to react'
    jump Continue4
label roof: 
    scene black with dissolve
    scene bg roof with dissolve
    pause 0.01 
    'You reached the roof level but the door to the roof top is closed very well'
    'As you try to backup you hear police officers yelling'
    jump caught1               
label Conference:
    scene black with dissolve
    scene bg conference_room with dissolve
    pause 0.01
    'Check if there\'s another way out of the conference room that might lead you to a safer or more strategic location within the building.'
    'You don\'t find anything..'
   
    'While you\'re scouting for a hiding spot, such as under the table, the door suddenly swings open and police officers enter the room.'
    jump caught1
label caught1:
    scene black with dissolve
    scene bg policeman_conference_room with dissolve
    pause 0.01 
    p 'Stand still, don\'t move you are being arreseted'
    jump Continue4 

label dashDoor:
    scene black with dissolve
    scene bg two_police_standing_by_the_door with dissolve
    pause 0.01          
    'You make a swift dash toward the door, but unfortunately, two policemen spread their arms wide and catch you forcefully'
    jump caught1

label Standing:     
    'The lady hangs up and makes a discreet hand signal to a nearby officer.'
    scene black with dissolve
    scene bg nearby_police with dissolve
    pause 0.01 
    'You watch, your pulse quickening, as they engage in a brief, hushed conversation, occasionally glancing at a computer screen and then back at you'
    'The air feels thick as the officer ends the conversation and starts walking towards you with deliberate steps'
    'While reaching into his back pocket, which appears to contain handcuffs, he says:'
    scene bg policetalk with dissolve
    pause 0.01 
    p 'Hey buddy,  just stay right where you are. I have a few questions for you' 
    menu:
        'What are you doing next?'
        "running out of the station":
            jump dashDoor 
        "stay still ":
            jump StayStill
label GiveUp: 
    scene black with dissolve
    pause 1.0
    scene bg keep_trying  with dissolve
    pause 0.01 
    'As you give in, a police officer\'s voice cuts through the air, commanding you to get on the ground.'
    'With a heavy heart, you comply, dropping to the pavement as instructed.'
    'The cold surface presses against your palms as you acknowledge defeat, surrounded by the watchful eyes of bystanders.'
    'Soon, strong hands pull you up and guide you into the back of a waiting police car'
    'Soon, strong hands pull you up and guide you into the back of a waiting police car while the click of handcuffs signaling your capture.'
    'Groups of people gather, their murmurs blending with the noise of the sirens. '
    scene black with dissolve
    pause 1.0
    jump end 





    

#FIRST CHAPTER
#LAWYER TASK (IBTISSEM)
label choice2_lawyer:
    scene black with dissolve
    pause 1.0
    scene glitshed5 with dissolve
    pause 2.0
    scene glitshed5 with dissolve
    pause 2.0
    scene black with dissolve
    pause 2.0
    scene bg pc with dissolve
    user"This can't be happening. Why me? What did I do to deserve this?"
    user"Maybe if I just ignore it, it'll go away. Yeah, that's it. I'll pretend like I never saw this message, and everything will go back to normal."
    user"No, I can't just ignore it. What if they're serious? What if they come after me or... or someone I care about?"
    "Your body sags against the familiar softness of your bed as you contemplate your current situation."
    user "I can’t let this spiral out of control, but I’m not quite sure what to do. I just need to keep calm."
    "The room is filled with the soft glow of your computer screen as you in silence, lost in thought."
    "Eventually, exhaustion takes over, and you drift off to sleep."
    show  black with out_eye
    scene black with fade
    "You're jolted awake by creaking noises" with vpunch
    "you see your son standing there, looking at you with concern ..."
    show bg blur with in_eye
    scene bg blur2 with dissolve
    pause 0.4
    scene bg kid with dissolve
    "Samy" "Hey, Dinner's ready, come on down..."
    "You rub your eyes, trying to shake off the tension"
    user "Um, yeah, I'm okay ... Just not feeling hungry right now. You guys go ahead and eat without me."
    "Samy" "Sure thing. But seriously, are you alright? You look kinda rough."
    "You force a smile"
    show bg smile with dissolve
    user "Yeah, just a bit tired, that's all."
    scene black with dissolve
    scene bg door with dissolve
    "You hear the soft click of the door closing as your son leaves the room, leaving you alone with your thoughts..."
    
    scene black with dissolve
    "Damn it all, if I don’t do what he says, I'll lose you guys."
    pause 0.3  
    centered"{cps=25}I....I'd rather die than have that...{/cps}"
    pause 0.9

    "Birds chirping wake you abruptly..."
    scene bg room with dissolve
    "Startled, you grope for your phone."
    user "This is really not the time to fall asleep ..."
    "6:50 PM. Ten minutes until the supposed task arrives..."
    scene bg pc with dissolve
    "You shuffle to your computer, setting it up for the day."
    "Suddenly, the screen flickers and a terminal pops up"
    scene black with dissolve
    pause 1.0
    scene glitshed6 with dissolve
    pause 2.0
    scene glitshed6 with dissolve
    pause 2.0
    scene black with dissolve
    pause 2.0
    centered"this is start of our game"
    centered"First Task: Swipe 200 grand from the target at this exact location: 2207 Oak Street, Apartment 91, Unit 1."
    scene bg pc with dissolve
    "The first task didn't seem as challenging as you anticipated, in fact it makes you wonder if the hacker tailored it to exploit your past..."
    scene black with dissolve
    pause 1.0
    scene bg day1 with dissolve
    pause 2.0
    scene black with dissolve
    scene bg pc with dissolve
    "you plug the address into your map app"
    "It directs you to a law firm named Justice and Order & Co."
    user "Now, why would this guy have anything to do with a firm like this..."
    scene black with fade
    "Rinng Ring ...."
    user "..."
    "... You hear the sound of the door bell ringing"
    "Son" "I will get it..."
    scene black with dissolve
    scene bg hall with dissolve
    user "NO DON'T !"
    "Son" "Oh.. umm okay"
    user "So- Sorry for yelling but I'm waiting for someone important"
    "You peek through the peephole but you find no one"
    scene black with dissolve
    scene bg package with dissolve
    "but there's a small package on your doorstep."
    user "What is this ?"
    "You open it to find a flash drive...."
    user"This must be it, the key to swiping the cash"
    "You feel you nerves buzzing"
    scene black with dissolve
    scene bg house with dissolve
    user"I should probably call the firm's number"
    "Ring ring ..."
    pause 0.3
    show sue  at right with dissolve
    "???" "Hello, this is Sue from Justice &co office."    

    menu HeySue:
        S "How can I be of any help?"       
        "I wanna learn more about the attorney in your firm.":
            jump Sue
        "I'd like to request your services.":
            jump service
label Sue:
    S "That would be Mr. Krysa he is a qualified attorney at law"
    S" with 10 years of court experience and a stellar record"
    S" I’m sure you’re going to find him very satisfying"
    menu :
        S" Would you like to schedule a meeting ?"
        "Yes, please":
            jump service
                 
 
                

label service:
    S "Sure, May I have your name for scheduling purposes?"    
    menu optional_name:
        "Tell her the truth":
            jump theTruth
        "Tell her a lie":
            jump TheLie


    label theTruth:               
        user "Certainly, my name is [username]"
        pause 0.2
        user "Maybe I shouldn't have told her my real name...Oh well, No point crying over spilled milk."
        jump assistance
 
    label TheLie:
        "Certainly, my name is umm... Michael. Michael Jones."
        user "Wow.... how creative of me"
        user "but, I can't go around telling her my real name."
        jump assistance

label assistance:
    S "Noted. What can I assist you with?"
    menu :
        user "I need help with my ...."
        "Divorce Case":
            jump alright
        "Financial Case":
            jump alright


label alright:
    "Alright, we have an opening at 5 PM. Is that convenient for you?"
    "Yeah, sounds good. See you then."
    hide sue with dissolve
    "you hang up"

    user "Alright, I've got some time to kill before the appointement. What should I do next?"
#define actions = set()
menu menu1 :
    "What will you do?"
#    set actions
    "Disguise yourself":
        jump disguise
    "Search the net about the law firm":
        jump net
    "Try to contact the hacker to give you more info":
        jump contact


label net:
    scene black with dissolve
    scene bg pc with dissolve
    pause 0.2
    user "I know what i should do!"
    user "I will look through the reviews to find what's so special about Justice &co"
    "after 5 minutes of scrolling through suspicious looking 5 stars reviews"
    user "pfft.. looks like i will gain nothing of value from searching them up"
    user "Wait what's this ?"
    user "A throwaway account left a 1 star review ...."
    "\"The truth will be known\""
    user "interesting... to say the least"
    jump contact

label disguise:
    scene bg disguise with dissolve
    "You scrutinize yourself in the mirror." 
    "With glasses, a wig, gloves, and makeup, you've crafted a whole new persona"
    "It's like your theater days are finally paying off"
    "You look in the mirror, amazed by how well the disguise works!"
    
    
    jump contact

label contact:
    scene bg keyboard
    "Well it's better to not waste time and get straight to the point now"
    "You hover over the keys, uncertain of what to ask, you write"
    user "I have a couple of questions about the task ..."
    "the screen flickers"
    scene black with dissolve
    scene glitshed with dissolve
    h "Haha, bring it on. What do you wanna know ? You are only allowed one question though"
menu  :
    "so pick wisely!"
    "How am i supposed to steal the money exactly ?":
        h "{color=#f00}You bagged 200 million, yet you're still struggling? Seriously?{/color}"
        h "Ugh, you're killing me... If you ever need a hand with that"
        h "I will help you out" 
        h "I'm not that cold-hearted, you know. LOL"
        jump steal
    "what happens if I get cought ?":
        h "{color=#f00}LOL, that's on you, buddy. But hey, remember, if I end up in cuffs{/color}"
        h "{color=#f00}it's not just me you should worry about.{/color}"
        h "{color=#f00}Say goodbye to your precious family...{/color}"   
        jump caught
    "what exactly will you do with the money ?":  
        h "{color=#f00}Hmm, normally I wouldn't respond{/color}"
        h "{color=#f00}but hey, since it's relevant to your tasks, I'm feeling generous.{/color} "
        h "Listen up. You'll need that money for your next task to win over someone crucial"
        h "so don't screw it up, okay? Enough spoilers for now, but remember"
        h "failure isn't an option here"
        jump money1

label steal:
    user "He's offering to help? Hmm ... Perhaps I should keep that in mind."
label caught:
    "You chuckle to yourself at the hacker’s bold warning."
    "Oh well, regardless of his silly threats, you know the urgency at hand."
    "You’ve got to stay focused and complete the task before the window of opportunity closes."
label money1:
    "You know that the stakes are high, but you’re convinced that you can pull it off."
    "The adrenaline rush from the pressure and the urgency of the task puts you on edge, yet you still manage to keep a calm exterior..."

scene black with dissolve
pause 1.0
scene bg day2 with dissolve
pause 2.0
scene black with dissolve
scene bg laws with dissolve

"You arrive at the prestigious Law Firm downtown"
menu :
    "What will you do?"
    "Scower the building":
        jump Scower
    "Enter the building":
        jump Enter    

label Scower:
    scene black with dissolve
    scene bg camera with dissolve
    "You look up at the towering building in front of you, its glass façade sparkling in the light."
    "An impressive display of luxury, modernity, and class, it stands as a symbol of the city's booming economic prosperity."
    "you notice a number of cameras guarding the building..."
    user "This is not going to be easy"
    jump Enter

label Enter:
    "You enter the building, passing through the reception area"
    scene black with dissolve
    scene bg first with dissolve
    "Sue the receptionist greets you with a polite but cold demeanor." 
    "Her piercing gaze and sharp demeanor give off that “mean business” vibe."
    S"You must be the person who called a while ago, please follow me"
    scene bg receptionist3 with dissolve
    "You follow Sue down the hallway"
    "aware of the towering building and its elegant design surrounding you as you make your way toward Michael Krysa's office."
    scene bg chow with dissolve 
    "Sue looks over to you"
    S "He is waiting for you, please enter "  
   
menu :
    "You're in front of the office."
    "Observe the office":
        scene black with dissolve
        scene bg law_room with dissolve
        "The elegant wood decor, impressive degrees adorning the walls"
        "it all screams Success."
        "{cps=25}But for some reason it all seems Shallow...{/cps} "
        menu :
            "Enter the office": 
                jump enter
                
        
    "Enter the office":
        label enter:
            scene black with dissolve
            scene bg lawyer1 with dissolve
            "Krysa gets up to shake your hand"
            K "Take a seat, please" 
            user"Thanks"
            "You follow Krysa's instructions as you take a seat"
            user "So this is him.."     
            user "Why do i get this weird feeling about him"
            scene black with dissolve
            scene bg the_law with dissolve
            user "No, THAT guy is getting inside my head..."
            user "I feel really bad for this man"
            user "He seems like a nice guy, and he definitely doesn't deserve this"
            "You cannot help but feel a wave of guilt wash over you as you see Krysa sitting there, completely unaware of the situation."
            pause 0.5
            K "I understand you need my expertise"
            K "Lay it out for me."
            "You clear your throat, weaving your fake backstory while discreetly retrieving the small vial of sedative from your jacket pocket..."
menu :
    "So you will.."
    "Fake a coughing fit to distract Krysa while you spike his coffee":   
        jump fake
    "Confront Krysa, and ask him for help":
        "You approach Krysa cautiously, mindful of the hacker's threat to your family"
        user "Listen, I need to come clean. I wasn't entirely truthful when I booked this appointment"
        scene bg lawyer_neutral with dissolve
        "Krysa raises an eyebrow, intrigued"
        user "I do need your help, but it's for something else entirely"
        "Krysa studies you, concern etching his features"
        K "Are you alright? You look terrible"
        "Summoning your courage, you disclose the truth about the hacker and your intended actions, even showing him the vial of sedative you had brought"
        user "I need your help. I can't let this hacker harm my family"
        "Krysa's expression shifts to one of genuine concern and sympathy"
        "However, as you delve into the details about the hacker, you sense a certain ominous air about him"
        "You quickly push aside the feeling."
        "you choose to trust him, hoping he can indeed help you"
        K "I'm so glad you decided to do the right thing"
        K "Don't worry everything is under control now"
        K "I know this guy, He is a cyber vigilante wanna be"
        K "we will make sure that he will never do this to someone else ever again"
        K "excuse me now , I have to make a phone call"
        scene bg law1 with dissolve
        pause 0.4
        scene bg law2 with dissolve
        pause 0.4
        scene bg law3 with dissolve
        K "I wil not be gone long"
        scene black
        pause 0.2
        scene bg law4 with dissolve
        "As you watched krysa leave, you felt a massive surge of comfort"
        "like a heavy burden was lifted from your chest"
        menu :
            "What's your next step?"
            "Wait in the office":
                jump wait
            "search the office":
                
                jump search3
label search3:
    user "But even still"
    user "I need to know what that psychotic guy wants with this law firm ..."
    user "if not for my sake, it's for krysa's ..."
    user "Yeah i would still be breaking in, but it's for good reasons"
    jump menu5

label wait:
    "You decide to wait for Krysa's return, hoping to learn more about his intentions."
    "As you sit in his office, the minutes tick by, and you begin to feel uneasy."
    "Eventually, you hear the sound of Krysa's footsteps approaching."
    "But instead of entering the office, you hear him speaking on the phone in hushed tones."
    scene black with dissolve
    scene bg full with dissolve
    "Your curiosity piqued, you strain to listen in on the conversation, trying to make out what he's saying."
    K"Yes he is with --- Please do -- I will  -"
    "But before you can hear anything of significance, Krysa abruptly ends the call and enters the office."
    "He gives you a reassuring smile, but you can't shake the feeling that something isn't right."
    menu :
        "confront him about the phone call":
            jump confront
        "silently wait for him to talk":
            jump waitM

label confront:
    scene black
    "You confront Krysa about his phone call, demanding to know who he was talking to."
    scene black with dissolve
    scene bg vii with dissolve
    "But Krysa brushes off your questions, insisting that it was just a personal matter."
    "Feeling frustrated and suspicious, you realize that Krysa is not being entirely truthful with you."
    "But without concrete evidence, there's little you can do to challenge him further."
    user "Krysa, I can't shake off this feeling of unease. Tell me the truth."
    scene bg stressed with dissolve
    "You say menacingly"
    "Krysa shifts uncomfortably in his seat, avoiding your gaze."
    K "I had to call the police..."
    user "You... you called the police on me?"
    scene bg stressed1 with dissolve
    "You struggle to contain your anger, your mind racing with disbelief."
    menu :
        "What will you do?"

        "try to run away":
            scene black with dissolve
            scene bg close2 with dissolve
            "With a quick glance towards the door, you make a split-second decision to make a run for it."

            "You push yourself away from Krysa, leaping out of your chair and darting towards the exit."
            scene black with dissolve
            scene bg what with dissolve
            S"hey, what do you think you are doing ?? "
            scene bg close2 with dissolve
            "But before you can reach the door, you hear the unmistakable sound of police sirens approaching."

            "Your heart sinks as you realize that you won't make it in time."

            "You sprint towards the exit, but just as you reach for the door handle, it swings open, revealing a group of police officers with their weapons drawn."
            scene black with dissolve
            scene bg policie with dissolve
            "They quickly move to apprehend you, their voices commanding you to get down on the ground."

            "Realizing that escape is futile, you comply with their orders, feeling the cold steel of handcuffs being clasped around your wrists."

            "As you're led away by the police, you can't help but curse the day you trusted Krysa, knowing that his betrayal has sealed your fate."

            "you catch one last glimpse of Krysa, his smile now a sinister grin."

            "You've been played, and now you're paying the price for trusting the wrong person."
            scene black with dissolve
            pause 1.0
            jump end
        "Quickly Subdue Krysa":
            "Your mind races with adrenaline-fueled detekermination as you realize Krysa's betrayal."
            "You can't let him get away with this."
            "In one swift motion, you lunge forward, grabbing Krysa's arms and pinning him to his chair."
            "Krysa struggles against your grip, but you hold him firmly in place, your anger lending you strength."
            user "If my military background was to be thanked for anything in my life, It will be now "
            user "But even still, i feel bad doing this to an old man.."
            "feeling the intense pressure of the police countdown, you remember what is at stake if you do not follow your task"
            jump menu5

        


label waitM:
    "You choose to remain silent, opting to observe Krysa's behavior and wait for him to speak first."
    "As Krysa enters the office, you carefully watch his movements, searching for any sign of deception."
    "He offers you a reassuring smile, and for a moment, you start to doubt your suspicions."
    "Maybe you were overthinking things. Maybe Krysa was truly on your side."
    "You engage in small talk with Krysa, his friendly demeanor putting you at ease."
    "He seems genuine, sharing stories about his work and life outside the office."
    "But just as you start to relax, you hear the distant wail of police sirens."

    "Your blood runs cold as the realization hits you. Krysa betrayed you."
    "You jump to your feet, but it's too late. The door bursts open, and police officers flood into the room."

    "They arrest you on charges of conspiracy and attempted sabotage, reading you your rights as you're handcuffed."

    "As they lead you away, you catch one last glimpse of Krysa, his smile now a sinister grin."

    "You've been played, and now you're paying the price for trusting the wrong person."
    scene black with dissolve
    pause 1.0
    jump end

            

label fake:
        "You decide to simulate a severe coughing fit, and surprisingly ..." 
        pause 0.2
        "it succeeds!"
        "Krysa appears momentarily distracted from his usual focused demeanor as he checks on you."
        "Seizing the opportunity, you discreetly slip the sedative into his coffee, then apologize for the inconvenience "
        scene black with dissolve
        scene bg la2 with dissolve
        "you watch cautiously as he takes a long sip. At first, he continues discussing the case normally."
        scene black with dissolve
        pause 1.0
        centered "But soon his words begin to slur, and his eyelids grow heavy as the powerful sedative takes effect."
        scene black with dissolve
        scene bg la1 with dissolve
        "Within moments, Krysa's head drops and he slumps forward unconscious on his desk"
        "knocking down a crystal figurine that was sitting on the side of the table."
        "You freeze, listening carefully for any sounds of Sue the secretary in the outer office area."
        scene black with dissolve
        scene bg la3 with dissolve
        "You prop Krysa's head up on his arm, trying to make him look like he is just resting. As you head for the door, you hear Sue's voice."
        user "I should act swiftly, i can't let Sue know what happened here"

menu:
    "What will you do ? "
    "Be straight with Sue - tell her Krysa is feeling ill and needs privacy":
        jump search

    "Take a big risk and just lock her out while you work":
        jump lock
label lock:
    "In a moment of panic, you lock the door to the office just as Sue tries to barge in"
    scene black with dissolve
    scene bg full with dissolve
    S "Mr. Krysa? Why is this locked?"

    "You hear the knob rattling  aggressively" 
    S "Open up right now!"
    "You back away, realizing your grave mistake. Sue won't simply give up and there's no way out."   
    menu :
        "You will.."
        "Try to reason with Sue ":
            jump reason
                
        "Subdue Sue if she gets through":
            default subdue = 10
            jump Subdue
                
                
label Subdue:
    scene black with dissolve
    centered "Realizing reasoning with Sue is futile, you brace yourself as she tries to force open the barricaded door. The moment it cracks open, you lunge forward and tackle Sue to the ground."
    centered "Keeping her restrained with one arm, you quickly grab a roll of duct tape from Wright's desk drawer. You tear off a strip with your teeth and bind Sue's wrists and ankles, immobilizing her."
    scene black with dissolve
    scene bg bye with dissolve
    "Only then do you remove your hand from her mouth"
    user "I'm sorry, i really don't want to do this but i don't have a choice"
    jump search2
label reason:
    "Thinking quickly, you realize deceiving Sue one last time may be your best chance to get her away from the office door before she calls for backup."
    menu:
        "You will.."
        "Take an agressive tone ":
            jump agressive
        "Take a calming tone ":
            jump calming
        "Take an innocent tone":
            jump innocent

label agressive:
    "You take a deep breath and shout back through the door in your most authoritative tone. "
    user"Hey, Sue! Quiet down and focus. Let's straighten this out. There's been a misunderstanding."
    "The pounding momentarily stops as she pauses..."
    S "A misunderstanding? What are you talking about? Open this door right now!"
    user "NO... i can't do that but you need to trust me"
    S "And why exactly should I trust a single word you say right now?"
    jump Subdue


label calming:    
    "You take a deep breath to calm your nerves"
    user"Sue, hold on! Take a breath and tune in. We need to clear something up. It's not what you think."
    S "Stop talking like you know me ! why are you keeping the damn door locked ?? "
    S "and why isn't Mr Krysa responding ??"
    user "NO... i can't do that but you need to trust me"
    S "And why exactly should I trust a single word you say right now?"
    jump Subdue

label innocent:
    "You decide to keep a innocent tone to fool Sue"
    user"Sue, hey! Slow down and really hear me out. It's important. I'm not sure what happened the lawyer here just collapsed"
    S"How am i supposed to believe you when you closed the door on me ??"
    S"And why exactly should I trust a single word you say right now?"
    jump Subdue




label search:
        scene black with dissolve
        scene bg recof with dissolve
        "As you crack open the door, she's already standing there with a concerned look on her face."
        "Umm Ah Sue, sorry for the noise. Mr. Krysa is feeling quite unwell, it seems that he overworked himself "
        "you say, putting on your best concerned expression"
        "He's just...resting at the moment. we will resume our buisness shortly.."
        scene bg look with dissolve
        "Sue looked over at the lawyer desk seeing him hunched over his computer, she sighed"
        "He is always like this, i wish he wouldn't tire himself that much..."
        scene bg mary with dissolve
        "Anyway, please tell him i'm going out since i finished my shift"
        user "sure thing"
        "If she was more curious, I would have been caught, i should be more careful from now on.."
        "now that Krysa and her are out of the way, what should i do ?"
label search2:
        "you turn your attention back to the important matter at hand" 
        "- searching Krysa's office for any relation to the hacker, and completing the task..."
define actio = set()
menu menu5:
    set actio
    user"Now, what will you do ?"
    "Look through the files":
            scene black with dissolve
            scene bg files with dissolve 
            "Towering file cabinets and overflowing boxes of documents cover the walls, seemingly full of potential leads."
            scene bg shelf with dissolve
            "Going through all the paper trails could unearth a treasure trove of information, but it also appears incredibly time-consuming to sift through it all"
            "you try to search for any clues, but you come up short-handed ..."
            jump menu5
    "Look inside the desk":
            scene black with dissolve
            scene bg deski with dissolve
            
            "Your gaze is immediately drawn to the large, imposing oak desk that serves as the room's centerpiece."
            "Stacks of files and papers are scattered in its surface, blanketed by a variety of office supplies and lawyers' knickknacks"
            "As you searched through the drawers in a last-ditch effort, your hopes dwindled as you found nothing."
            scene black with dissolve
            scene bg desk with dissolve
            menu:
                "Continue searching":
                    jump continue_SEARCH
                "Give up":
                    jump give_UP
        

    "Look inside the computer":
            scene black with dissolve
            scene bg pc_law with dissolve
            "A sleek-looking computer sits atop the desk "
            "You notice security footage as well as clients registry forms"
            user"Might as well delete these"
            if truth == 10 :
                "At least i can remove my name and fix my mistake from earlier"
            user"Now what should i do"
            jump menu5

          
label continue_SEARCH:
        scene black with dissolve
        scene bg drawe
        "Disheartened, You decided to keep searching"
        "as you were shuffling between the the drawers you noticed a major weight difference and that the second drawer design was misaligned"
        "so you decide to investigate it further"
        scene black with dissolve
        scene bg drawer
        "you tap the bottom of the drawer, and bingo, a hollow sound resonated. There must be a false bottom! "
        jump investigate_drawer

label give_UP:  
        scene black with dissolve
        scene bg drawe
        "Disheartened. you decided that the search was futile"
        "you put up the drawer's content in the best order that you remember"
        "accidently droping a paper clip into the bottom of the drawer while at it"
        scene black with dissolve
        scene bg drawer
        "you hand brushes against the seemingly normal bottom, causing it to tilt slightly"
        "you tap the bottom of the drawer, and bingo, a hollow sound resonated. There must be a false bottom!"
        jump investigate_drawer

    
label investigate_drawer:
"you proceed to tear apart the mechanism, to find out stack of files ..."
menu kk:
    "You will.."
    "Search through the files ":
        scene black with dissolve
        scene bg papers1 with dissolve
       
        
        user "Looks like they all relate to a certain Hospital case.."
        user "But it's weird that they were all kept secluded here "
        user "Maybe they can provide clues for me to figure out why is that guy interested with this law firm "
    "Take pictures of your findings":
        user "I don't exactly know where these files fit in the puzzle"
        user "But they seem too important to miss"
        "you take a photos of the files"
        user "done"    
        

    

label mail:
    user"Let's read"
    "Dear Michael"
    "Regarding the Brown vs. Central Hospital case, your efforts are crucial to us."
    "We're committed to compensating you appropriately. In addition to the agreed funds settlement"
    "I'm authorizing an extra $10,000 payment upon optimal case resolution"
    "This compensation will be discreetly transferred from our offshore accounts"
    "Your counsel has been a huge help"
    "Thank you"
    "Dr xxxx xxxxx"
    user"It has been scribbled over"
    "The lawyer has been receiving secret offshore payments? I wonder what this is all about"
    "he has been taking bribes from a certain docter to lose his cases ??! This is insane, why would the hospital go this far to win ?"
    scene bg papers2 with dissolve
    "you look through the other files and you notice a similar pattern"
    "Something very wrong is happening within this hospital"
    "And what's most chilling is the implication is that a Doctor is behind all of this!!"
    "what should i do next"

menu final :

    user"Now what should I do"
    "further Explore the office":
        "Seeing what I've seen here, it's clear I need to investigate this office more thoroughly"
        jump second
        
    "Ask for the hacker help to acces the lawyer digital money wallet":
        jump money



label second: 
    define act = set()
    menu:
            set act
            "What will you do?"
            "look into Photo frame":
                scene black with dissolve
                scene bg frame with dissolve
                "You stumble upon a photo frame displaying the lawyer's son"
                "As you hold it, memories of your own son flood your mind, reminding you of the high stakes involved."
                user"This guy's situation is eerily similar to mine. Is this why that guy chose me?"
                user"Is it retribution for the stolen money I got? He sees this lawyer and me as one, playing with our lives to fulfill some twisted justice fantasy"
                jump second
            "look into the Medals and prizes":
                scene black with dissolve
                scene bg diploma with dissolve
                "At the center of it all, proudly displayed, were shiny Public service awards"
                "Legal industry recognitions, and Academic honors. With a portfolio gleaming with these accolades"
                " it's no wonder Mr. Lawyer here could sweep a few bad cases under the rug."
                " He seemed to have it all together, but I guess perfection isn't always what it seems"
                jump second
            "I've had enough":
                jump money        
label money:
        "As you make the call to the hacker's burner number" 
        scene black with dissolve
        scene bg phone_law with dissolve
        "an automated robotic message instructs you to insert the USB drive into the lawyer's laptop."
        "With a sense of resignation, you comply, and a terminal window promptly opens up."
        scene black with dissolve
        scene bg pc_law with dissolve
        h "Thank you for your hard work"
        h "The money will be delivered straight to your account."
        "With a bitter taste of revulsion lingering in your mouth, you power down the laptop and cast a final, piercing gaze around the office."
        if subdue == 10 :
                "You look down at the subdued Sue, your voice low but firm. Not a word of what happened here leaves this room," 
                "Because if you don't comply, everything I just uncovered will go public - and you'll be right in the middle of the fallout."
        scene bg phone_law with dissolve      
        "you regain your calm and look through the window ...."
        user"I'll hunt you down, no matter what it takes, Just you wait you declare with unwavering resolve"
        user"the intensity of your determination echoing through the silent room."
        scene black with dissolve
        scene bg camera with dissolve
        "you stepaway out from the law Firm trying to blend with the crowd"
        "you go into a public restroom"
        "and get rid of the make up and clothes"
        user "like nothing happened.."


#SECOND CHAPTER AMIRA

"You return home"
label forensic:
scene black with dissolve
pause 1.0
scene glitshed7 with dissolve
pause 2.0
scene glitshed7 with dissolve
pause 2.0
scene black with dissolve
pause 2.0

scene glitshed with dissolve
h "I liked how obedient you were [username]! You have now successfully completed your first task."
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
    "Next day...\n"
    scene black with dissolve
    pause 1.0
    scene bg day3 with dissolve
    pause 2.0
    scene black with dissolve
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
    scene bg run with dissolve
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
    centered "Next day..."
    scene black with dissolve
    pause 1.0
    scene bg day4 with dissolve
    pause 2.0
    scene black with dissolve
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
    centered "Next day..."
    scene black with dissolve
    pause 1.0
    scene bg day4 with dissolve
    pause 2.0
    scene black with dissolve
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
    centered "Next day..."
    scene black with dissolve
    pause 1.0
    scene bg day4 with dissolve
    pause 2.0
    scene black with dissolve
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
    centered "Next day..."
    scene black with dissolve
    pause 1.0
    scene bg day4 with dissolve
    pause 2.0
    scene black with dissolve
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
    scene black with dissolve
    pause 1.0
    scene bg day5 with dissolve
    pause 2.0
    scene black with dissolve
    scene bg minagate with dissolve
    "You park in front of the university and wait. She just came out."
    menu:
        "What will Syou do?"
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
        play sound "hit.mp3"
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
        stop sound
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
        play sound "police.mp3"
        "Suddenly, you hear the sound of police surrounding your house."
        scene bg police with dissolve
        user "DAMNN!!"
        "The university gate cameras captured everything, you've been located by the police."
        stop sound 
        scene black with dissolve
        jump end
    
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
    scene black with dissolve
    pause 1.0
    scene bg day5 with dissolve
    pause 2.0
    scene black with dissolve
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
    jump doctor_lina

    
label doctor_lina:


# DAY6 AND DAY7
#picture in his desktop

    "Stay strong ,[username] you're in the final stretch. Don't mess it up now."
    scene black with dissolve
    pause 1.0
    scene glitshed8 with dissolve
    pause 2.0
    scene glitshed8 with dissolve
    pause 2.0
    scene black with dissolve
    pause 2.0
    

    scene black with dissolve
    pause 1.0
    scene bg day6 with dissolve
    pause 1.0
    scene glitshed with dissolve
    user'frustrated sigh What now?'
    h'Ah, always so eager to chat, aren\'t we? I\'ve got a little task for you.'
    user "What kind of task?"
    h "Oh, nothing too difficult, my friend. Just a small favor I need"
    user" I'm not your friend, and I'm not in the business of doing favors for hackers"
    h" Oh, but you've been doing quite a few favors for me already, whether you realize it or not. Consider this one the cherry on top"
    user "What do you want?"
    h "I want you to... kill someone for me."
    user "WHAT??? No! This is insane. I already can't live with myself for the things I had to do. If I kill someone, I'll be no better than you "
    h "Fine then, be selfish. I hope you would like your new life in prison "
    user "No, anything but that..."
    scene bg elderlyman with dissolve
    pause 0.01
    h"here is his photo. His name is Mark"
    "You hear a notification sound buzzing"
    user "What now?"
    scene bg adresse with dissolve 
    pause 5   
    
    scene bg myroom with dissolve 
    pause 0.01  
    "Paralyzed with dread, you take a seat in a nearby chair in your room... No, this can't be happening"
    "You hear another notification sound" 
    "What would you do ?"
    menu:
        "Check the new message immediately":
            jump check
        "Ignore the message and try to come up with a plan":
            jump ignore

label check:
    "You reluctantly pick up your phone and read the message"
    scene bg readmsg with dissolve
    pause 3 
    'The message includes the location where Mark will be and the exact time of his arrival'
    "The weight of the decision crushes you. You have to act fast"
    menu:
        "Go to the adress":
            jump goAdress

label ignore:
    'You ignored the text, but...'
    'Five minutes later, your phone started ringing. It stopped for a few seconds, then started ringing again.'
    'Leaving you no choice but to read the text'
    menu:
        'Fine i\'ll just read it!':
            jump check

        

label goAdress:
    scene bg closet with dissolve
    pause 0.01 
    "Before leaving the house you made your way to the closet, With a shaky hand, you retrieve a gun from a hidden compartment and left the house"
    "Your heart pounds as you drive to the address"
    scene bg markhouse with dissolve
    pause 0.01 
    'As you approach the adress, a house come into view. It must be Mark\'s house'
    "What will you do know?"
    menu:
        'Park a block away so no one becomes suspicious':
            jump parkAway
        'Park in front of the house entrance':
            jump ParkInfront
        
label parkAway:
    scene bg blockaway with dissolve 
    'After parking a block away from the house, you walk cautiously towards the entry'
    'What are you going to do ?'
    menu: 
        "Observe the house": 
            jump observe
        "Break into the house quietly to avoid detection":
            jump ScaryRoom

label observe:
    
    "You decide to observe the house from a hidden vantage point to gather information before making any decisions"
    "Suddenly, a figure emerges from the shadows, sending a chill down your spine"
    "It's the forensic doctor, Charles"
    scene bg mantoback with dissolve
    "You watch as the doctor makes his way to the back of the house, constantly looking over his shoulder"
    'What do you do ?'
    menu:
        'Follow the doctor':
            jump Follow
        'Stalk him from far':
            jump StalkFar  

label Follow:
    'You walk behinde the doctor but he turns around once again and he sees you'
    scene bg manturn with dissolve
    f "Hey you ! What are you doing here!"
    'How are you going to react?'
    menu:
        'Run away as fast as you can to your car':
            jump RunFromCharles
        'Lie to him':
            jump LieToCharles

label ParkInfront:
    scene bg housecar with dissolve
    'While you\'re parcking near the house you see another car approaching to the house entrance'
    'The man who\'s driving the car looks at you, a look of confusion on his face '
    'But in that moment, you realize that this man is Mr. Charles, the forensic doctor'
    'He then grabs his phone and make a call'
    scene bg angrycharles with dissolve 

    'A few moments later, you see Mark rushing out of the house, slamming the door behind him.'
    'And he yells'
    m 'Hey, you! Who are you? What makes you think you can park on my property?'
    'What do you do now ?' 
    menu: 
        'Drive away as fast as possible':
            jump DriveFast
        'Get out of the car and talk to mark':
            jump TellTRUTH

label TellTRUTH:
    'You tell Mark everything about the hacker and how he told you to kill him and that he has some strong evidance that he\'s threatening you with'
  

label DriveFast: 
    'You try to start your car and drive away quickly, but the man in the car follows you.'
    scene bg manturn with dissolve
    'He ends up catching you'
    'What choice are you making ?'
    menu:
        'Make an excuse and lie to him':
            jump LieToCharles
        'Tell him that you want to talk to Mr. Mark':
            jump TellTRUTH



label RunFromCharles:
    'You tried to run from him, but he catches you, grabbing you by your shirt'
    jump LieToCharles

label LieToCharles:
    'You have to come up with a believable lie.'
    'What are you going to say ?'
    menu:
        'Sorry, i got sent the wrong location':
            jump KeepLying
        'Sorry, i\'m bipolar and sometimes i do crazy things':
            jump KeepLying 


label KeepLying:
    'After hearing your lie Mr. Charles let you leave, but he warns you that if he sees you again he\'s calling the police'
    'He also took pictures of your car matricule '
    scene bg faraway with dissolve 
    'You\'re back in your car'
    'And you park miles away from the house, waiting for the hacker to contact you again...'  
    'After almost two hours you get a call from an unknown number'
    h'You little bastard, why haven\'t kill him yet'
    'You tried to explain to him what happend but he doesn\'t leave room to talk'
    h'Look this is your last chance, stop making dumb decsions and get the work done'
    'You tell him that you can\'t go back there because Mark is not alone'
    h'Which part of my orders you are not understanding? I want him dead Today even if it means killing anyone who\'s steping in the way'
    'The hacker hangs up in your face'
    'You go back to the house, but this time you take a route that leads you to the back of the house.'
    scene bg backdoor with dissolve
    pause 0.01 
    'When you finally get there, you notice a small, hidden back entrance to the basement.'
    menu:
        'Go take a look at that basement':
            jump ScaryRoom
label StalkFar:
    scene bg backhouse with dissolve
     
    'You observe Charles walking behind the house. It appears there is a hidden back entrance to the basement.'
    scene black 
    pause 1
    scene bg rushingout with dissolve 
    
    "Minutes later, you see both Mark and Mr. Charles leaving the house in a rush as they into Mr. Charles' car."
    'What is you next move?'
    menu:
        'Stay hidden incase they come back':
            jump KeepHiding
        'Go take a look at that basement':
            jump ScaryRoom

label ScaryRoom:
    scene bg backdoor with dissolve 
    'With all your strength, you pull open the basement door at the back of the house. It creaks open, and you descend the narrow stairs. A pungent smell of rot hits you like a wave.'
    'The room is pitch dark, so you take out your phone and turn on the flashlight' 
    'You gasp !!'
    scene bg basement with dissolve
    'In the dim light, you see a filthy hospital bed with bloodstained sheets. Surgical gloves and instruments lie scattered on a small table next to the bed.'
    'Most shocking of all are the human organs preserved in jars containig a strange liquid and displayed on dusty shelf.'
    'So Mark must be a surgical doctor, working illegally in this basement.'
    'At the bottom of the shelf, you see a drawer that opens with a key.'
    'You also notice that the basement has another entrance from inside the house'
    'What do you do now?'
    menu:
        'Open the drawer':
            jump searchParty



label KeepHiding:
    
    'You didn\'t have to wait long before they both returned. It seems Mark forgot something in the house and went back to look for it. '
    scene bg opendoor with dissolve
    pause 0.01 
    'Mark opened the door to his house, and Mr. Charles followed him inside, leaving the door open behind them.'
    'Would you like to follow them since the door is open?'
    menu:
        'Yes!':
            jump hidelisten


label hidelisten:
    scene bg basementdoor with dissolve 
    pause 0.01 
    'You notice a dim light at the base of the basement door, and you can hear two people chatting loudly.'
    'You listen closely and hear them saying...'
    f "I'M TELLING YOU MARK I'M SURE IT'S HIM! "
    f "HE WANTED TO GET REVANGE FOR SO LONG!"
    f "He\'s winning this time"
    scene bg sadface with dissolve 
    pause 0.01
    m 'Look, I know he\'s the one behind all this, but we need to be careful now.'
    m'If he pulled shit like that on Krysa and then you...I must be next'
    m'We have to burn all the documents that i have of his mom'
    m' WE HAVE TO DO IT NOW !'
    'Shocked beyond belief, you realize they know the hacker\'s identity, confirming your theory that he is seeking revenge.'
    'They stop talking for a while'
    'Which course of action are you taking next?'
    menu:
        'Confront them ':
            jump ConfrontWithGun   
        'Look for the documents in the basement after they go out ':
            jump searchParty

label searchParty:
    scene bg drawerclosed with dissolve
    pause 0.01 
    'You bend over and quietly attempt to open the drawer, but it\'s locked with a key'
    menu:
        'Look around for the key':
            jump KeySearch

label KeySearch:
    'Search the immediate area for the key, checking obvious places like nearby shelves, under objects'
    'Where do you want to search first? You need to be quick Mark and Charles could enter the basement at any moment.'
    menu:
        'Under the shelf':
            jump undershelf
        'Under the jars':
            jump CheckJars
        
label undershelf:
    'You check under the shelf using your phone\'s flashlight.'
    'There is no key, only dust.'
    menu:
        'Check under each jar':
            jump CheckJars

label CheckJars:
    scene bg jars with dissolve 
    pause 0.01 
    'You lift the first jar...'
    'Nothing is under it.'
    'Second jar...'
    'Also nothing.'
    'But as soon as you lift the third jar, a piece of paper catches your eye.'
    scene bg paperdesk with dissolve
    pause 0.01 
    'You open it and it reads: "19 20 1 9 18 19".'
    'It seems like a code.'
    'Here is the first clue to help you decipher it.'
    menu:
        'First Clue':
            jump firstClue

label firstClue:
    'Numbers and alphabets often have a direct correlation.'
    menu:
        'Decipher the code':
            jump DecipherCode
        'Need another clue':
            jump secondClue

label secondClue:
    'Each letter have a number'
    menu:
        'Decipher the code':
            jump DecipherCode
        'Need more help':
            jump thirdClue

label thirdClue:
    'Here is the mapping of numbers to letters:'
    '1 - A, 2 - B, 3 - C, 4 - D, 5 - E, 6 - F, 7 - G, 8 - H, 9 - I, 10 - J'
    '11 - K, 12 - L, 13 - M, 14 - N, 15 - O, 16 - P, 17 - Q, 18 - R, 19 - S, 20 - T, etc.'
    menu:
        'Decipher the code':
            jump DecipherCode
        'Need the answer':
            jump giveAnswer

label giveAnswer:
    'Alright, here is the solution:'
    '19 is S, 20 is T, 1 is A, 9 is I, 18 is R, and 19 is S again.'
    'The code spells "STAIRS".'
    menu:
        'Continue':
            jump FindKey

label DecipherCode:
    'Enter your answer :'
    $ user_input = renpy.input("What does the code spell?")
    $ user_input = user_input.strip().lower()
    if user_input == "stairs":
        'You are correct! The code spells "STAIRS".'
        jump FindKey
    else:
        'The correct answer is "STAIRS".'
        jump FindKey

label FindKey:
    'You realize the key must be hidden near the stairs.'
    scene bg stairskey with dissolve 
    pause 0.01 
    'You quickly move to the stairs and start inspecting the area closely.'
    'After a moment of searching, you find a loose board under the stairs. You lift it carefully and find a hidden compartment.'
    'Inside, there\'s a small, rusty key. Your heart races with excitement as you grasp it in your hand.'
    'Now you need to be quick and open the drawer.'
    menu:
        'Open the drawer':
            jump documents

label documents:
    scene bg draweropened with dissolve
    pause 0.01 
    'You open the drawer, and a wave of relief washes over you as you realize that the key you found is indeed the one needed to unlock it.'
    'But this fleeting comfort is quickly replaced by a chilling dread.'
    'As you delve deeper, you uncover multiple documents pertaining to patients. Each file contains detailed personal information and photographs, all marked with the same cause of death: heart attacks.'
    'The signatures at the bottom belong to none other than Mr. Charles, the forensic doctor.'
    'Your heart races as you push aside the patient files, only to reveal a hidden stack of papers at the back of the drawer.'
    'Each sheet is filled with clinical coldness, detailing the harvest of various organs, each paper signed by two individuals: Dr. Mark and his lawyer, Krysa.'
    'A sense of horror grips you as the pieces fall into place. Lawyer Krysa, Mr. Charles, and Dr. Mark are involved in human trafficking operation.'
    'Your hands tremble, and a cold sweat breaks out as the weight of this revelation crashes down upon you. The room seems to close in, your breath quickening as fear and panic threaten to overwhelm you.'
    'But then, you hear the front entrance of the house open with the sound of keys.'
    'Moments later, you catch the voices of the two sinister men as they make their way toward the basement.'
    'What will you do?'
    menu:
        'Put the documents and files back, close the drawer, and return the key':
            jump putBack
        "Hide immediately":
            jump HideNOW


label putBack:
    scene bg drawerclosed with dissolve
    pause 0.01 
    'You hastily put the documents and files back in the drawer. As you do, you hear the basement key turning in the lock they\'re opening the door.'
    'You quickly close the drawer with the key just as the basement door swings open, and you hear them descending the stairs.'
    'Panic sets in as you realize the key was supposed to be hidden in the stairs.' 
    'What cautious decision will you make? '

    menu:
        "Hide immediately":
            jump HideNOW
        "Leave the key in the drawer's keyhole as if they forgot it there":
            jump leaveKey

label HideNOW:
    scene bg underbed with dissolve
    pause 0.01 
    'You hide under the bed, and from your vantage point, you can see both of their feet as they stand in the middle of the basement.'
    'You strain to hear their conversation.'
    f "I'M TELLING YOU MARK I'M SURE IT'S HIM! "
    f "HE WANTED TO GET REVANGE FOR SO LONG!"
    f "He\'s winning this time"
    scene black with dissolve 

    scene bg sadface with dissolve 
    pause 0.01
    m 'Look, I know he\'s the one behind all this, but we need to be careful now.'
    m'If he pulled shit like that on Krysa and then you...I must be next'
    m'We have to burn all the documents that i have of his mom'
    m' WE HAVE TO DO IT NOW !'
    'Shocked beyond belief, you realize they know the hacker\'s identity, confirming your theory that he is seeking revenge.'
    'They stop talking for a while'
    'What will you do now?'
    menu:
        'Keep hiding':
            jump KeepHiding1
        'Confront them holding your gun':
            jump ConfrontWithGun

label KeepHiding1:
    scene bg lookingkey with dissolve
    pause 0.01 
    "you observe Mark as he approaches the stairs and lifts the wooden piece in search of the key but he doesn\'t find it"
    "He checks his pockets, but it\'s not there either"
    "You silently hope that he has a spare key, but alas, he does not"
    scene bg mark with dissolve
    m"I can't find the damn key to open the drawer."
    scene bg charles with dissolve 
    f "Are you serious right now?"
    f "Maybe you changed the place where you hid it"
    scene bg mark with dissolve 
    m "No, I didn't. Even the code on the paper underneath the jar still says 'stairs'. If I had changed it, I would have changed its code for sure. I always do when I change it."
    scene bg charles with dissolve
    f "You don\'t have a spare key or something?"
    scene bg mark with dissolve
    m "No, I don't"
    m"I think somebody came down here and took it."
    scene bg charles with dissolve 
    f "What do you mean somebody?"
    f "WHAT DO YOU MEAN BY THAT?"
    scene bg mark with dissolve
    m "Hey, hey, stop stressing."
    scene bg charles with dissolve 
    f 'NO, NO, NO, we both know that this\'somebody\' is none othe than Elliot Delarson'
    f 'He\'s going to get us all locked behind bars for the rest of our lives'
    scene bg mark with dissolve 
    m "Yes, it could be him..."
    m "Shit! THE FILES."
    'They must be talking about the hacker, or we should now call him Elliot Delarson'
    scene bg charles with dissolve 
    f 'We have to check if he\'s still here'
    scene bg mark with dissolve 
    m 'You think he\'s still inside my house'
    f 'Yes it\'s possible'
    'You satrt feeling scarred as they might catch you while they\'re looking'
    scene bg lookingkey with dissolve 
    'You watch Mrk as he gets up the stairs to check the upstairs'
    'But charles doesn\'t follow him and instead he checks the basement'
    scene bg backdoor
    'He goes to the entrance of the back first and he chock it with his hand'
    f 'Shit we left this open'
    f 'Or maybe not us ...'
    'He now knows that the back entrance of the basemnt was used to get inside'
    'he checks under the bed'
    scene bg markyelling with dissolve 
    f 'MARK COME DOWN SOMEONE IS HERE !!!!!'
    'What are you gooing to do?'
    menu:
        'Reach for your gun':
            jump gungrab
        'Try to slide away drom underneath the bad and run':
            jump runfrombed

label gungrab:
    'You put you hand inside you pocket reaching for your gun but Mr. Charles holds you hand and doesn\'t let you move'
    'Mark comes runing down the basement stairs'
    'He grabs a syringe and he straik you in your hand with it all while your under the bed '
    jump TheFinalEnd


label runfrombed:
    'You glide to the opposite side of the hospital bed where you had concealed yourself, away from Mr. Charles presence.'
    'You rise to your feet, aiming the gun at him'
    scene bg handsup with dissolve
    'He puts his hand up'
    'Then you hear gun shot...' 
    scene black with dissolve 
    "You're overcome by an intense wave of pain radiating from your the erea between your left shoulder and your neck"
    scene bg gundropped with dissolve
    'You drop your gun '
    "Then you realised that you've been shot from behinde by Mark"
    scene bg markgun with dissolve 
    m 'Shit i missed it ! I WANTTED TO SHOOT HIM IN THE HEAD'
    scene bg charles with dissolve 
    f 'Oh well you saved my life there'
    'They laugh as your body drops in the ground. The pain worsens.'
    scene bg lacblood with dissolve 
    'Swimming in your own blod, you surrender to unconsciousness.'
    jump TheFinalEnd




label ConfrontWithGun:
    'You glide to the opposite side of the hospital bed where you had concealed yourself, away from the two men\'s presence.'
    scene bg holdgun with dissolve 
    'You rise to your feet, aiming the gun at them.'
    scene bg menpanic with dissolve 
    'They gasp and swiftly raise their hands in surrender.'
    f 'WHO ARE YOU!? HOW DID YOU GET IN!?'
    m 'WHAT DO YOU NEED FROM US!?'
    'What will you tell them?'
    menu:
        'Do as the hacker told you, and kill them':
            jump killBothOfThem
        'Ask them questions':
            jump QuestionTHEM


label leaveKey:
    scene bg underbed with dissolve
    pause 0.01 
    'You leave the key and quickly hide under the bed and from your vantage point, you can see both of their feet as they stand in the middle of the basement.'
    'You strain to hear their conversation.'
    f 'I\'M TELLING YOU MARK I\'M SURE IT\'S HIM!'
    f "HE WANTED TO GET REVANGE FOR SO LONG!"
    f "He\'s winning this time"
    scene bg sadface with dissolve 
    pause 0.01
    scene bg mark with dissolve
    m 'Look, I know he\'s the one behind all this, but we need to be careful now.'
    m'If he pulled shit like that on Krysa and then you...I must be next'
    m'We have to burn all the documents that i have of his mom'
    m' WE HAVE TO DO IT NOW !'
    scene bg underbed with dissolve 
    'Shocked beyond belief, you realize they know the hacker\'s identity, confirming your theory that he is seeking revenge.'
    'They stop talking for a while'
    scene bg lookingkey with dissolve 
    'You observe Mark as he approaches the stairs and lifts the wooden piece in search of the key but he doesn\'t find it.'
    'He checks his pockets, but it\'s not there either.'
    'You silently hope that he has a spare key, but alas, he does not'
    scene bg mark with dissolve
    m"I can't find the damn key to open the drawer"
    scene bg charles with dissolve 
    f 'Are you serious right now?'
    'He checks his pockets, but it\'s not there either'
    scene bg mark with dissolve
    m 'I can\'t find the damn key'
    scene bg charles with dissolve
    f 'Are you serious right now?'
    scene bg mark with dissolve
    m "Oh wait it's here ! i left it here last time"
    scene bg charles with dissolve
    f 'You scared me'
    'Mark believes he left it there'
    scene bg paperdesk with dissolve 
    "You need to intervene to stop him from burning those files."
    "How do you intend to prevent that from happening?"
    menu:
        'Get out of you hiden spot and confront them':
            jump ConfrontWithGun
        'Get out of you hidding spot and kill them both':
            jump killBothOfThem



label QuestionTHEM:
    'What questions do you intend to ask?'
    menu:
        'What activities do you engage in within this basement?':
            jump wedotheillegal
        'Who is the individual you are referring to?':
            jump TheTRUTH
        

label wedotheillegal:
    m 'Look we can talk in my livingroom upstairs and we will answer all your questions'
    f 'Yes we can explain everything this is not how it might seem it is '
    'They\'re trying to decive you but they don\'t know you\'ve seen the evidance'
    'What is your answer?'
    menu:
        'I\'ve seen everything just spell it out':
            jump iveSeenItAll
        'Ok let\'s go upstairs and talk':
            jump GoUpStairs

label iveSeenItAll:
    m 'You are going to regret this'
    f 'Elliot sent you am i right? He sent you to kill us. Haven\'t he done enough?!'
    'What are you going to respond?'
    menu:
        'Yes he sent me':
            jump ElliotSentMe
        'Tell me more about This Elliot guy':
            jump InfoAboutHacker

label ElliotSentMe:
    m 'We didn\'t kill his mother when is he going to uderstand that it wasn\'t our fault'
    'So you tell him to explain more about what happend to his mom'
    m 'So yo don\'t even know why the guy who sent you is doing all of this?'
    f 'He must\'ve payed him well'
    m 'In 2000 Elliot mom was very sick and she came to me for consultation. But i couldn\'t do anything for her. i tried my best but her cancer spread eveywhere'
    m 'She dead few days later'
    'What do you say?'
    menu:
        'Ask him about Elliot Mom name cuz maybe you\'ve seen it on one of the files':
            jump AskName
        'Beleive what Mark is saying':
            jump GoUpStairs


label InfoAboutHacker:
    "you step out of the shadows holding up your gun"
    m "who are you!"
    f " hey hey buddy stay calm let us exlain "
    " would you listen to them or kill them?"
    menu:
        "listen to them":
            jump listen1
        "kill them":
            jump killBothOfThem

label killBothOfThem:
    'You didn\'t hesitate; you fired at Mark immediately.'
    scene black with dissolve 
    pause 0.05 
    scene bg markdied with dissolve 
    'His body drops to the ground'
    scene bg charleshorri with dissolve 
    f 'NO DON\'T DO-  '
    scene bg charlesdied with dissolve
    'But you shoot him as well. His body drops to the ground'
    scene black with dissolve
    pause 0.05 
    scene bg policenight with dissolve
    'As you run away, the wail of police sirens pierces the air, echoing down the streets.'
    'It\'s the telltale sign that someone, likely a vigilant neighbor, has alerted the authorities to the gunfire.'
    'Panic grips you as you attempt to evade capture, but suddenly, you find yourself encircled by law enforcement, their commands sharp and urgent.'
    scene bg keep_trying with dissolve 
    p 'Stay perfectly still, don\'t make a move'
    'Before you know it, the cold metal of handcuffs clamps around your wrists sealing your fate.'
    'Now, confined in the back of the police car, the gravity of your situation hits you like a sledgehammer.'
    jump Continue4

label AskName:
    'You inquire about her name, but you\'re met with silence'
    'But then he says that her name was Elisabeth'
    'Elisabeth Delarson'
    'As the name resonates in your mind, you realize you\'ve encountered it before in the files.'
    'The revelation dawns upon you, they\'ve been deceiving you.'
    'What course of action will you take now?'
    menu:
        'Act like you believed them':
            jump act

 
label GoUpStairs:
    
    'As you all ascend from the basement together, settling into Mark\'s living room. Mr. Charles momentarily disappears from view, only to emerge from behind, striking your head with a heavy metal bar.'
    'Your consciousness fades...'
    jump TheFinalEnd



label TheFinalEnd:
    scene black with dissolve
    pause 0.5
    scene bg dirtybed
    'You wake up and you find yourself bound to the dirty hospital bed in the basement.'
    'The effects of drugs make it difficult to open your eyes or move.'
    scene bg sinister  with dissolve 
    'Through the haze, you discern Mark\'s grin as he brandishes a syringe, a sinister smile etched upon his face.'
    'He\'s going to make a bag out of your organs'
    jump end

label act:
    'You lower your gun and affirm your belief in their story.' 
    'They look at each other and then back at you'
    m 'Do you want to work with us instead?'
    'You agree because that\'s the only way for you to get out of this house safely now that you know the hacker\'s identity'
    'They promise you that they won\'t tell the police about you breaking in Mark\'s house'
    m 'You have to kill Elliot for us'
    m 'Instead of killing two innocent men, kill him!!'
    f 'You\'re a killer anyways...'
    'You reluctantly accept their proposition, finally departing the house armed with the hacker\'s identity.'
    'Before leaving, they provided you with the location of Elliot\'s workplace. It turend out that Elliot the hacker works in a software comapny called MYSOS, 30 min away from where you live'
    'And they also told you to meet with them in the basement after burrying his body'
    #MEETING THE HACKER   

# last day cofront hacker 
 
label Confronthacker:
    scene black with dissolve
    pause 0.5
    scene bg day7 with dissolve
    pause 2.0
 
    scene black with dissolve
    pause 0.05
    scene bg myroom with dissolve 
    user"Finally I can meet the person who tormented me all this week"
    "Suddenly your phone buzzes"
    scene glitshed with dissolve
    h"You are really getting on my last nerve, you know that, what do you not understand by I WANT THEM DEAD"
    h"Are you slow to not understand Such a simple Task"
    h"Tell me what is stopping me from Telling the Cops about your less than favorable past"
    "What will you to Him"
    menu :
        "I'm sorry, Please, it will be done by tommorow i swear it ":
            h"IT BETTER BE, tommorow is the last day of our first agreement"
            h"Think about it well today, will ya?"
            h"It's either you or them"
            h"Now then, GOOD LUCK"
        "I'm too scared to do it":
            h"EXCUSES... EXCUSES, Well you better get over that quickly"
            h"because after Tommorow, I simply will not have it in me to excuse your behaviour"
            h"Now then GOOD LUCK"
        "He hangs the phone"
    user"UGHH, This guy is THE WORST"    
    "You slam the phone on the ground,feeling a surge of frustration"
    "before deciding to call it a night, knowing you'll need every ounce of energy you can get for tomorrow."
    "You decide to meet him tommorow, As you spent the entire rest of the Day fantisizing about the look in his face when he realizes that his jig is up"
    "Next day..."
    scene black with dissolve
    pause 1.0
    scene bg day7 with dissolve
    pause 2.0
    scene black with dissolve
    scene bg hackerhouse with dissolve 
    "By the next day, You drive your car to the adress that Charles and Mark gave to you "
    "You count the hours until Elliot gets back to home from  work"
    "As the appointed time for your \'rendezvous\' draws near, you stealthily position yourself behind a bush near his house"
    "Suddenly you see a young guy approaching"
    #pas de photo 
    scene black 
    user"That must be HIM, I cannot believe that i was being bossed around by such a Youth, I'm so ashaimed..."
    "What will you do ?"
    menu:
        "Call out to him":
            jump caller
        "Wait until he opens the door and go behind him":
            jump Behind
        
label Behind:
    "You wait up for Elliot to open the door"
    "Then you swiftly go behind him, pointing you gun directly on his back"
    User"One word and You're dead keep moving"
    "You close up the door with your free hand as you walk into his house"
    E"So finally meet, you have my upmost congratulations for surviving this week [user]"
    jump talk

label caller:
    "Hey Bastard"
    "You say holding a gun to Elliot's head"
    "Elliot turns around"
    E"Well if it isn't [user]"
    E"Honestly didn't expect you to actually find me"
    E"You have trully exceded my expectations BRAVO"
    jump talk
label talk:   
    E"It must have been hell to you hasn't it ?"
    user"YEAH, you made my life a living hell"
    E"I'm sorry to hear that"
    E"I needed someone to exercice my vengence, and it just happened that you were unlucky enough"
    user"but WHY are you so hellbent on vengence"
    E"Well aren't you at least going to drop the gun before i tell you my sob story "
    menu:
        "I'd rather not":
            "Sorry but you see you aren't the most trust worthy person"
            E"huh, Undrestandable.."
            jump answer
        "drop the gun":
            "You take a deep breath and look at your gun"
            "huh,I'm really not cut up for this"
            jump answer
label answer:
    "well to answer your question"       
    E"I don't know why, ever since my mother was killed, I made avenging her my one true goal in life"
    E"I think by doing that i kinda went insane"
    E"i wouldn't say i regret the way i lived my life, because simply i do not know any other way"
    E"if you want to kill me, do so, because i have failed in my life"
    user"You do know it doesn't have to be like this right?"
    E"what ?"
    user"You are young and still got a whole life in front of you"
    user"Revenge is a vicious cycle that only breed more hatred"
    user"the real heroes are the one to break that cycle, not the ones who fuel it"
    user"What i'm getting at is, Let's team up, I promise you that we will bring those who killed your mother to justice"
    E"I'm not sure i would be satisfied with that, Justice failed me once, why should i trust it again"
    user"Trust me Elliot Justice is the only true way to handle these problems"
    user"your mother wouldn't have wanted you to live a life of revenge"
    E"I guess it wouldn't hurt to give it another go"
    user"Believe me you won't regret it, i have tons of evidences, from when i did the tasks to supply our case"

label fin:
    "Fast forward 2 months"
    scene bg n_a_Court_room_and_a_paper_of_the_judge_written with dissolve 
    "You and Elliot raise charges against krysa, Charles and Mark"
    "The Trio are found guilty with fraud, organ Traficking and first degree murder"
    "And are sentenced to life imprisonment"
    "You get back to your ordinary happy life, and Eliott seems to have founded a new life for himself as well"
    centered "GOOD END"
    centered "NEVER CLICK ON A LINK YOU DON'T KNOW AGAIN !"




label end:
        play sound "gameover.mp3"
        scene bg end with dissolve
        pause 0.1
        scene black with dissolve
        pause 0.1
        scene bg end with dissolve
        pause 0.1
        scene black with dissolve
        pause 0.1
        scene bg end with dissolve
        pause 0.1
        scene black with dissolve
        pause 0.1
        scene ended with dissolve
        pause 2.0
        scene ended with dissolve
        pause 2.0
        scene black with dissolve
        pause 2.5
        "Wait a minute..."
        scene black with dissolve
        pause 1.0
        scene glitshed with dissolve
        "It was dumb to make that choice, wasn't it?"
        "You didn't go to prison for the money you stole, but you'll go for a bad choice, poor [username], you make bad decisions to save your life"
        h "Well, [username] couldn't survive."
        scene glitshed2 with dissolve
        h "No matter, I'll just find another victim, hahahaha."
        scene black with dissolve
        pause 3.0
        return



return
