# Multi-functional Calculator
#### Video Demo: <URL>
## Description:
-> This program offers 3 functionality when you open the program.
<ol>
    <li>
        Calculation <b>(addition, subtraction, division, multiplication, modulo, sin function, cos function and tan function)</b>
    </li><br>
    <li>
        BMI Calculator which show BMI and status <b>(underweight, Healthy weight, Overweight, Obese)</b>
    </li><br>
    <li>
        Unit Converter which can convert <b>(km -> m, m -> km, kg -> lbs, lbs-> kg, °F -> °C, °C -> °F, ft -> m, m -> ft)</b>
    </li>
</ol>
<br>
-> This calculator has 3 main funcionalities:<br/>
<ol>
    <li>General purpose calculator</li>
    <li>BMI(Body Mass Index) calculator</li>
    <li>Unit converter</li>
</ol></br>

### Explanation on Structure of code
-> All of the necessary functions used in the program are in the file project.py. This file houses the entirety of the project.<br>

#### The customs functions used in this project are:
<ol>
    <li>Main function -> <b>def main()</b></li>
    <li>Calculator function -> <b>def calculator()</b></li>
    <li>BMI calculator -> <b>def bmi_calculator()</b></li>
    <li>Kilometer to Meter Function -> <b>def km_to_m()</b></li>
    <li>Meter to Kilometer Function -> <b>def m_to_km()</b></li>
    <li>Kilogram to Pounds Function -> <b>def kg_to_lb()</b></li>
    <li>Pounds to Kilogram Function -> <b>def lb_to_kg()</b></li>
    <li>Fahrenheit to Celcius Function -> <b>def fahrenheit_to_celcius()</b></li>
    <li>Celcius to Fahrenheit Function -> <b>def celcius_to_fahrenheit()</b></li>
    <li>Feet to Meter Function -> <b>def feet_to_meter()</b></li>
    <li>Meter to Feet Function -> <b> def meter_to_feet()</b></li>
</ol>

#### Based on the core functionalities these functions can be grouped as:

-> Group of functions for General Purpose Calculator:
<ul>
    <li>Calculator function -> <b>def calculator()</b></li>
</ul>
</br>

-> Group of functions for BMI calculator:
<ul>
    <li>BMI calculator -> <b>def bmi_calculator()</b></li>
</ul>
</br>

-> Group of functions for Unit converter:
<ol>
    <li>Kilometer to Meter Function -> <b>def km_to_m()</b></li>
    <li>Meter to Kilometer Function -> <b>def m_to_km()</b></li>
    <li>Kilogram to Pounds Function -> <b>def kg_to_lb()</b></li>
    <li>Pounds to Kilogram Function -> <b>def lb_to_kg()</b></li>
    <li>Fahrenheit to Celcius Function -> <b>def fahrenheit_to_celcius()</b></li>
    <li>Celcius to Fahrenheit Function -> <b>def celcius_to_fahrenheit()</b></li>
    <li>Feet to Meter Function -> <b>def feet_to_meter()</b></li>
    <li>Meter to Feet Function -> <b> def meter_to_feet()</b></li>
</ol>
</br>

### Why did I structure my code like this?
-> The main reason I structured my code like these with functions is because every function has defined inputs and defined output. It became a lot easier to test these functionalities when my code was complete.

### Explaining each core functionality and their functions:
#### General Purpose Calculator:
-> This core functionality of this program depends on only one function:
#### # def calculator(operator, first_num = 0, second_num = 0, mode='r')
<b>-> Explaining each parameter of the function:</b>
<ol>
    <li>Operator parameter: Takes one of these string operator <b>'+', '-', '/', '%', 'sin', 'cos', 'tan'</b></li>
    <li>First_num parameter: Takes first operand a integer or float value. Default value is 0</li>
    <li>Second_num parameter: Takes second operand a integer or float value. Default value is 0</li>
    <li>Mode: This parameter sets the mode. Takes <b>'r'</b> for Radian and <b>'d'</b> for Degree. Default value is 'r'</li>
</ol>
<b>-> Explaining the control flow of calculator function:</b>
<ul>
This program uses match operator to match the given operator with the correct operation. After that it simply returns the value after given operation. </br></br>
When certain exceptions such as ZeroDivisionError occur it raises the error and error is handled by main function. That made the function easier to test.If invalid angles such as 90° or 270° for tan is given it raises ValueError.
</ul>

#### BMI(Body Mass Index) Calculator:
-> This core functionality depends on only one function and returns a list with BMI and status <b>(Underweight, Normal weight, Overweight, Obese)</b>:
#### # def bmi_calculator(weight_kg, height_m)
<b>-> Explaining each parameter of the function:</b>
<ol>
    <li>Weight_kg: This parameter expects integer value i.e. in Kilograms</li>
    <li>Height_m: This parameter expects integer value i.e. in Meters</li>
</ol>
<b>-> Explaining the control flow of BMI calculator function:</b>
<ul>
    <li>This function uses the formula <b>weight_in_kgs / (height_in_m)*(height_in_m)</b>.</li>
    <li> After calculating the BMI. It provides status. <b>Below 18.5</b>, it says <b>Underweight</b>.</li>
    <li>Inbetween <b>18.5 and 24.9</b>, it says <b>Healthy Weight</b>.</li> <li>Inbetween <b>25 and 29.9</b>, it says <b>Overweight</b>.</li>
    <li>Inbetween <b>30 and 34.5</b>, it says <b>Obese</b>.</li>
    <li>For <b>more than 34.5</b>, it says <b>Extremely Obese</b></li>
</ul>

#### Unit Converter:
-> This core functionality depends on 8 simple functions. It has features to convert <b>(km -> m, m -> km, kg -> lbs, lbs-> kg, °F -> °C, °C -> °F, ft -> m, m -> ft)</b>
#### # def km_to_m(km)
-> This function has one input parameter called km which expects input as integer in kilometers. It returns meters.
#### # def m_to_km(m)
-> This function has one input parameter called m which expects input as integer in meters. It returns meters.
#### # def kg_to_lb(kg)
-> This function has one input parameter called kg which expects input as integers in kilograms. It returns pounds.
#### # def lb_to_kg(lb)
-> This function has one input parameter called lb which expects input as integers in pounds. It returns kilograms.
#### # def fahrenheit_to_celcius(f)
-> This function has one input parameter called f which expects input as integer in fahrenheit. It uses the formula <b>fahrenheit - 32 / 1.8</b>. It returns celcius
#### # def celcius_to_fahrenheit(c)
-> This function has one input parameter called c which expects input as integer in celcius. It uses the formula <b>celcius * 1.8 + 32</b>. It returns fahrenheit.
#### # def feet_to_meter(f)
-> This function has one input parameter called f which expects input as integer in feet. It returs meter.
#### # def meter_to_feet(m)
-> This function has one input parameter called m which expects input as integer in meter. It returns feet.
### Inside the main function (Control Flow):
    At beginning, It prompts the user to choose between General Calculator, BMI Caculator and Converter. Then If the user chooses General Calculator, It checks if the operator is valid and one of ( + , -, /, %, sin, cos, tan). If operator isn't valid it quits the program. If inside the General Calculator, sin, cos, tan is chosen, it prompts for mode.
<br>

    If (+, -, *, /, %) is chosen, It asks for the left operand and right operand to perform operation on. Here while calculation it also handles ZeroDivisionError and ValueError with try and except block. For ZeroDivisionError 'undefined' is printed. For ValueError 'infinity' message is printed.
<br>

    If the user chooses BMI calculator, it promts the user for age, weight in kgs and height in meter. If the age is less than 14, BMI can't be calculated message is printed. If the input is numerical, it goes ahead and calculates the BMI and prints out the BMI and status of weight.
<br>

    When the user chooses Converter. The program prompts the user for specific unit conversion from available different conversions such as (km -> m, m -> km, kg -> lbs, lbs-> kg, °F -> °C, °C -> °F, ft -> m, m -> ft). It checks if the chosen option is valid and calculates the unit conversion from the available functions to convert unit.

### Enjoy The Multi-functional Calculator












