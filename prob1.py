try: 
  age = int(input("Enter your age: "))
  if age in range(12, 19):
      print("Valid age")

except ValueError:
  print("Invalid input. Please enter a whole number")
