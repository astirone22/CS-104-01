#Anthony Stirone
#CS 104 01
# Average Test Score Algorithm
average=0 
total=0
howManyEntered=0
#just gives us our base values
howMany=int(input("How many test scores would you like to average?"))
#givs us our howMany to run our while loop
while howManyEntered<howMany:
    testScore=int(input("Enter test score:"))
    total=total+testScore
    howManyEntered +=1
#The while loop is saying that while howManyEntered is less than the input we gave for howMany
    #we have to input a test score under the input of testScore
#In addition while we are inputting the values for testScore they are just adding to each other to give us the total
    #Lastly, for each input of test score it is adding one to howManyEntered, stopping when it gets to howMany input  

average = total/howMany
print("The average for the tests you entered is:",average)
