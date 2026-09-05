from os import path
import random



gem = 0
gemList = []
# ------ Lists ----------------
aList = ["you crawl up the rocks and come across 3 different ways you can go", "after that you stumble upon a pickaxe and two other paths", "youre almost out of the cave now choose your final path"]
bList = ["you jump into the water and come across 3 different ways you can go", "after that you stumble upon a digging tool and two other paths", "youre almost out of the cave now choose your final path"]

# -----------------FUNCTIONS-----------------------------
def AorB(choice, path):
        if choice == "A":
                A(path)
                PathChoice("A", path)
        else:
                B(path)
                PathChoice("B", path)        
def A(path):
        if path == PathOne:
                print(aList[0])
        elif path == PathTwo:
                print(aList[1])
        else:
                print(aList[2])  
def B(path):
        if path == PathOne:
                print(bList[0])
        elif path == PathTwo:
                print(bList[1])
        else:
                print(bList[2])
def guessNumber():
        secret = random.randint(1,50)
        guess = int(input("guess a number between 1-50 and you may find a gem if you guess the number correctly"))
        guesses = 10
        while guess != secret and guesses > 0:
                if guesses == 1:
                        print("you ran out of guesses the number was", secret, "no gem for you")
                if guess > secret:
                        guesses = guesses - 1
                        print("No, lower. You have", guesses, "guesses left")
                elif guess < secret:
                        guesses= guesses - 1
                        print("No, Higher. You have", guesses, "guesses left")
                else:
                        guess = secret
                        guesses= guesses - 1
                        
                if guess != secret:            
                        guess = int(input("what number am i thinking of between 1 and 50"))
        if(guess == secret):                
                print("Correct! it took",10 - guesses, " guesses to find the secret number and you have found a gem!")
                gemList.append(1)               
        print("-_" * 10)                              
def PathChoice(choice, path):
    for i in path[choice]:
       print (i["one"], i["four"])
    pick = input("what do you choose")
    for v in path[choice]:
        if v["one"] == pick:
            print(v["two"])
            gemList.append(v["three"])
def gemCount(): 
       for i in gemList:
           global gem
           gem += i
def gemCheck():
        if gem >= 5:
            print("you have collected", gem, "gems which is enough gems to escape the cave")
        else:
            print("you have not collected enough gems to escape the cave ypu only collected", gem, "gems you need 5 gems to escape the cave")                     
def welcome():

        print("you were on a treasure hunt but accidentally fell into a cave now you must collect enough Gems to escape the cave")
        print("You Stand up and see a dangerous Cave animal you have two choices to escape ")
        print("A. escape by climbing the rocks")
        print("B. escape by jumping into the water")
def start ():
        name = input("Enter your name:")
        print("Hello", name)
        print("_-" * 10)
        welcome()
        Choice1 = input("What do you choose(A or B): ")

        print("_-" * 10)
        Choice1 = Choice1.upper()
        AorB(Choice1, PathOne)
        print("_-" * 10)
        guessNumber()
        print("A go to the sharp area or B go to the area of small creatures")
        choice2 = input("What do you choose(A or B): ")
        choice2 = choice2.upper()
        print("_-" * 10)
        AorB(choice2, PathTwo)
        print("you come across rocky stairs you can either go A up or B down")
        choice3 = input("What do you choose(A or B): ")
        choice3 = choice3.upper()
        print("_-" * 10)
        AorB(choice3, PathThree)
        print("_-" * 10)
        gemCount()
        gemCheck()            

#-----------------------DICTIONARIES-----------------------------    



PathOne = {
    "A" : [ 
            {"one" : "1", "two" : "while walking by the water you saw a gem now you have a gem", "three": 1, "four": "follow the river"}, 
            {"one" : "2", "two" : "you keep looking but no Gems are found", "three": 0, "four": "go into the glowing cave"},
            {"one" : "3", "two" : "while walking in the dark you see a glowing Gem!", "three": 1, "four": "go into the dark mysterious hole"} 
           ],
    "B" : [
            {"one" : "1", "two" : "while walking down the blue path you find a gem!", "three": 1, "four": "right to a blue looking path "}, 
            {"one" : "2", "two" : "you follow the path and dont find any gems", "three": 0, "four": "turn left to a dark path with glowing plants"},
            {"one" : "3", "two" : "you found 3 gems while digging! and a mysterious underground area you decide to explore", "three": 3, "four": "dig a hole"} 
        
    
    ],


}
PathTwo = {
    "A" : [ 
            {"one" : "1", "two" : "while mining for gems you find 2 gems and find a area you decide to explore", "three": 2, "four": "mine for gems"}, 
            {"one" : "2", "two" : "on the rocky path you stumble apon a Gem!", "three": 1, "four": "leave it and continue on forward to the rocky path"},
            {"one" : "3", "two" : "while walking in the dark you dont see any gems", "three": 0, "four": "turn right into a dark path"} 
           ],
    "B" : [
            {"one" : "1", "two" : "while walking down the blue path you find a gem!", "three": 1, "four": "right to a blue looking path "}, 
            {"one" : "2", "two" : "you follow the path and dont find any gems", "three": 0, "four": "turn left to a dark path with glowing plants"},
            {"one" : "3", "two" : "you found 3 gems while digging! and a mysterious underground area you decide to explore", "three": 3, "four": "dig a hole"} 
        
    
    ],

}
PathThree = {
    "A" : [ 
            {"one" : "1", "two" : "you find one final gem!", "three": 1, "four": "go forward"}, 
            {"one" : "2", "two" : "you dont find any more gems!", "three": 0, "four": "go up"},
            {"one" : "3", "two" : "you find one final gem!", "three": 1, "four": "go down"} 
           ],
    "B" : [
            {"one" : "1", "two" : "you find one final gem!", "three": 1, "four": "go forward"}, 
            {"one" : "2", "two" : "you find one final gem!", "three": 1, "four": "go left"},
            {"one" : "3", "two" : "you dont find any more gems!", "three": 0, "four": "go right"} 
        
    
    ],

}
#---------------Start the game----------------
start()


