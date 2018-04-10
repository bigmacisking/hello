
print("Welcome the the world of pick your own adventure")
print("The adventures you take are a result of your choice. You are responsible because you choose!  ")
print("After you make your choice, follow the instructions to see what happens to you next.")
print("Remember--you cannot go back! think carefully before you make a move! One ")
print("mistake can be your last....or it may lead you to fame and fortune!")
print("But first a few simple questions about your avatar. ")
print("")
print("")
print("")
race = input("Race of avatar? ")
print("")
gender = input("Gender of Avatar? ")
print("")
age = int(input("Age of your avatar? "))
print("")
Class = input("Class of avatar? ")

if race == "triton":
    print("Welcome guardian of the ocean")
elif race == "tortle":
    print("Welcome")
elif race == "orc":
    print("Welcome ugly")
elif race == "human":
    print("Welcome fleshy one")
elif race == "goblin":
    print("Welcome")
elif race == "gnome":
    print("Welcome little one")
elif race == "elf":
    print("Welcome pointy eared one")
elif race == "dwarf":
    print("Welcome little one")
else:
    print("No race selected")


if gender == "male":
    print("Hello Man your a")
elif gender == "female":
    print("Hey Girl your a")
else:
    print("Hi Weirdo your a")


if  age < 21:
    print("party animal")
elif age <31:
    print("middle aged adventurer")
elif age <41:
    print("getting on in age and experiance")
elif age <55:
    print("experianced adventurer")
else:
    print("You should retire from adventuring")


if  Class == "wizard":
    print("Welcome magic user")
elif Class == "warrior":
    print("May your enemies fear you")
elif Class == "tank":
    print("May your shield protect the innecent")
elif Class == "rouge":
    print("May you be swift in your travels")
elif Class == "healer":
    print("Go forth and save lives")
else:
    print("An undecided be who you want to be")

print("Let the adventure begain.......")
Print("You wake up in a strange room and can't remember how you got there.")
print("The last thing you remember was drinking ale at the local taven")
