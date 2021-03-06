#Author: Jose Tobar
#Program Name: Variables and Calculations
#Purpose: The purpose of this program is for the user to input the name of a student
#Then input their test scores and get the total points earned as well as their test average
#Feburary 1, 2015


strUserName = input("Please input your full name: ");
doubleTestOne = float(input("Please Input your first test score: "));
doubleTestTwo = float(input("Please input your second test score: "));
doubleTestThree = float(input("Please Input your third test score: "));
doubleTestFour = float(input("Please Input your fourth test score: ")); 
doubleTestFive = float(input("Please Input your fifth test score: "));

#Calculate Total points earned.
doubleSumofTests = doubleTestOne + doubleTestTwo + doubleTestThree + doubleTestFour + doubleTestFive;
#Calculating the average using doubleSumofTests(the variable which holds the points earned n the tests) divided by the total number of tests
doubleTestAverage = doubleSumofTests/5;

#Here is where we display all the information to the user using format to make sure everything shows up nice and clean
print("The Student's Name is: " + strUserName + "\n" + 
      "-"*60 +
      "\nTest one: " + format(doubleTestOne, "6.2f") +"%" + 
      "\nTest Two: " + format(doubleTestTwo, "6.2f") + "%"+ 
      "\nTest Three: " + format(doubleTestThree, "6.2f") +"%" + 
      "\nTest Four: " + format(doubleTestFour, "6.2f") +"%" + 
      "\nTest Five: " + format(doubleTestFive, "6.2f") + "%\n" +
      "-"*60 +
      "\nThe sum of all the test scores is: " + format(doubleSumofTests, "7.2f") +
      "\nThe average of the test scores is: " + format(doubleTestAverage, "7.2f") + "%");
