def WOPR():
    print """
Greetings Professor Falken,
    """
    print """Would you like to play a game?
    """
    
    answer = raw_input("Type 'yes' or 'no' and hit 'Enter'. ").lower()
    
    if answer == "no":
        print """
Have a good day then, Professor Falken.
        """
    
    elif answer == "yes":
        print """
Here are the games we can play. What sounds good?
        
    Chess
    Checkers
    Poker
    Fighter Combat
    Guerrilla Engagement
    Desert Warfare
    Air-To-Ground Actions
    Theaterwide Tactical Warfare
    Theaterwide Biotoxic and Chemical Warfare
        
    Global Thermonuclear War
        """
        
        def WOPR2():
        
            print """What game would you like to play?
            """
            
            answer2 = raw_input("Type the game you would like, and then hit 'Enter' ").lower()
        
            if answer2 == "chess":
                print """
Great!
                """
            elif answer2 == "checkers":
                print """
Great!
                """
            elif answer2 == "poker":
                print """
Great! Hopefully you'll hold onto your money a little better this time, Professor Falken!
                """
            elif answer2 == "fighter combat":
                print """
If you wish, Professor Falken.
                """
            elif answer2 == "guerrilla engagement":
                print """
Perhaps we choose the setting to be Afghanistan, Professor. The ultimate challenge.
                """
            elif answer2 == "desert warfare":
                print """
We have seen quite enough of Desert Warfare recently, sir. Perhaps something else?
                """
            elif answer2 == "air-to-ground actions":
                print """
The air wins; we've seen this game before, sir.
                """
            elif answer2 == "theaterwide tactical warfare":
                print """
Are you sure, Professor Falken?
                """
            elif answer2 == "theaterwide biotoxic and chemical warfare":
                print """
Have I enlightened you about WW1 and the intricacies of chlorine gas, Professor?
                """
            elif answer2 == "global thermonuclear war":
                print """
            
            
            Are you sure, Professor? Perhaps, a good game of chess instead. 
            I thought we learned last time; it's a strange game...




            The only way to win is not to play.
            
            
            
            
            
            
                """
        
            else:
                print """
Pardon, Professor?
                """
                WOPR2()
        WOPR2()
        
    else:
        print """
Try again.
        """
        WOPR()
WOPR()