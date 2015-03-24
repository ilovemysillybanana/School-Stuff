__author__ = 'jose'
# ======================================================================================================================
# Programmer : Jose Tobar
#Program Name: Assignment #09 Creating, sorting and searching gpa array using data files to read data and write results while loop version
#Date Written: 3/1/2015
#======================================================================================================================
#initialize variables and array
def initializeVariables():
    global gpa;
    gpa = [0.00] * 100;  #initializes 101 memory locations to the value of 0.00
    #end of intitializevariables function


#======================================================================================================================
#populate gpa array with data using a text data file
def createArray():
    global gpa;
    count = 0;  # lcv/index -local variable within the scope of this function
    inFile = open("studentGPA.txt", "r");  #in file is a variable name from programmer
    while (count < 25):  #test lcv
        line = inFile.readline();  #read entire line inside the data file
        line = line.strip();  #remove all blank spaces from line
        gpa[count] = float(line);  #move value into gpa array with data type float
        count = count + 1;  #updating lcv
        #end while loop
    inFile.close();
    #end of createArray function


#======================================================================================================================
def displayGpaList():
    count = 0;
    outFile.write("UNSORTED GPA LIST" + "\n");  #writes the label/ttiel
    outFile.write("=" * 25 + "\n");
    while(count < 25):
        outFile.write(format(format("GPA #", "5s") + format(count + 1, "<2"), "^7s") + format(" ===> ", "^5s") + format(gpa[count], "5.2f") + "\n");
        count = count + 1;
        #end of while loop
    outFile.write("=" * 25 + "\n");
    outFile.write("\n");
    #end of display gpa list function
#======================================================================================================================
#searches for particular gpa in the list /array
def searchGpa():
    global targetCount, targetGpa;
    count = 0;
    targetCount = 0;
    targetGpa = float(input("Enter target GPA searching for "));
    while (count < 25):
        if (targetGpa == gpa[count]):
            targetCount = targetCount +1; #counter
        count = count + 1;
        #end if
    #end while
    #end searchGPA
#======================================================================================================================
#displays the results of a gpa search
def displaySearchResults():
    outFile.write("\n");
    outFile.write("=" * 70 + "\n");
    outFile.write("The target GPA " + "\"" + str(targetGpa) +"\"" + ", occur(s) " + str(targetCount) + " time(s)" + "\n");
    outFile.write("=" * 70 + "\n");
    #end display search results function
#======================================================================================================================
def sortGpaArray():
    flag = 0; #indidcates that swap or exhcange of values takes place
    swap = 0; #intiailze swap index
    while(flag == 0):#flag is set to to 0 in this outer loop to begin the sort routine
        flag = 1; #flag is set to 1 to erenter the loopp, if no swap then list sorted
        swap = 0;
        while (swap < (25 - 1)): #if true exchange or swap the adjacent elements
            if(gpa[swap] > gpa[swap + 1]):
                tempGpa = gpa[swap];
                gpa[swap] = gpa[swap + 1];
                gpa[swap + 1] = tempGpa;
                flag = 0; #set to 0 when sap or exhcange is done
                #end if
            swap = swap + 1;
    #end of sortGpaArray function
#======================================================================================================================
#display sorted gpa list
def displaySortGpaList():
    count = 0;
    outFile.write("SORTED GPA LIST" + "\n"); #writes and centers the label title
    outFile.write("=" * 25 + "\n");
    while(count < 25):
        outFile.write(format(format("GPA #", "5s") + format(count + 1, "<2"), "^7s") + format(" ==> ", "^5s") + format(gpa[count], "5.2f") + "\n");
        count = count + 1;
        #end of while loop
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
    outFile = open("Tobar_Jose_A09_PYTHON_WHILE_LOOP_OUTPUT.txt", "w");
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