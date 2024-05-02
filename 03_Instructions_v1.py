want_instructions = input("Do you want to see the instructions? ").lower()

if want_instructions == 'yes' or want_instructions == 'y':
    want_instructions = 'yes'
    print("Instructions goes here.")

elif want_instructions == 'no' or want_instructions == 'n':
    want_instructions = 'no'
    print("Program Continues.")

else:
    print("Please input yes/no.")