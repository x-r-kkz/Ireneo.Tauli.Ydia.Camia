#PROBLEM 1

try: 
  age = int(input("Enter your age: "))
  if age in range(12, 19):
      print("Valid age")
  else:
      print("Invalid age. Must be between 12 and 18.")

except ValueError:
  print("Invalid input. Please enter a whole number")
