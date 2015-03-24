__author__ = 'jose'
# ======================================================================================================================
#Programmer : Jose Tobar
#Program Name: Assignment #08 - Creating and Searching an Array (While Loop version)
#Date Written: 3/1/2015
#======================================================================================================================
#initialize variables and array
def initializeVariables():
    global gpa;
    gpa = [];  #creates an empty array
    #end initializeVariables function


#======================================================================================================================
#populate gpa array with data
def createArray():
    global gpa;
    count = 0;

    while (count < 10):
        #the statement below is used to enter data via the keyboard/console, inside the array/list
        gpa.append(float(input("Enter GPA #" + format(count + 1, ">3") + format(" :==> ", ">6s"))));
        count = count + 1;
        #end of while loop
    #end of createArray function
#======================================================================================================================
#display results
def displayGpaList():
    count = 0;
    print();
    print("=" * 45);
    while (count < 10):
        print(format(format("GPA #", "5s") + format(count + 1, "<2"), "^7s") + format(" ===> ", "^5s") + format(gpa[count], "5.2f"));
        count = count + 1;
        #end of while loop
    print("=" * 45);
    print();
    #end of displayGpaList function
def searchGpa():
    global targetCount, targetGpa;
    count = 0;
    targetCount = 0;
    targetGpa = float(input("Enter target GPA search for: ==>"));

    while(count < 10):
        if(targetGpa == gpa[count]):
            targetCount = targetCount + 1;
        count = count + 1;
        #end if
    # #end while loop
#end of searchGpa function
def displaySearchResults():
    print();
    print("=" * 45);
    print("The target GPA " + "\"" + str(targetGpa) + "\"" + ", ocur(s)" + str(targetCount) + " time(s)");
    print("=" * 45);
#======================================================================================================================
initializeVariables();
createArray();
displayGpaList();
searchGpa();
displaySearchResults();
#======================================================================================================================
#END of program