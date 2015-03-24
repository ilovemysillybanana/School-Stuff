#Author: Jose Tobar
#Name: Tobar_Jose_A3_GROSS_PAY_IF_STATEMENT
#Purpose: To input an employee's name, hours worked, over time if any and then output their pay

print("=" * 60);

strEmployeeName = input("Please Enter Employee's Name: ");

float_EmployeePayRate = float(input("Please Input Employee's Rate of Pay: "));
float_EmployeeHoursWorked = float(input("Please Input the Hours this Employee Worked: "));


#Print out preliminary output statements
print("=" * 60);
print(format("PAY ROLL INFORMATION FOR: ", "27s") + format(strEmployeeName, "27s"));
print("=" * 60);
print(format("            HOURS WORKED: ", "27s") + format(float_EmployeeHoursWorked, "8,.2f"));
print(format("            RATE OF PAY: $", ">27s") + format(float_EmployeePayRate, "8,.2f"));
print("=" * 60);

if float_EmployeeHoursWorked <= 40:
    float_GrossPay = float_EmployeePayRate * float_EmployeeHoursWorked;
    print(format("        GROSS PAY: $", ">27s") + format(float_GrossPay, "8,.2f"));
else:
    float_OverTimeHours = float_EmployeeHoursWorked - 40; #get over time hours by taking 40 away from total hours
    float_OverTimePay = float_OverTimeHours * (float_EmployeePayRate * 1.5);#calculate over time pay taking the number of over time hours, multiply it by the pay rate multiplied by 1.5
    float_BasePay = float_EmployeePayRate * 40;#get base pay multiplying 40 hours by their pay rate
    float_GrossPay = float_BasePay + float_OverTimePay;#add ot pay and base pay to get gross
    print(format("       OVER TIME HOURS: ", "27s") + format(float_OverTimeHours, "8,.2f"));
    print(format("       OVER TIME PAY: $", ">27s") + format(float_OverTimePay, "8,.2f"));
    print(format("       TOTAL BASE PAY: $", ">27s") + format(float_BasePay, "8,.2f"));
    print(format("       GROSS PAY: $", ">27s") + format(float_GrossPay, "8,.2f"));
#END IF   
