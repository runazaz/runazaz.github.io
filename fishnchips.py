#Fish and Chips | Text Game Demo
#build 0005
end = "Hello. Thanks for playing my game (or what you want to call it)."
print("Hello.")
print("Welcome to my game.")
print("You want to play it?")
enter = input("yes or no : ")
yes = "yes"
no = "no"
if enter == yes:
    beat = "beat"
    ask = "ask"
    print("So, you want to enter my game?")
    print("")
    print("Well. Do that.")
    print("I have some informations to you.")
    print("First, your progress isn't going to be saved.")
    print("Second, if there are bugs, don't worry. It will get fixed soon.")
    print("So, well. Let the adventure begin.")
    print("The world is yours.")
    print("Decide your Fate.")
    print("-----------------")
    print("Youre sitting in the Park and eating fish and chips.")
    print("Suddenly there comes an aggresive person called '000' and steals your chips.")
    print("What do you do?")
    print("If you beat 000, enter 'beat'")
    print("If you ask 000, enter 'ask'")
    firstdec = input("")
    if firstdec == "beat":
        beat001 = "beat001"
        clear001 = "clear001"
        run001 = "run001"
        print("You hit 000 with your strong arm.")
        print("He gives you your chips and runs away.")
        print("A random passerby called '001' saw that and is going to fight with you.")
        print("If you beat 001, enter 'beat001'")
        print("If you want to clear everything peacefully, enter 'clear001'.")
        print("If you run away, enter 'run001'")
        beatdec1 =  input("")
        if beatdec1 == "beat001":
            print("001 takes a gun out of his coat and shoots you.")
            print(end)
            pass
        if beatdec1 == "clear001":
            print("You try to calm down 001.")
            print("It doesn't work.")
            print("001 takes a gun out of his coat and shoots you.")
            print(end)
            pass
        if beatdec1 == "run001":
            print("You run out of the park.")
            print("001 chases you.")
            print("You run into your house.")
            print("001 calls the police.")
            print("You got arrested.")
            print(end)
        pass
    if firstdec == "ask":
        fac = "fac"
        ham = "ham"
        print("You ask 000 why he is stealing your chips.")
        print("He stuttered, and then he ran away.")
        print("You don't care anymore and you go to a shop to buy new fish and chips.")
        print("You have 5$ left.")
        print("You can buy fish and chips for 3$ or a hamburger for 3$ 50¢.")
        print("What are you going to buy?")
        print("If you buy fish and chips, enter 'fac'")
        print("If you buy the hamburger, enter 'ham'")
        food = input("")
        if food == "fac":
            print("You buy fish and chips from a seller called '002'.")
            print("It tastes very good with chips.")
            print(end)
            pass
        if food == "ham":
            beat000 = "beat000"
            run000 = "run000"
            print("You buy a hamburger from a seller called '002'")
            print("You can feel the fatness in your blood")
            print("Very suddenly 000 comes back to you and tries to steal your hamburger.")
            print("What do you do?")
            print("If you beat him, enter 'beat000'")
            print("If you run away, enter 'run000'")
            returnof000 = input("")
            if returnof000 == "beat000":
                print("You hit 000 with your strong arms.")
                print("A random officer called '003' saw that and catches 000.")
                print("Then 003 tackles 000.")
                print("This attack was very effective!")
                print("000 was defeated!")
                print("003 gets 166 experience points!")
                print("Have a look! 003 is developing into MEGA 003!")
                print("Do you want to nickname 003?")
                print("Well, you don't.")
                print(end)
                pass
            if returnof000 == "run000":
                cybermoney = "cybermoney"
                blogblog = "blogblog"
                print("You run away.")
                print("000 follows you.")
                print("You run into your house.")
                print("He tries to break the front door")
                print("The front door brakes.")
                print("You can see, that 000 wants to kill you.")
                print("Before he gets to kill you, an officer called '003' shoots at 000.")
                print("He died.")
                print("You survived.")
                print("Youre entering your house.")
                print("When you're in there, you sit to your computer.")
                print("If you log in to your bank account, enter 'cybermoney'")
                print("If you write a blog entry about what happened, enter 'blogblog'")
                pcplayer = input("")
                if pcplayer == "cybermoney":
                    banana = "banana"
                    bank_data = "US4623", "378584", 540.389, 7,16,21
                    bank_string = "Hello, welcome to jajageil Bank, %s%s. You have %f$ left. Your bank account is usable till %d/%d/%d."
                    login_data = "US4623", "378584"
                    login_string_1 = "> player@game1337:~$ cd jjg_bank"
                    login_string_2 = "> player@game1337:~/jjg_bank$ ./jjg_bank -l -p"
                    login_string_3 = "> Enter Password for %s%s, please."
                    print(login_string_1)
                    print(login_string_2)
                    print(login_string_3 % login_data)
                    #Tip, the password is banana!
                    login_bank = input("Password: ")
                    if login_bank == "banana":
                        exit = "exit"
                        print(bank_string % bank_data)
                        print("Hello. Thanks for playing my game!")
                        print("I hope you liked it :3")
                        print("Type 'exit' to exit this game!")
                        if lastdec == "exit":
                            print("Bye.")
                            pass
                        pass
                    pass
                if pcplayer == "blogblog":
                    exit = "exit"
                    print("> player@game1337:~$ cd blog")
                    print("> player@game1337:~/blog$ ./blog")
                    print("20 overrated hours of writing later...")
                    print("You wrote your blog entry.")
                    print("It's live now.")
                    print("What do you do now?")
                    print("If you end this game, enter 'exit'.")
                    lastdec = input("")
                    if lastdec == "exit":
                        print("Bye.")
                        pass
                    pass
                pass
            pass
        pass
    pass
if enter == no:
    Bye = "Okay, bye."
    print(Bye)
    pass
