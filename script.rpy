
label start:
    #this starts the game 
    #intro
    "you were casually sifting through your emails when one caught your eye. It appeared innocent enough"
    "showcasing the profile photo of an old comrade from your military days"
    "reaching out to catch up and sharing their social media link."
    "Nostalgia swept over you, and without a second thought, you clicked on the link."
    "However, instead of redirecting you to a familiar social media page"
    "your screen flickered..."
    "an app began downloading automatically..."
    "Cursing under your breath, you realized you had been hacked"
    "Then, a voice, heavily distorted yet oddly playful, emanated from your computer."
    "Well, well, well, what do we have here?"
    "Seems our ex-military friend has stumbled into quite the situation!"
    "You are sitting on 200 mil stolen cash in your bank accounts."
    "Gotta say I'm impressed!"
    "the screen flashed with files of your past malpractices, information you thought was buried deep..."
    "This wasn't just a random attack - the hacker knew about your past"
    menu menu2:
        set action
        "How did you find these files?":
            "Unknown" "{color=#f00}Oh, let's just say I have my ways. The important thing is that they're in my possession now."
            jump menu2

        "Who are you, and what do you want from me?":
            "Unknown" "{color=#f00}Oh, come on now, no need for introductions.{/color}"
            "Unknown" "{color=#f00}Let's just say I'm someone who likes a good game.{/color}"
            "Unknown" "{color=#f00}How about a little deal? I'll send over a list of Tasks for you to take out, just for kicks.{/color}"
            "Unknown" "{color=#f00}If you nail them, your shady past will be our little secret{/color}"
            jump menu2

        "But why? What's the point of all this?":
            "Unknown" "Ah, where's the fun in explaining?"
            "Unknown" "Let's just say it is a little experiment of mine."
            "Unknown" "And oh, by the way, you've got a week to play along. Your countdown starts tomorrow at 7:00 PM sharp!"
            jump menu2
    #chapter1
    #chapter2
    #chapter3
    #end

#HERE WE DEFINE THE CHARACTERS

define user=Character("[username]",color="#1613bd")



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



return
