
number1=float(input("Hi! Please input any number: "))
number2=float(input("enter another number: "))
operand=input("What mathematical operation would you like for your numbers? (insert only +, -,x, / for divide)  ")
result=""

if operand == "+":
    result= number1+number2
elif operand == "-":
    result= number1 - number2
elif operand == "x" :
    result = number1 * number2
else :
    result=number1 / number2


print(f"Here's your answer : {result}" )
