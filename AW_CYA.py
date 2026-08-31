from os import path


name = input("Enter your name:")
gem = 0
aList = ["you crawl up the rocks and come across 3 different ways you can go", "after that you stumble upon a pickaxe and two other paths", "youre almost out of the cave now choose your final path"]
bList = ["you jump into the water and come across 3 different ways you can go", "after that you stumble upon a digging tool and two other paths", "youre almost out of the cave now choose your final path"]

print("Hello", name)
print("you were on a treasure hunt but accidentally fell into a cave now you must collect enough Gems to escape the cave")
print("You Stand up and see a dangerous Cave animal you have two choices to escape ")
print("A. escape by climbing the rocks")
print("B. escape by jumping into the water")
Choice1 = input("What do you choose(A or B): ")
Choice1 = Choice1.upper()
AorB(Choice1, PathOne)
print("A go to the sharp area or B go to the area of small creatures")
choice2 = input("What do you choose(A or B): ")
choice2 = choice2.upper()
AorB(choice2, PathTwo)
print("you come across rocky stairs you can either go A up or B down")
choice3 = input("What do you choose(A or B): ")
choice3 = choice3.upper()
AorB(choice3, PathThree)
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
    

        

                
def PathChoice(Choice, path):
    for i in path[choice]:
       print (i["one"], i["four"])
    pick = input("what do you choose")
    for v in path[choice]:
        if v["one"] == pick:
            print(v["two"])
            gem += v["three"]

            




    



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



