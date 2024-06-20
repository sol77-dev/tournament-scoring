# The menu to select the program option from
def menu():
    print('''
    \nTournament Score Input Program.
    Would you like to:
    1. View tournament information 
    2. Input scores 
    3. View individual scores
    4. View team scores
    5. Exit the program
    (please enter just the number of your selection)
    ''')

# Allows for input of all variables needed for calculations 
def input_scores():
# Check whether the scores are being inputted on behalf of a team or individual 
    choice = input("Are you entering the scoring for a team or individual? ")
    choice = choice.lower()
    # If team, write to team scores.txt 
    if choice == "team":
        # Counts how many lines are in the team scores file
        with open("team scores.txt", "r") as f:
            num = len(f.readlines())
        # Checks if the limit has been met already; 4 teams maximum (5 specified to accomodate for the heading line)
        if num >= 5:
            print("Unfortunately, the maximum number of teams has been reached")
            #kills the program 
            exit()
        else:
            #input name of the team 
            name = input("Please enter the name of the team: ")

    # If individual, write to individual scores.txt
    elif choice == "individual":
        with open("individual scores.txt", "r") as f:
            num = len(f.readlines())
        if num >=21:
            print("Unfortunately, the maximum number of individual participants has been reached")
            exit() 
        else:
            name = input("Please enter the name of the individual: ")

    # If something else was entered besides the accepted responses, the program forcibly ends 
    else:
        print("that was not one of the options, please try again")
        exit()

    # Creates a list to append all the scores to 
    results = ["\n" , name]
    # Establish total score variable
    totalscore = 0 

    # Loops score input 5 times for each of the 5 events 
    for i in range(5): 
        event = input("Did the participant(s) take part in event number " + str(i+1) + "? ")
        event = event.lower()
        # If participant took part in that event
        if event == "yes":
            #input score from the event
            score = int(input("What was the participants score out of 10? "))
            #add it to total score
            totalscore = +score 
            #append event score to results list
            results.append(" || event " + str(i+1) + ":" + " " + str(score))
        # If participant didnt take part in that event
        elif event == "no":
            #appened 'N/A' in place of a score
            results.append(" || event " + str(i+1) + ": N/A")
    
    # Appends total score to the results
    results.append(" || total: " + str(totalscore))

    # Joins each of the list items into a string
    finalresults = ''.join(results)

    # Outputs all of the results
    print("Here are the participants results:") 
    print(finalresults)

    # If earlier 'team' was chosen, results are appended to the team scores file
    if choice == "team":
        with open("team scores.txt", "a") as f:
            f.write(finalresults)

    # If earlier 'individual' was chosen, results are appended to the individual scores file 
    elif choice == "individual":
        with open("individual scores.txt", "a") as f:
            f.write(finalresults)

# Sets the information for the event description
def info():
    print('''
\nEvents:

There are 5 events. These are:
    1. Spelling
    2. Maths
    3. Trivia
    4. Throwing
    5. Sprinting

Each event has 10 rounds, gradually increasing in difficulty.
Scores are determined based upon the participants ranking.
''')


# Sets the continuation variable to true 
cont = True

# Loops until the continuation variable is changed 
while cont == True:
    menu()
    choice1 = input()
    if choice1 == "1":
        info()
    elif choice1 == "2": 
        input_scores()
    elif choice1 == "3":
        print("")
        with open("individual scores.txt", "r") as f:
            print(f.read())
    elif choice1 == "4":
        print("")
        with open("team scores.txt", "r") as f:
            print(f.read())
    elif choice1 == "5":
        print("Exiting program.")
        cont = False
