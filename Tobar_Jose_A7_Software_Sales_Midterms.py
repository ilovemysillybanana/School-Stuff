__author__ = 'jose'
# Author: Jose Tobar
# Purpose: The purpose of this program is for the user to be able to put in a set amount of packages and recieve an appropriate discount.
# Version: 1
#Date: 2/14/2014
def getData():
    global packageNumber;#not sure why this needs to be a global according to my ide
    packageNumber = float(input("Please input how many packages you'd like to make: "));
    #calls the determineDiscounts method with packageNumber as a parameter
    determineDiscounts(packageNumber);
#end of getData()
def initializeVariables():
    #global priceWithoutDiscount, priceWithDiscount, totalPrice, discountRate, discountAmount;
    discountRate = 0;
    priceWithoutDiscount = 0;
    priceWithDiscount = 0;
    priceWithDiscount = 0;
    totalPrice = 0;
    discountAmount = 0;
#end of initializeVariables()
def determineDiscounts(packageNumber):
    #our if statement that calculates the appropriate discount
    if(packageNumber >= 100):
        discountRate = 0.4;
    elif(packageNumber <= 99 and packageNumber >= 50):
        discountRate = 0.3;
    elif(packageNumber <= 49 and packageNumber >= 20):
        discountRate = 0.2;
    elif(packageNumber <=19 and packageNumber >= 10):
        discountRate = 0.1;
    else:
        discountRate = 0.0;
    #calls the calculateAmounts method with discountRate as a parameter
    calculateAmounts(discountRate);
#end of determineDiscounts
def calculateAmounts(discountRate):
    priceWithoutDiscount = packageNumber * 99.00;
    priceWithDiscount = priceWithoutDiscount - (priceWithoutDiscount * discountRate);
    discountAmount = priceWithoutDiscount - priceWithDiscount;
    totalPrice = priceWithoutDiscount - discountAmount;

    #print("Discount Rate: " + str(discountRate));
    #print("Price Without Discount = " + str(priceWithoutDiscount));
    #print("Price with discount = " + str(priceWithDiscount));
    #print("Discount amount" + str(discountAmount));
    #print("Total amount" + str(totalPrice));
    #calls the display results function with all our parameters
    displayResults(totalPrice, priceWithoutDiscount, priceWithDiscount, discountAmount);
#end of calculateAmounts()
def displayResults(totalPrice, priceWithoutDiscount, priceWithDiscount, discountAmount):
    print("\nSoftware package(s) purchased: " + str(packageNumber));
    print("\nTotal amount before discount: $" + str(round(priceWithoutDiscount,2)));
    print("\nTotal discount based on the number of software packages purchased: $" + str(round(priceWithoutDiscount-priceWithDiscount, 2)));
    print("\nTotal amount of the purchase after the discount: $" + str(round(totalPrice, 2)));
#end of displayResults()
#initializes variables
initializeVariables();
#asks the user for input
getData();
