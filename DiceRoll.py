from random import randrange
pntDiceTotal = 0

#How many dice to roll
intNumberOfDice = 10

#How many sides do the dice have
intNumberOfSides = 6

#Text Prompts
DiceIndicator = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Nineth", "Tenth", "Eleventh", "Tweleth"]

#RollDice - Each individual Dice
for i in range(intNumberOfDice):

    #Identify which dice number is being used. Add "Dice" at the end
    pntDiceName = DiceIndicator[i] + " Dice "

    #Generate a number between 1 and the max number of "intNumberOfSides"
    pntDiceValue = randrange(intNumberOfSides) + 1

    #Combine the two variables to generate what dice, and number rolled
    print("{0:>13} = {1:2.0f}".format(pntDiceName,pntDiceValue))

    #Add Current Dice Value to Total Number
    pntDiceTotal = pntDiceTotal + pntDiceValue

#Print Total Value of all the Die
print("{0:>13} = {1:2.0f}".format("TOTAL DICE ",pntDiceTotal))

