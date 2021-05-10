from art import logo
from replit import clear

def calculate(operation, first_num, second_num):
  """Takes two input numbers, a chosen mathematical operation, and performs the operation on the two numbers and returns the output."""
  if operation == '+':
    output = first_num + second_num
    return output
  elif operation == '-':
    output = first_num - second_num
    return output
  elif operation == '*':
    output = first_num * second_num
    return output
  elif operation == '/':
    output = first_num / second_num
    return output
  else:
    return "Invalid operator chosen."

print(logo)
initial_calc = True

while initial_calc == True:
  num1 = float(input("What's the first number? "))
  subsequent_calc = True
  print("+\n-\n*\n/")
  while subsequent_calc == True:
    operator = input("Pick an operation: ")
    num2 = float(input("What's the second number? "))
    
    result = calculate(operator, num1, num2)
    print(f"{num1} {operator} {num2} = {result}")

    if type(result) == float or type(result) == int:
      y_or_n = input(f"Type 'y' to continue calculating with {result},\nor type 'n' to start a new calculation: ").lower()

      if y_or_n == "n":
        subsequent_calc = False
        clear()
      elif y_or_n == 'y':
        num1 = result
      else:
        subsequent_calc = False
        initial_calc = False
        print("Sorry, you didn't enter 'y' or 'n'.")
        
    else:
        subsequent_calc = False
        initial_calc = False
        print("Sorry, you entered an invalid operator.")
