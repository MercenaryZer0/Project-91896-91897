# Function goes here...

import time
import pandas

def no_blanks(question):
    while True:
        response = input(question)

        if response == '':
            print("No blanks allowed, try again.")
        
        else:
            return response

# Main routine goes here...

