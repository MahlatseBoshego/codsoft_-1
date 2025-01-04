print("                                                          Welcome to the calculator\n"
      "        This calculator allows you to pick two numbers and a binary operation of your choice(addition,subtraction,division,multiplication) and yields a result.")




def add_function():
      global num1
      global num2
      result = num1 + num2
      print("Your answer is",result)

def sub_function():
      global num1
      global num2
      result = num1 - num2
      print("Your answer is",result)


def div_function():
      global num1
      global num2
      result = num1 / num2
      print("Your answer is",result)

def mul_function():
      global num1
      global num2
      result = num1 * num2
      print("Your answer is",result)


while True:

      begin =input("Would you like to start (y/n) ").lower()
      if begin =="n":
            quit()



      if begin =="y":

            num1 = int(input("Please enter your first number: "))
            num2 = int(input("Please enter your second number: ")
      while True:
            binary_operation = input("Please select a binary operation: \n"
                                           "Add for Addition, Sub for Subtraction, Mul for Multiply, Div for Division ").lower()

            if binary_operation == "add":
                  add_function()
                  break
            if binary_operation == "sub":
                        sub_function()
                        break
            if binary_operation == "div":
                        div_function()
                        break
            if binary_operation == "mul":
                        mul_function()
                        break
            else:
                        print("Please enter a valid value!")


      else:
            print("Please enter a valid value either (y) or (n) ")



