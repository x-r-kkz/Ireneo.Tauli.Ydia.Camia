try:
    grade_level = int(input("Enter your grade level: "))
    if 12>= grade_level >= 7 :
        print("Valid grade level.")
    else:
        print("Invalid grade level.")

except ValueError:
    print("Invalid grade level. Please enter a whole number.")
