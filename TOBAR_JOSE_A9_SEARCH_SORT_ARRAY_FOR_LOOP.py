__author__ = 'jose'
# ======================================================================================================================
#Programmer : Jose Tobar
#Program Name: Assignment #08 - Creating and Searching an Array (FOR Loop version)
#Date Written: 3/1/2015
#======================================================================================================================
#initialize variables and array
def initializeVariables():
    global gpa, howMany;
    gpa = [0.00] * 100;  #initializes 101 memory locations to the value of 0.00
    print();
    howMany = int(input("How many GPA's will be read/processed? "));
    print();
    #end of intitializevariables function
#======================================================================================================================
#populate gpa array with data using a text data file
def createArray():
    global gpa;
    count = 0;  # lcv/index -local variable within the scope of this function
    inFile = open("studentGPA.txt", "r");  #in file is a variable name from programmer
    for count in range(0, howMany, 1):#  #test lcv
        line = inFile.readline();  #read entire line inside the data file
        line = line.strip();  #remove all blank spaces from line
        gpa[count] = float(line);  #move value into gpa array with data type float
        count = count + 1;  #updating lcv
        #end for loop
    inFile.close();
    #end of createArray function
#======================================================================================================================
def displayGpaList():
    count = 0;
    outFile.write("UNSORTED GPA LIST" + "\n");  #writes the label/ttiel
    outFile.write("=" * 25 + "\n");
    for count in range (0, howMany, 1):
        outFile.write(format(format("GPA #", "5s") + format(count + 1, "<2"), "^7s") + format(" ===> ", "^5s") + format(gpa[count], "5.2f") + "\n");
        count = count + 1;
        #end of for loop
    outFile.write("=" * 25 + "\n");
    outFile.write("\n");
    #end of display gpa list function
#======================================================================================================================
def searchGpa():
    global targetCount, targetGpa;
    count = 0;
    targetCount = 0;
    targetGpa = float(input("Enter target GPA searching for "));
    for count in range(0, howMany, 1):
        if (targetGpa == gpa[count]):
            targetCount = targetCount +1; #counter
        count = count + 1;
        #end if
    #end while
    #end searchGPA
#======================================================================================================================
def displaySearchResults():
    outFile.write("\n");
    outFile.write("=" * 70 + "\n");
    outFile.write("The target GPA " + "\"" + str(targetGpa) +"\"" + ", occur(s) " + str(targetCount) + " time(s)" + "\n");
    outFile.write("=" * 70 + "\n");
    #end display search results function
#======================================================================================================================
def sortGpaArray():
    passCount = 0;
    swap = 0;
    tempGpa = 0;
    for passCount in range(0, howMany - 1, 1):
        for swap in range(0, howMany - 1, 1):
            if(gpa[swap] > gpa[swap + 1]):
                tempGpa = gpa[swap]
                gpa[swap] = gpa[swap +1];
                gpa[swap + 1] = tempGpa;
                #end if
            #end for loop swap
        #end for loop passcount
    #end sort gpa array
#======================================================================================================================
#display sorted gpa list
def displaySortGpaList():
    count = 0;
    outFile.write("SORTED GPA LIST" + "\n"); #writes and centers the label title
    outFile.write("=" * 25 + "\n");
    for count in range(0, howMany, 1):
        outFile.write(format(format("GPA #", "5s") + format(count + 1, "<2"), "^7s") + format(" ==> ", "^5s") + format(gpa[count], "5.2f") + "\n");
        count = count + 1;
        #end of for loop
    outFile.write("=" * 25 + "\n");
    outFile.write("\n");
    #end of display
#======================================================================================================================
#display student ainformation
def studentInfo():
    outFile.write("\n");
    outFile.write("=" * 70 + "\n");
    outFile.write("Assignment #09 - Created and executed by Jose Tobar \n");
    outFile.write("=" * 70 + "\n");
#======================================================================================================================
#opens the output file for writing the output file and wresults
def openOutputFile():
    global outFile;
    outFile = open("Tobar_Jose_A09_PYTHON_FOR_LOOP_OUTPUT.txt", "w");
    #end of openOuptupt file functions
#======================================================================================================================
#close the external output file
def closeOutputFile():
    outFile.close();
    #end close outputl file finction
#======================================================================================================================
#call functions
initializeVariables(); #initialize varirables
openOutputFile(); #opens theoutput external file
createArray(); #populates the array with actual gpa data
displayGpaList(); #displays a list of gpa data
sortGpaArray(); #sorts the gpa list
displaySortGpaList(); #displays the sorted gpa list
searchGpa(); #searches the list for a specific target gpa and counts number of urrrnacs
displaySearchResults(); #dispalsy the target gpa prints and the number so aof curssz
studentInfo(); #idispalay the student informatn
closeOutputFile(); #after allthe resutls are have ben written, close the output file
#======================================================================================================================
#END OF PROGRAM