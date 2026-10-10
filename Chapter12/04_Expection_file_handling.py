try:
    num1 = int(input("Enter a number1: "))
    num2 = int(input("Enter a number2: "))
    print(num1/num2)
    
except ZeroDivisionError:
    print("error: we can not divide by 0 ")

except Exception as e:
    print(e)

except ValueError:
    print("Error: Give correct input. ")

finally:
    print("program executed successfully. ")





