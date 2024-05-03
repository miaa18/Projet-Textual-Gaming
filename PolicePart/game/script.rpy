#Police part
define h =Character("Hacker", color="#bd1313")
label start :
label intro:
    'You were casually sifting through your emails when one caught your eye..'
    ' It appeared innocent enough, showcasing the profile photo of an old comrade from your military days, reaching out to catch up and sharing their social media link. Nostalgia swept over you, and without a second thought, you clicked on the link. However, instead of redirecting you to a familiar social media page, your screen flickered, and an app began downloading automatically. Cursing under your breath, you realized you had been hacked!'
    'Then, a voice, heavily distorted yet oddly playful, emanated from your computer'
label into2:#red 
    
    h "Well, well, well, what do we have here?\" the voice taunted\"Seems our retired military friend has stumbled into quite the predicament. A hefty sum of 200 million sitting pretty in your account. Quite the windfall, wouldn't you say?" 
    menu:
        #green text !!!
        'Who are you, and what do you want from me?':
            jump intro3
label intro3: #hacker red 
    h "Oh, come on now, no need for introductions. Let's just say I'm someone who likes a good game. How about a little deal? I'll send over a list of targets for you to take out, just for kicks."
    menu: #greeen
        'but why? What\'s the point of all this?':
            jump intro4
label intro4: #reed
    h "Ah, where's the fun in explaining? Let's just say it's a little experiment of mine"
    h "And oh, by the way, you've got a week to play along. Your countdown starts tomorrow at 7:00 PM sharp!"

label startPlay:
    # play music discrepancy_preview loop 
    scene bg pc_on_desk
    "After enduring the most harrowing nightmare of your life, your computer screen returns to its usual state. What prudent action will you take next?"
    
    menu:
        "Go to the police":
            jump choice1
        "Wait for the countdown to start tomorrow at 7:00 pm":
            jump choice2

label choice1:
    scene bg looking_phone 
    "You\'re inside you car On you\'re way to the police station, you receive a text message on your phone from an unknown number. The message warns,\'If you set foot in the police station, I\'ll provide them with evidence of the illegal money transfers. What course of action do you take next?"
    menu:
        "Ignore the text and keep going":
            jump PoliceStation
        "Text them back":
            jump TextThemBack
        "Take a step back and instead wait for the countdown to start tommorow at 7:00 pm":
            jump choice2


label TextThemBack:
    "You stop in the middle of the street, more furious than ever, you enter the chat on your phone with the unknown sender. What message do you type?"
    menu:
        "You prick ! i\'m not scared of you":
            jump UnavailableSender

        "How do you know where i am??? Are you following me?!":
            jump LookingAround

label UnavailableSender:
    "Your phone alerts you that your text message cannot be sent because the intended recipient does not exist. What would you like to do next?"
    menu:
        "Take  a setp back and go back home and wait": 
            jump choice2
        "Proceed on your way to the police" :
            jump PoliceStation

label LookingAround:
    scene bg choice_escape1
    "You exit your car, slamming the door shut, and begin to spin around in paranoid circles, scanning for any distant figures that might be observing you.Where do you wanna look?"
    menu:
        "Left":
            jump Left
        "Right":
            jump Right
        'Behind':
            jump Behind
label Left:
    scene bg street_with_a_few_people_looking_and_a_few_looking
    'To the left, the street is hive of activity, with buildings lining either side, their facades varying from sleek modern designs to weathered brick structures ,The bustling street is like a lively symphony of motion  with cars, buses, and bicycles weaving through the traffic as pedestrians navigate the sidewalks. Nothing seems suspicious.'
    menu:
        'Look in the other directions' :
            jump Directions 
label Right:
    scene bg small_nice_town_houses_aligned
    'To your right, you find a gently winding cobblestone path, leading up to a tranquil hillside town. The path is hugged by vibrant green bushes and the occasional splash of wildflowers that sway gently in the breeze. Ahead, the town emerges with a warm and inviting aura. The houses, painted in soft pastels, boast sun-kissed, terra cotta roofs and weathered wooden doors, suggesting years of stories and history within their walls'
    menu:
        'Look in the other directions':
            jump Directions 
label Behind:
    scene bg black_car_behind
    'Behind you, a sleek black car, guided by a man appearing to be in his thirties. The pathway is cocooned between two majestic lines of trees. On either side of the road stand townhouses, each their gardens. Amidst this serene scene, a woman leisurely strolls with her furry companion, the dog\'s tail wagging joyously as they explore the tranquil surroundings.' 
    menu:
        'Look in the other directions':
            jump Directions
        'Head over and have a conversation with the individual in the car, they seem suspicious':
            jump TalkingWithCarGuy

label Directions:
    scene bg choice_escape1 
    menu:
        'Left':
            jump Left
        'Right':
            jump Right
        'Behind':  
            jump Behind

label TalkingWithCarGuy:
    scene bg talking_with_car_guy
    'As you approach the car, the man inside rolls down his window. What message do you intend to convey to him?'
    menu:
        'Are you following me ???':
            jump Question

label Question:
    'The man in the car gazes at you, a confused expression crossing his face and he says: "Following you? I don\'t even know you, man!".What will you respond?'
    menu:
        "Excuse me sir,  i'm just being paranoid !":
            jump BackToCar
        "Stop lying you ugly rat!":
            jump badgeReveal

label badgeReveal:
    scene bg badge_reveal 
    'The man angrily exits his car, slamming the door shut, and abruptly thrusts a small wallet in your face. To your surprise, it\'s a police officer badge! He then begins questioning you about your identity.'
    menu:
        'Respond to his questions':
            jump Questions
        'Try to escape':
            jump Escaping
label Questions:
    'You choose to respond to the police officer\'s questions. What is your answer?'
    menu:
        "Officer, I apologize if I\'ve caused any trouble. I misunderstood the situation, i thought you were someone else. My name is *Your Name* and i live in Rivendell city":
            jump FreeToGo

label FreeToGo:
    scene bg free_to_go 
    'The police officer gives you a serious warning about unfounded accusations in the future. He informs you that he has noted your name and will conduct a brief investigation to ensure you\'re not involved in any suspicious activity.'
    menu:
        'Thank him and get back to your car':
            jump BackToCar

    
label Escaping:
    'As you contemplate the best direction to evade the police man, which path do you ultimately choose to take?'
    menu:
        'Go left':
            jump choiceEscape1
        'Go right': 
            jump choiceEscape2
        'Look around before runing':
            jump Directions1



label choiceEscape1:
    scene bg escape_choice1
    'Choosing to evade the police, you turn left into the bustling city streets, dodging between cars and buses. The scent of exhaust mixes with the aroma of street food as you disappear into the crowd. Suddenly, after just five minutes of running, the loud wail of police sirens reaches your ears!'
    menu:#REMOVE CONTINUE ANS USE JUST A CLICK OR ENTER INSTEAD
        'Continue':
            jump Continue

label Continue:
    'Panic sets in as you realize the authorities are closing in. Desperation drives you to move faster, but in your haste, you collide with pedestrians with every step you take adding to the chaos while drawing more attention to yourself. What is you next move?'
    menu:
        'Keep running':
            jump KeepRuning 
        'Avoid the public by running towards a secluded rural area':
            jump TheRural

label KeepRuning:
    scene bg keep_running 
    'As you continue running, a police vehicle approaches from one direction, while another closes in from behind. You watch as the officers step out of their cars shouting "Stay still, don\'t move!\" \"Put your hands up!!.\". There seems to be no escape now. What do you wanna do ?'
    menu: 
        'Keep Trying':
            jump KeepTrying 
        'Give up':
            jump GiveUp
label KeepTrying:
    scene bg keeptrying
    'You are surounded and guns are directed at you. Where do you choose to escape this police Besieged?'
    menu: 
        'You rush into the building to your left':
            jump ArtGallery
        'Run backwords':
            jump RunBack
label ArtGallery:
    #photo
    'As you desperately seek refuge, you spot an open door to a nearby building and rush inside. The dimly lit interior reveals white walls adorned with strange paintings and sculptures, hinting that you\'ve stumbled into an art gallery. But before you can take another step, a searing pain shoots through your knee, sending you crashing to the ground. The echo of a gunshot fills the hallway, and you realize with horror that you\'ve been hit. Darkness envelops you as the harsh reality sinks in: your escape attempt has ended in tragedy.'  
    jump YouLost
label RunBack:
    scene bg street_people_walk_and_police
    'As you frantically run backward, hoping to evade the pursuing officers, you unexpectedly stumble upon a group of additional police officers blocking your path. Before you can react, one of the officers swiftly grabs your hands, wrenching you off balance and causing you to fall to the ground. The world spins around you and with one final gasp, you succumb to unconsciousness, the events of the chase fading into oblivion'
    jump YouLost    

label GiveUp:    
    'As you give in, a police officer\'s voice cuts through the air, commanding you to get on the ground. With a heavy heart, you comply, dropping to the pavement as instructed. The cold surface presses against your palms as you acknowledge defeat, surrounded by the watchful eyes of bystanders. Soon, strong hands pull you up and guide you into the back of a waiting police car Soon, strong hands pull you up and guide you into the back of a waiting police car while the click of handcuffs signaling your capture. Groups of people gather, their murmurs blending with the noise of the sirens. '
    jump YOULost

label Directions1:
    menu : 
        'Left':
            jump Left1 
        'Right':
            jump Right1

label Left1:    
    scene bg street_with_people_walking
    ' To the left, the street is hive of activity, with buildings lining either side, their facades varying from sleek modern designs to weathered brick structures ,The bustling street is like a lively symphony of motion  with cars, buses, and bicycles weaving through the traffic as pedestrians navigate the sidewalks. '
    menu:
        'choose to run Left':
            jump choiceEscape1
label Right1:
    #photo
    'To your right, you find a gently winding cobblestone path, leading up to a tranquil hillside town. The path is hugged by vibrant green bushes and the occasional splash of wildflowers that sway gently in the breeze. Ahead, the town emerges with a warm and inviting aura. The houses, painted in soft pastels, boast sun-kissed, terra cotta roofs and weathered wooden doors, suggesting years of stories and history within their walls'
    menu:
        'choose to run Right' :
            jump choiceEscape2

label BackToCar:
    scene bg car_from_the_drivers_view_the_wheel
    'You compose yourself and get into your car, slamming the door shut. You pause for a moment before starting the engine, pondering who the hacker could be? and how does he know your location? You wonder whether you should continue to the police station or wait to see what unfolds tomorrow. What do you think you should do next?'
    menu:
        'Go to the police station and tell them everything':
            jump PoliceStation
        'Go back home and wait for what tommorow holds':
            jump choice2 


label TheRural:
    scene bg the_rural 

label choiceEscape2:



label PoliceStation:
    scene bg twopolices
    'You\'ve just stepped into the police station. To your right, two officers are chatting casually, one of them is holding a cup of steaming coffee.'
    jump Continue1
label Continue1:
    'Ahead of you, a man in a suit briskly walks from the right to the left side of the station. He then ascends the stairs and disappears from view'
    jump Continue2
label Continue2:
    scene bg lady_sitting_at_her_desk_police-removebg
    
    'You walk straight to a lady sitting at her desk, she appears to be conversing on the phone. You attempt to speak to her, but she gestures with her hand, indicating for you to wait. "One moment, sir," she mouths, focusing on her call. Where are you waiting untill she finishes?'   
    menu:
        'You take a seat on a nearby chair, positioned conveniently by the staircase':
            jump Sitting  
        'You stand near to the exit door and wait'  :
            jump Standing 

label Sitting:
    'You sit on hard plastic chair, trying to blend into the background. The lady hangs up and makes a discreet hand signal to a nearby officer. You watch, your pulse quickening, as they engage in a brief, hushed conversation, occasionally glancing at a computer screen and then back at you'
    jump Continue3
label Continue3:
    'The air feels thick as the officer ends the conversation and starts walking towards you with deliberate steps. While reaching into his back pocket, which appears to contain handcuffs, he says, "Hey buddy,  just stay right where you are. I have a few questions for you." as he approaches. What are you doing next?'
    menu:
        'Stay still':
            jump StayStill
        'Run up the staircases':
            jump Staircases
        'Run to the entry door of the police station where the othe officer is standing':
            jump dashDoor

label StayStill:
    'You straighten your jacket and sit up tall, maintaining a composed and confident demeanor. You look the officer in the eye, ready to respond clearly and assertively. What do you say to the officer?'
    menu:
        'Let him ask you the questions without saying anything' :
            jump nothing 
        'Hi sir and tell him why you came here in the fisrt place':   
            jump HiSir
        'Ask him if you are in trouble because him reaching out to handcuffs worried you' :
            jump InTrouble

label nothing:
    'The police officer\'s voice pierces the heavy silence, his tone firm as he commands,"Stand up." As you rise, he expertly secures the handcuffs around your wrists. While he does this, he begins to question you. It\'s clear from his pointed questions that he already knows far more about you than you expected. After confirming your identity, he recites  with a practiced clarity: "You have the right to remain silent. Anything you say can and will be used against you in a court of law. You have the right to consult with a lawyer and have that lawyer present during any questioning." His voice, steady and authoritative, leaves no room for doubt or negotiation as you process the gravity of the situation.'
    menu:
        'Why am i being arrested ?':
            jump WhyArrested 
label WhyArrested:
    'He informs you gravely that you have been implicated in an illegal money transfer originating from a military base. He explains that the station has recently received compelling evidence that links you to the crime. His voice is stern and the look in his eyes serious as he details the steps that will follow. You will be detained at the station, held in custody until a thorough investigation can unravel the truth behind these accusations'
    jump Continue4
label Continue4:
    'You find yourself confined within the stark walls of the interrogation room, the gravity of your situation becoming painfully clear. With nowhere to escape, you realize you\'ve been caught; the hacker has not only invaded your life but has exposed your deepest secret, turning your world upside down'      
    jump YouLost

label HiSir:
    'You tell him all about the hacker and the messages he sent you'
    jump next1

label next1:  #not finished 
label InTrouble: #not finished 
label Staircases: #not finished 
label dashDoor: # not finished 
label Standing: #not finished
label choice2:
label YouLost :  #don't forget return to quit
