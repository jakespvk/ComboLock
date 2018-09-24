# set constant position zero
POSITION_ZERO = 0

# get correct numbers from user
number1 = int(input("What is the first number? "))
number2 = int(input("What is the second number? "))
number3 = int(input("What is the third number? "))

# set up correct boolean
correct = "false"

# set up while loop so that while the correct condition is false, code will repeat
while (correct != "true"):
     # ask user for number of ticks in direction
     ticks1 = int(input("How many ticks clockwise? "))
     ticks2 = int(input("How many ticks counterclockwise? "))
     ticks3 = int(input("How many ticks clockwise? "))

     # set position to zero
     position = POSITION_ZERO

     # set correct to true by default
     correct = "true"

     # do calculations/movement and check correctness, if incorrect set to false and re execute code
     position = 40 - ticks1
     if (position == number1):
          position = position + ticks2
          if (position > 40):
               position = position - 40
          if (position == number2):
               if (ticks3 > position):
                    ticks3 = 40 - ticks3
                    position = position + ticks3
                    if (position == number3):
                         print("Yay!! You unlocked a Disney cruise with all your Smash Bros!!")
                    else:
                         correct = "false"
                         print("Your combo was incorrect, please try again.")
               elif (ticks3 <= position):
                    position = position - ticks3
                    if (position == number3):
                         print("Yay!! You unlocked a Disney cruise with all your Smash Bros!!")
                    else:
                         correct = "false"
                         print("Your combo was incorrect, please try again.")
               else:
                    correct = "false"
                    print("Your combo was incorrect, please try again.")
          else:
               correct = "false"
               print("Your combo was incorrect, please try again.")
     else:
          correct = "false"
          print("Your combo was incorrect, please try again.")


# Research questions: 64,000 possible combinations; 192,000 seconds; 1,000,000 different possible combinations, the 6 number combo would be more unbreakable.
