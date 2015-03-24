#===================================================================================================
#PROGRAMMER: JOSE TOBAR
#PROGRAM NAME: Assignment #5 Gross Pay -- Using Functions
''' This program calculates the gross pay based on the numbers of ours worked and
and the rate of pay of an employee. It makes the a program decision based on the number
of hours worked. If the employee works more than 40 hours per week, the program calculates over time hours over time, etc '''
#===================================================================================================

#Initialize variables to ensure accurate data in memory
def initializeVaribles():
    grossPay = 0.00;
    overTimeHours = 0.00;
    overTImePay = 0.00;
    regularPay = 0.00;
    #this is the end of my initializeVariables function
    
#===================================================================================================
#user input elements
def getData():
    global employeeName, hoursWorked, payRate; # makes these local variables available for other functions

    employeeName = str(input("Enter the Employee's Name: " ));
    hoursWorked = float(input("How many hours did " + employeeName + " work? " ));
    payRate = float(input(employeeName + " what is your rate of pay? " ));
    #end of getData function
#===================================================================================================
#information output before calculations
def displayInitialGrossPayData():
    print("\n" +
         ("-" * 60) +
          format("\nPAY ROLL INFORMATION: ", "27s") + format(employeeName, "27s") + ("\n") +
         ("-" * 60) +
          format("\n             HOURS WORKED: ", "27s") + format(hoursWorked, "9.2f") +
          format("\nRATE OF PAY: $", ">27s") + format(payRate, "9,.2f")
          );
    #end of displayInitialGrossPayData function
#===================================================================================================
#function to calculate gross pay if hours worked is less than or equal to 40
def grossPayLessThanOrEqual40():
    global grossPay, payRate; #make these local variables for other functions
    grossPay = hoursWorked * payRate;
    print(format("\nGROSS PAY: $", ">27s") + format(grossPay, "9,.2f"));
    #end of grossPayLessThanOrEqual40 function
#===================================================================================================
#these local variables avaliable for other functions
def grossPayGreaterThan40():
    #these local variables available for other functions
    global overTimeHours, overTimePay, regularPay, grossPay;
    overTimeHours = hoursWorked - 40;
    overTimePay = overTimeHours * (payRate * 1.5);
    regularPay = payRate * 40;
    grossPay = regularPay + overTimePay

    #display output
    print(format("\nOVER TIME HOURS WORKED: = ", ">27s") + format(overTimeHours, "9.2f"));
    print(format("\nOVER PAY: $", ">27s") + format(overTimePay, "9.2f"));
    print(format("\nREGULAR PAY: $", ">27s") + format(regularPay, "9.2f"));
    print(format("\nGROSS PAY: $", ">27s") + format(grossPay, "9,.2f"));
    print("-" * 60);
    #end of grossPayGreaterThan40 function
#===================================================================================================
#Calculations and if statement to determine over time hours, over time pay, regular pay and gross pay
def determinePay():
    if(hoursWorked <= 40):
        grossPayLessThanOrEqual40(); #call the function gross pay <= 40
    else:
        grossPayGreaterThan40(); #call function gross pay > 40
        #end if else
    #end of determineGrossPay function
#===================================================================================================
#call main program (all functions)
initializeVaribles();
getData();
displayInitialGrossPayData();
determinePay();
#===================================================================================================
#END OF PROGRAM
