"""
Instructions

Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

Warning you should convert the result to a whole number.
Example Input

weight = 80
weight = 80

height = 1.75
height = 1.75

Example Output

80 ÷ (1.75 x 1.75) = 26.122448979591837

26
26

e.g. When you hit run, this is what should happen:

https://cdn.fs.teachablecdn.com/wmjVjddeSmGj0QVtOUrE
Hint

    Check the data type of the inputs.
    Try to use the exponent operator in your code.
    Remember PEMDAS.
    Remember to convert your result to a whole number (int).

"""


height = input("Enter the height")

weight = float(input("Enter the weight"))

BMI = weight/(height**2)

print(BMI)