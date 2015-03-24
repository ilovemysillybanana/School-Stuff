__author__ = 'jose'
# ======================================================================================================================
#Programmer : Jose Tobar
#Program Name: Assignment #08 - Creating and Searching an Array (While Loop version)
#Date Written: 3/1/2015
#======================================================================================================================
#initialize variables and array
def initializeVariables():
    global gpa, howMany;
    gpa = [];
    print();
    howMany = int(input("How many GPA's do you wish to enter? "));
    print();
    #end of initialize variables functions
#======================================================================================================================
#populate gpa array with data
def createArray():
    globals();
    for count in range(0, howMany, 1):
        gpa.append(float(input("Enter GPA #" + format(count + 1, "<2") + format("==> ", ">5s"))));
        #end of for loop
    #end of createArray function
#======================================================================================================================
def displayGpaList():
    count = 0;
    print();
    print("=" * 45);
    for count in range(0, howMany, 1):
        print(format(format("GPA #", "5s") + format(count + 1, "<2"), "^7s") + format(" ===> ", "^5s") + format(gpa[count], "5.2f"));
        #endd of for loop
    print("=" * 45);
    print();
    #end of displayGpaList
#======================================================================================================================
def searchGpa():
    global targetCount, targetGpa;
    count = 0;
    targetCount = 0;
    print();
    targetGpa = float(input("Enter target GPA searching for: ==> "));

    for count in range(0, howMany, 1):
        if(targetGpa == gpa[count]):
            targetCount = targetCount + 1;
            #end if
        #end for loop
    #end searchGpa Function
#======================================================================================================================
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