############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.
#70pt
print "What temperature would you like to convert from Celsius to Fahrenheit?"
userInput = int(raw_input())
userInput = userInput * 9 / 5 + 32
print "This temperature is " + str(userInput) + " degrees Celsius."

#85pt
temperatureList = [102,98,96,101,100,99,103,97,98,105]
myList = []
for x in temperatureList:
    if x>100:
        myList.append(x)
print myList

#100pt
print "How many patients are there?"
userInput1 = int(raw_input())
for x in range(int(userInput1)):
    print "What's your temperature?"
    userInput2 = int(raw_input())
    print "Have you been sick in the last 24 hours?"
    userInput3 = raw_input()
    print "Have you been to West Africa recently?"
    userInput4 = raw_input()
    if userInput2 >= 102 and userInput4 == "Yes":
        print "EBOLA!!"
    else:
        print "no ebola......."
    if userInput2 > 100 or userInput3 == "Yes" and userInput4 == Yes:
        print ".....EBOLA!!!"
    else:
        print "no ebola........"