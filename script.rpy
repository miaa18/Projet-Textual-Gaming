
label start:
    #this starts the game 
    #intro
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
